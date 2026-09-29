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


def test_rejects_duplicate_names():
    csv = GOOD_CSV + "Mt Baker,peak,easy,\"48.7767,-121.8144\",,again\r\n"
    with pytest.raises(ValueError, match="duplicate"):
        parse_locations(csv, BBOX)


def test_rejects_unknown_category():
    csv = (
        "name,category,difficulty,geometry,image,blurb\r\n"
        "Odd,volcanoe,easy,\"48.0,-121.0\",,x\r\n"
    )
    with pytest.raises(ValueError, match="Odd.*category"):
        parse_locations(csv, BBOX, categories={"peak"})


def test_skips_blank_trailing_rows():
    locs = parse_locations(GOOD_CSV + ",,,,,\r\n,,,,,\r\n", BBOX)
    assert len(locs) == 3


def test_rejects_point_outside_region_mask():
    square = [[[47.0, -123.0], [47.0, -121.0], [49.0, -121.0], [49.0, -123.0]]]
    ok = parse_locations(GOOD_CSV.split("Wapta")[0], BBOX, region=square)
    assert [l.name for l in ok] == ["Mt Baker"]
    with pytest.raises(ValueError, match="Wapta.*region"):
        parse_locations(GOOD_CSV, BBOX, region=square)


def test_kind_point_line_area_and_loop_route():
    ring = '"49.0,-120.0; 49.0,-119.0; 50.0,-119.0; 49.0,-120.0"'
    csv = (
        "name,category,difficulty,geometry,image,blurb\r\n"
        'Pt,peak,easy,"48.0,-121.0",,x\r\n'
        'Ln,river,easy,"48.0,-121.0; 48.5,-121.0",,x\r\n'
        f"Lk,lake,easy,{ring},,x\r\n"
        f"Loop,traverse,easy,{ring},,x\r\n"
    )
    kinds = {l.name: l.kind for l in parse_locations(csv, BBOX)}
    assert kinds == {"Pt": "point", "Ln": "line", "Lk": "area", "Loop": "line"}


def test_facts_column_is_parsed_and_validated():
    from pnwtap import config
    csv = (
        "name,category,difficulty,geometry,image,blurb,facts\r\n"
        'BNW,climb,hard,"47.4980,-121.7549",,x,"grade: 5.14d | style: sport"\r\n'
    )
    assert parse_locations(csv, BBOX, facts_registry=config.FACTS)[0].facts == {"grade": "5.14d", "style": "sport"}
    bad = csv.replace("style: sport", "styel: sport")
    with pytest.raises(ValueError, match="BNW.*unknown fact"):
        parse_locations(bad, BBOX, facts_registry=config.FACTS)


def test_coordinates_are_kept_to_four_decimals():
    from pnwtap.sheet import parse_locations
    from pnwtap import config
    csv_text = "name,category,difficulty,geometry,image,blurb\nX,peak,easy,\"47.433612,-121.773598\",,b\n"
    loc = parse_locations(csv_text, config.BBOX)[0]
    assert loc.geometry == [(47.4336, -121.7736)]


ANY_ROW = ('name,category,difficulty,geometry,image,blurb\n'
           'Any growing glacier,glacier,hard,"Crater Glacier: 46.2000,-122.1900; 46.2100,-122.1800; 46.2050,-122.1700; 46.2000,-122.1900 | '
           'Hubbard Glacier: 60.0200,-139.5000",,b\n')


def test_an_any_of_row_has_named_members():
    from pnwtap.sheet import parse_locations
    from pnwtap import config
    loc = parse_locations(ANY_ROW, config.BBOX)[0]
    assert loc.kind == "any"
    assert [(m.name, m.kind) for m in loc.members] == [("Crater Glacier", "area"), ("Hubbard Glacier", "point")]
    assert len(loc.geometry) == 5                      # every member's points, for validation


@pytest.mark.parametrize("cell, msg", [
    ("46.2,-122.19 | Hubbard Glacier: 60.02,-139.5", "needs a name"),
    ("A: 46.2,-122.19 | A: 60.02,-139.5", "share a name"),
    ("A: 46.2,-122.19 | B: 10.0,-139.5", "outside"),
])
def test_bad_any_of_rows_name_the_problem(cell, msg):
    from pnwtap.sheet import parse_locations
    from pnwtap import config
    with pytest.raises(ValueError, match=msg):
        parse_locations(f'name,category,difficulty,geometry,image,blurb\nX,glacier,hard,"{cell}",,b\n', config.BBOX)


def test_an_any_of_row_cannot_have_an_image():
    from pnwtap.sheet import parse_locations
    from pnwtap import config
    row = ANY_ROW.replace('",,b', '",https://example.com/x.jpg,b')
    with pytest.raises(ValueError, match="can't have an image"):
        parse_locations(row, config.BBOX)
