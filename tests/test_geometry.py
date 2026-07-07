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
