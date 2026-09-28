import pytest
from pnwtap.geometry import (
    parse_geometry, haversine_km, nearest_point_km, within_bbox,
)


def test_parse_single_point():
    assert parse_geometry("48.7767,-121.8144") == [(48.7767, -121.8144)]


def test_parse_multi_point_line():
    pts = parse_geometry("51.68,-116.45; 51.60,-116.40; 51.53,-116.34")
    assert pts == [(51.68, -116.45), (51.60, -116.40), (51.53, -116.34)]


def test_parse_rejects_bad_pair():
    with pytest.raises(ValueError):
        parse_geometry("48.7767")


def test_parse_rejects_empty():
    with pytest.raises(ValueError):
        parse_geometry("   ")


def test_haversine_seattle_to_portland():
    seattle = (47.6062, -122.3321)
    portland = (45.5152, -122.6784)
    assert haversine_km(seattle, portland) == pytest.approx(233, abs=5)


def test_nearest_point_single():
    baker = (48.7767, -121.8144)
    # ~0 km when tapping the point itself
    assert nearest_point_km(baker, [baker]) == pytest.approx(0, abs=0.01)


def test_nearest_point_line_is_near_midsegment():
    # a tap right next to the middle of a line should score much closer
    # than the distance to either endpoint
    line = [(48.0, -121.6), (48.0, -121.0)]
    tap = (48.02, -121.3)  # just north of the segment midpoint
    d_mid = nearest_point_km(tap, line)
    d_end = haversine_km(tap, line[0])
    assert d_mid < d_end
    assert d_mid == pytest.approx(2.2, abs=1.0)  # ~0.02 deg lat ≈ 2.2 km


def test_nearest_point_rejects_empty_path():
    with pytest.raises(ValueError):
        nearest_point_km((48.0, -121.0), [])


def test_within_bbox():
    bbox = (41.0, -126.0, 56.0, -112.0)
    assert within_bbox((48.5, -121.0), bbox) is True
    assert within_bbox((60.0, -121.0), bbox) is False


def test_in_region_multiple_rings():
    from pnwtap.geometry import in_region
    a = [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0]]
    b = [[5.0, 5.0], [5.0, 6.0], [6.0, 6.0], [6.0, 5.0]]
    assert in_region((0.5, 0.5), [a, b])
    assert in_region((5.5, 5.5), [a, b])
    assert not in_region((3.0, 3.0), [a, b])


def test_in_region_real_mask_contains_sample_places():
    import json, pathlib
    from pnwtap.geometry import in_region
    mask = json.loads((pathlib.Path(__file__).parent.parent / "data" / "region_mask.json").read_text())
    assert in_region((48.7767, -121.8144), mask)      # Mt Baker
    assert in_region((60.7212, -135.0568), mask)      # Whitehorse
    assert not in_region((40.7608, -111.8910), mask)  # Salt Lake City
    assert not in_region((46.8721, -113.9940), mask)  # Missoula, Montana


# ---- areas & size-calibrated decay ----
from pnwtap.geometry import area_km2, decay_km, is_closed

SQUARE = [(49.0, -120.0), (49.0, -119.0), (50.0, -119.0), (50.0, -120.0), (49.0, -120.0)]


def test_area_scores_zero_inside_but_a_loop_does_not():
    assert is_closed(SQUARE)
    assert not is_closed(SQUARE[:-1])
    assert nearest_point_km((49.5, -119.5), SQUARE, area=True) == 0.0
    assert nearest_point_km((49.5, -119.5), SQUARE) == pytest.approx(36.4, abs=0.5)   # loop: to the edge
    assert nearest_point_km((49.5, -118.9), SQUARE, area=True) == pytest.approx(7.2, abs=0.3)


def test_area_km2_of_one_degree_square():
    assert area_km2(SQUARE) == pytest.approx(111.2 * 72.9, rel=0.02)


def test_decay_areas_and_loops():
    assert decay_km(SQUARE, 40, 10, area=True) == 10          # 8,000 km² dwarfs a point's zone
    small = [(49.0, -120.0), (49.0, -119.9), (49.1, -119.9), (49.1, -120.0), (49.0, -120.0)]
    as_loop = decay_km(small, 40, 10)                          # ~40 km loop route
    as_area = decay_km(small, 40, 10, area=True)               # ~80 km² lake
    assert 10 < as_loop < as_area < 40


def test_decay_point_keeps_base():
    assert decay_km([(48.0, -121.0)], 40, 10) == 40


def test_decay_shrinks_with_length_and_hits_floor():
    short = [(48.0, -121.0), (48.1, -121.0)]              # ~11 km
    medium = [(48.0, -121.0), (49.0, -121.0)]             # ~111 km
    long = [(45.0, -121.0), (53.0, -121.0)]               # ~890 km
    d_short, d_med, d_long = (decay_km(p, 40, 10) for p in (short, medium, long))
    assert 35 < d_short < 40
    assert 10 < d_med < d_short
    assert d_long == 10


def test_decay_equalises_the_good_zone():
    import math
    line = [(48.0, -121.0), (48.5, -121.0)]
    d = decay_km(line, 40, 1)
    from pnwtap.geometry import length_km
    zone = 2 * length_km(line) * d + math.pi * d * d
    assert zone == pytest.approx(math.pi * 40 ** 2, rel=1e-6)
