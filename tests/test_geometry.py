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


# ---- areas & the score curve ----
from pnwtap.geometry import is_closed, score

SQUARE = [(49.0, -120.0), (49.0, -119.0), (50.0, -119.0), (50.0, -120.0), (49.0, -120.0)]


def test_area_scores_zero_inside_but_a_loop_does_not():
    assert is_closed(SQUARE)
    assert not is_closed(SQUARE[:-1])
    assert nearest_point_km((49.5, -119.5), SQUARE, area=True) == 0.0
    assert nearest_point_km((49.5, -119.5), SQUARE) == pytest.approx(36.4, abs=0.5)   # loop: to the edge
    assert nearest_point_km((49.5, -118.9), SQUARE, area=True) == pytest.approx(7.2, abs=0.3)


def test_score_curve_landmarks():
    s = lambda km: score(km, 10, 1500, 2)
    assert s(0) == 100
    assert s(3) == 99            # a near miss costs almost nothing
    assert s(10) == 93
    assert s(20) == 84
    assert s(117) == 51          # 'it's in the scablands' still counts
    assert s(1500) == 0
    assert s(5000) == 0


def test_score_every_halving_is_worth_about_the_same_far_out():
    s = lambda km: score(km, 10, 1500, 2)
    gains = [s(d / 2) - s(d) for d in (1200, 800, 400, 200, 100)]
    assert max(gains) - min(gains) <= 2
    assert all(12 <= g <= 16 for g in gains)


def test_score_shape_one_is_plain_log():
    assert score(5, 5, 1500) == 88 and score(50, 5, 1500) == 58


def test_score_is_monotone():
    vals = [score(d / 4, 10, 1500, 2) for d in range(0, 8000)]
    assert all(a >= b for a, b in zip(vals, vals[1:]))


def test_polyline_round_trips_exactly():
    from pnwtap.geometry import encode_polyline, decode_polyline
    paths = [
        [(48.7767, -121.8144)],
        [(48.09, -121.62), (48.06, -121.47), (47.93, -121.09)],
        [(60.2576, -141.9), (69.7396, -141.8977), (41.5, -109.5), (0.0, 0.0), (-0.0001, 0.0001)],
    ]
    for path in paths:
        assert decode_polyline(encode_polyline(path)) == [list(p) for p in path]
    assert encode_polyline([(38.5, -120.2), (40.7, -120.95), (43.252, -126.453)], 1e5) == "_p~iF~ps|U_ulLnnqC_mqNvxq`@"
