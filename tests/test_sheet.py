import pytest
from pnwtap.sheet import parse_locations, Location

BBOX = (41.0, -126.0, 56.0, -112.0)

GOOD_CSV = (
    "name,category,difficulty,geometry,image,blurb\r\n"
    "Mt Baker,peak,easy,\"48.7767,-121.8144\",,Glaciated stratovolcano\r\n"
    "Wapta Traverse,traverse,hard,\"51.68,-116.45; 51.60,-116.40\",,Icefield ski route\r\n"
    "Fremont Troll,poi,hard,\"47.6510,-122.3473\",http://example.com/troll.jpg,Under the bridge\r\n"
)


def test_parses_rows_into_locations():
    locs = parse_locations(GOOD_CSV, BBOX)
    assert len(locs) == 3
    assert isinstance(locs[0], Location)
    assert locs[0].name == "Mt Baker"
    assert locs[0].geometry == [(48.7767, -121.8144)]
    assert locs[0].image is None
    assert locs[1].geometry == [(51.68, -116.45), (51.60, -116.40)]
    assert locs[2].image == "http://example.com/troll.jpg"


def test_rejects_bad_difficulty():
    csv = (
        "name,category,difficulty,geometry,image,blurb\r\n"
        "Bad,peak,trivial,\"48.0,-121.0\",,x\r\n"
    )
    with pytest.raises(ValueError, match="Bad"):
        parse_locations(csv, BBOX)


def test_rejects_out_of_bbox():
    csv = (
        "name,category,difficulty,geometry,image,blurb\r\n"
        "Faraway,peak,easy,\"12.0,-121.0\",,x\r\n"
    )
    with pytest.raises(ValueError) as exc:
        parse_locations(csv, BBOX)
    msg = str(exc.value)
    assert "bbox" in msg
    assert "Faraway" in msg          # error must name the offending row


def test_rejects_missing_name():
    csv = (
        "name,category,difficulty,geometry,image,blurb\r\n"
        ",peak,easy,\"48.0,-121.0\",,x\r\n"
    )
    with pytest.raises(ValueError, match="name"):
        parse_locations(csv, BBOX)
