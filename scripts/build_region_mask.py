"""Regenerate data/region_mask.json — the stencil outline of the play region.

Downloads Natural Earth admin-1 boundaries, keeps the target states/provinces,
unions them into one outline (so internal borders vanish), simplifies, and
writes the result as a list of [lat, lng] rings for the browser mask.

The output is committed, so the normal build does NOT need this or shapely.
Only run this to change which regions the stencil covers.

Requires: shapely  (pip install shapely)
Usage:    python scripts/build_region_mask.py
"""
import json
import os
import ssl
import urllib.request

from shapely.geometry import shape
from shapely.ops import unary_union

NE_URL = (
    "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
    "master/geojson/ne_50m_admin_1_states_provinces.geojson"
)
REGIONS = {"Washington", "Oregon", "British Columbia", "Alberta", "Yukon"}
COUNTRIES = {"Canada", "United States of America"}
COAST_BUFFER_DEG = 0.9   # ~100 km outward margin: smooths the edge and takes in coastal islands
SIMPLIFY_TOL = 0.03      # degrees; larger = coarser outline
MIN_ISLAND_DIAG = 0.4    # drop leftover islands smaller than this (bbox diagonal, degrees)
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "region_mask.json")


def _perp(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
    t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return ((px - (ax + t * dx)) ** 2 + (py - (ay + t * dy)) ** 2) ** 0.5


def _simplify(points, tol):
    """Douglas-Peucker on a list of (lng, lat) points."""
    if len(points) < 3:
        return points
    a, b = points[0], points[-1]
    dmax, idx = 0, 0
    for i in range(1, len(points) - 1):
        d = _perp(points[i], a, b)
        if d > dmax:
            dmax, idx = d, i
    if dmax > tol:
        return _simplify(points[: idx + 1], tol)[:-1] + _simplify(points[idx:], tol)
    return [a, b]


def _diag(ring):
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return ((max(xs) - min(xs)) ** 2 + (max(ys) - min(ys)) ** 2) ** 0.5


def main():
    data = json.loads(urllib.request.urlopen(NE_URL, timeout=60, context=ssl.create_default_context()).read())
    geoms = [
        shape(f["geometry"])
        for f in data["features"]
        if f["properties"].get("name") in REGIONS and f["properties"].get("admin") in COUNTRIES
    ]
    if len(geoms) != len(REGIONS):
        raise SystemExit(f"expected {len(REGIONS)} regions, matched {len(geoms)}")

    # union adjacent regions, then expand outward ~100 km so the edge is smooth
    # (not blocky) and coastal islands — San Juans, Gulf Islands, Haida Gwaii —
    # fall inside the stencil rather than being cut out as sea.
    merged = unary_union([g.buffer(0) for g in geoms])
    region = merged.buffer(COAST_BUFFER_DEG, join_style=1)  # round joins = smooth coast
    polys = [region] if region.geom_type == "Polygon" else list(region.geoms)

    rings = []
    for poly in polys:
        ext = list(poly.exterior.coords)  # (lng, lat)
        if _diag(ext) < MIN_ISLAND_DIAG:
            continue
        simplified = _simplify(ext, SIMPLIFY_TOL)
        if len(simplified) >= 4:
            rings.append([[round(lat, 4), round(lng, 4)] for lng, lat in simplified])

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(rings, fh)

    pts = sum(len(r) for r in rings)
    print(f"wrote {os.path.relpath(OUT_PATH)}: {len(rings)} rings, {pts} points")


if __name__ == "__main__":
    main()
