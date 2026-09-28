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
# case). Change both in lockstep — tests/test_scoring_parity.py checks them.
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


def _centroid(path):
    return (sum(p[0] for p in path) / len(path), sum(p[1] for p in path) / len(path))


def length_km(path: list[tuple[float, float]]) -> float:
    """Total length of the polyline (the perimeter, for an area)."""
    return sum(haversine_km(path[i], path[i + 1]) for i in range(len(path) - 1))


def area_km2(path: list[tuple[float, float]]) -> float:
    """Planar (shoelace) area of a closed ring, in km²; 0 for anything not closed."""
    if not is_closed(path):
        return 0.0
    c = _centroid(path)
    xy = [_project(c, p) for p in path]
    return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(xy, xy[1:]))) / 2


def decay_km(path: list[tuple[float, float]], base_km: float, floor_km: float, area: bool = False) -> float:
    """Score decay distance for this feature, calibrated so a big feature isn't a freebie.

    The zone where you score >= 37 (within one decay distance) should cover the same
    area as it does for a single point: pi * base². For a feature with area A and
    perimeter P that zone is roughly A + P*d + pi*d², so solve for d — clamped to
    [floor_km, base_km]. A point keeps `base_km`; a 1,000 km river hits the floor.
    """
    if len(path) == 1:
        return base_km
    a = area_km2(path) if area else 0.0
    p = length_km(path) if area else 2 * length_km(path)  # a line's zone has two sides
    target = math.pi * base_km ** 2 - a
    if target <= 0:
        return floor_km
    d = (-p + math.sqrt(p * p + 4 * math.pi * target)) / (2 * math.pi)
    return max(floor_km, min(base_km, d))


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
