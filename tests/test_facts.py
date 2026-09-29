import pytest

from pnwtap import config
from pnwtap.facts import card, clue_text, full_value, parse_facts


def test_parse_facts_basic_and_blank():
    assert parse_facts("") == {}
    assert parse_facts("grade: 5.14d | style: sport") == {"grade": "5.14d", "style": "sport"}
    # values may contain colons and commas; only the first colon splits
    assert parse_facts("first_ascent: 1870, Stevens: Van Trump") == {"first_ascent": "1870, Stevens: Van Trump"}


@pytest.mark.parametrize("cell, msg", [
    ("grade 5.9", "key: value"),
    ("grade: 5.9 | grade: 5.10", "twice"),
    ("gradee: 5.9", "unknown fact"),
    ("elevation_m: tall", "number"),
])
def test_parse_facts_rejects(cell, msg):
    with pytest.raises(ValueError, match=msg):
        parse_facts(cell, config.FACTS)


def test_feet_round_trip_with_one_decimal():
    assert full_value("m", "4392.2") == "4,392 m (14,410 ft)"      # Rainier's famous 14,410
    assert full_value("m", "184.4") == "184 m (605 ft)"            # Space Needle
    assert full_value("km", "1375") == "1,375 km (854 mi)"
    assert full_value("km", "6.5") == "6.5 km (4 mi)"
    assert full_value("km2", "344.6") == "345 km² (133 sq mi)"
    assert full_value("int", "18") == "18"


def test_clue_text_forms():
    assert clue_text("pitches", "1", "climb") == "1 pitch"
    assert clue_text("pitches", "23", "climb") == "23 pitches"
    assert clue_text("population", "1,010,899 (2021)", "town") == "pop. 1,010,899"
    assert clue_text("elevation_m", "3619", "peak") == "3,619 m"
    assert clue_text("elevation_m", "645", "town") == "elev. 645 m"
    assert clue_text("height_m", "189", "waterfall") == "189 m drop"


def test_card_orders_by_category_and_keeps_where_facts_off_the_prompt():
    facts = parse_facts("range: North Cascades | first_ascent: 1936 | elevation_m: 2652 "
                        "| type: granite spire | tagline: A test tagline", config.FACTS)
    c = card(facts, "peak", config.FACTS, config.CARDS)
    assert c["tagline"] == "A test tagline"
    assert [r[0] for r in c["rows"]] == ["Elevation", "Type", "Range", "First ascent"]
    assert c["clues"] == ["2,652 m", "granite spire"]              # range / first ascent aren't clues


def test_card_caps_clues_at_three():
    facts = parse_facts("grade: 5.9 | style: sport | pitches: 18 | length_m: 548.6", config.FACTS)
    assert card(facts, "climb", config.FACTS, config.CARDS)["clues"] == ["5.9", "sport", "18 pitches"]


def test_every_card_key_is_registered():
    for cat, keys in config.CARDS.items():
        assert cat in config.CATEGORIES
        assert set(keys) <= set(config.FACTS)


def test_small_areas_read_in_acres():
    from pnwtap.facts import full_value, clue_text
    assert full_value("km2", "0.1016") == "0.1 km² (25 acres)"          # Rachel Lake, 25.1 ac
    assert full_value("km2", "0.01133") == "0.011 km² (2.8 acres)"      # Lila Lake, 2.8 ac
    assert full_value("km2", "0.355") == "0.35 km² (88 acres)"
    assert full_value("km2", "2.266") == "2.3 km² (560 acres)"
    assert full_value("km2", "2.59") == "2.6 km² (1 sq mi)"             # a square mile and up: sq mi
    assert clue_text("area_km2", "0.01133", "lake") == "0.011 km²"


def test_a_length_clue_says_long():
    from pnwtap.facts import clue_text
    assert clue_text("length_km", "50", "traverse") == "50 km long"   # not "50 km", which reads like a miss
