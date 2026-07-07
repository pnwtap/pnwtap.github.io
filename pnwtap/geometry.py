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


def nearest_point_km(tap: tuple[float, float], path: list[tuple[float, float]]) -> float:
    """Distance in km from `tap` to the nearest point on `path` (point or polyline)."""
    if not path:
        raise ValueError("empty path")
    if len(path) == 1:
        return haversine_km(tap, path[0])
    return min(_segment_dist_km(tap, path[i], path[i + 1]) for i in range(len(path) - 1))


def within_bbox(pt: tuple[float, float], bbox: tuple[float, float, float, float]) -> bool:
    """True if pt (lat, lng) lies within bbox (min_lat, min_lng, max_lat, max_lng)."""
    min_lat, min_lng, max_lat, max_lng = bbox
    return min_lat <= pt[0] <= max_lat and min_lng <= pt[1] <= max_lng
