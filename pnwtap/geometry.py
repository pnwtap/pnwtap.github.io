"""Geometry helpers: parse coordinate strings, great-circle and nearest-point distances."""
import math

EARTH_RADIUS_KM = 6371.0088


def parse_geometry(s: str) -> list[tuple[float, float]]:
    """Parse "lat,lng; lat,lng; ..." into a list of (lat, lng) tuples."""
    points: list[tuple[float, float]] = []
    for chunk in s.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = chunk.split(",")
        if len(parts) != 2:
            raise ValueError(f"bad coordinate pair: {chunk!r}")
        points.append((float(parts[0]), float(parts[1])))
    if not points:
        raise ValueError("empty geometry")
    return points


# NOTE: static/scoring.js mirrors haversine_km / nearest_point_km (incl. the area
# case) / score. Change both in lockstep — tests/test_scoring_parity.py checks them.
def haversine_km(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Great-circle distance in km between two (lat, lng) points."""
    lat1, lat2 = math.radians(a[0]), math.radians(b[0])
    dphi = math.radians(b[0] - a[0])
    dlmb = math.radians(b[1] - a[1])
    h = math.sin(dphi / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlmb / 2) ** 2
    return 2 * EARTH_RADIUS_KM * math.asin(min(1.0, math.sqrt(h)))


def _project(origin: tuple[float, float], pt: tuple[float, float]) -> tuple[float, float]:
    """Local equirectangular projection to km offsets relative to `origin`."""
    x = math.radians(pt[1] - origin[1]) * math.cos(math.radians(origin[0])) * EARTH_RADIUS_KM
    y = math.radians(pt[0] - origin[0]) * EARTH_RADIUS_KM
    return x, y


def _segment_dist_km(tap: tuple[float, float], a: tuple[float, float], b: tuple[float, float]) -> float:
    """Distance in km from `tap` to segment a–b (planar approximation, fine at PNW scales)."""
    ax, ay = _project(tap, a)
    bx, by = _project(tap, b)  # tap projects to the origin (0, 0)
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(ax, ay)
    t = -(ax * dx + ay * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(ax + t * dx, ay + t * dy)


def is_closed(path: list[tuple[float, float]]) -> bool:
    """A closed ring: 4+ points with the last equal to the first."""
    return len(path) >= 4 and tuple(path[0]) == tuple(path[-1])


def nearest_point_km(tap: tuple[float, float], path: list[tuple[float, float]], area: bool = False) -> float:
    """Distance in km from `tap` to `path` (a point or polyline); for an `area`, 0 inside the ring."""
    if not path:
        raise ValueError("empty path")
    if len(path) == 1:
        return haversine_km(tap, path[0])
    if area and in_region(tap, [path]):
        return 0.0
    return min(_segment_dist_km(tap, path[i], path[i + 1]) for i in range(len(path) - 1))


def nearest_member_km(tap: tuple[float, float], members) -> tuple[float, int]:
    """(km, index) of the nearest of several (path, area) targets: an "any of" place."""
    return min((nearest_point_km(tap, path, area), i) for i, (path, area) in enumerate(members))


def score(km: float, near_km: float, zero_km: float, shape: float = 1.0) -> int:
    """Round score for a miss of `km`: 100 at 0, nearly flat out to ~`near_km`, then
    log-scaled (every halving of the miss is worth the same points), 0 at `zero_km`."""
    frac = 1 - math.log1p((km / near_km) ** shape) / math.log1p((zero_km / near_km) ** shape)
    return math.floor(100 * max(0.0, frac) + 0.5)   # round half up, like JS Math.round


def within_bbox(pt: tuple[float, float], bbox: tuple[float, float, float, float]) -> bool:
    """True if pt (lat, lng) lies within bbox (min_lat, min_lng, max_lat, max_lng)."""
    min_lat, min_lng, max_lat, max_lng = bbox
    return min_lat <= pt[0] <= max_lat and min_lng <= pt[1] <= max_lng


def in_region(pt: tuple[float, float], rings: list[list[list[float]]]) -> bool:
    """True if pt (lat, lng) falls inside any of the region-mask rings ([[lat, lng], ...])."""
    lat, lng = pt
    for ring in rings:
        inside = False
        j = len(ring) - 1
        for i in range(len(ring)):
            (yi, xi), (yj, xj) = ring[i], ring[j]
            if (yi > lat) != (yj > lat) and lng < (xj - xi) * (lat - yi) / (yj - yi) + xi:
                inside = not inside
            j = i
        if inside:
            return True
    return False


# The page carries every path as an encoded polyline (Google's algorithm, 1e4 precision:
# ~10 m, which is all the source data has): about a fifth the size of JSON arrays.
# static/scoring.js decodes it; keep the two in lockstep.
POLYLINE_PRECISION = 1e4


def encode_polyline(path, precision: float = POLYLINE_PRECISION) -> str:
    out, prev = [], (0, 0)
    for lat, lng in path:
        cur = (round(lat * precision), round(lng * precision))
        for d in (cur[0] - prev[0], cur[1] - prev[1]):
            v = ~(d << 1) if d < 0 else d << 1
            while v >= 0x20:
                out.append(chr((0x20 | (v & 0x1F)) + 63))
                v >>= 5
            out.append(chr(v + 63))
        prev = cur
    return "".join(out)


def decode_polyline(s: str, precision: float = POLYLINE_PRECISION) -> list[list[float]]:
    out, i, acc = [], 0, [0, 0]
    while i < len(s):
        for k in (0, 1):
            shift = result = 0
            while True:
                b = ord(s[i]) - 63
                i += 1
                result |= (b & 0x1F) << shift
                shift += 5
                if b < 0x20:
                    break
            acc[k] += ~(result >> 1) if result & 1 else result >> 1
        out.append([acc[0] / precision, acc[1] / precision])
    return out
