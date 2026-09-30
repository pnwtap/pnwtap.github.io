import json
from datetime import date
from pnwtap.sheet import Location
from pnwtap.schedule import build_schedule
from pnwtap.render import build_payload, render_site
from pnwtap import config


def _pool():
    diffs = ["easy", "medium", "hard", "hard"]
    return [Location(d + str(i), "peak", d, [(48.0, -121.0)], None, "b")
            for i, d in enumerate(diffs * 1)]


def test_payload_shape():
    locs = _pool()
    sched = build_schedule(locs, date(2026, 7, 7), 3, config.RAMP, seed=0)
    payload = build_payload(locs, sched, {}, config)
    assert payload["locations"][0]["geometry"] == [[48.0, -121.0]]
    assert payload["locations"][0]["image"] is None
    assert payload["config"]["scoreNearKm"] == config.SCORE_NEAR_KM
    assert payload["config"]["categories"]["poi"] == {"icon": "📍", "label": "landmark"}
    assert payload["locations"][0]["facts"] == {"tagline": None, "clues": [], "rows": []}
    assert 100 * sum(payload["config"]["multipliers"]) == 1000


def test_render_writes_self_contained_site(tmp_path):
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    locs = _pool()
    sched = build_schedule(locs, date(2026, 7, 7), 3, config.RAMP, seed=0)
    index = render_site(locs, sched, {}, config,
                        docs_dir=tmp_path, template_dir=root / "templates",
                        static_dir=root / "static")
    html = index.read_text(encoding="utf-8")
    assert "window.PNWTAP" in html
    assert "easy0" in html                       # a location name is baked in
    assert (tmp_path / "game.js").exists()
    assert (tmp_path / "style.css").exists()


def test_script_breakout_is_escaped(tmp_path):
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    locs = [Location("Evil", "peak", d, [(48.0, -121.0)], None, "</script><b>x</b>")
            for d in ["easy", "medium", "hard", "hard"]]
    sched = build_schedule(locs, date(2026, 7, 7), 3, config.RAMP, seed=0)
    index = render_site(locs, sched, {}, config,
                        docs_dir=tmp_path, template_dir=root / "templates",
                        static_dir=root / "static")
    html = index.read_text(encoding="utf-8")
    assert "</script><b>x</b>" not in html      # raw breakout must not survive
    assert "\\u003c/script>" in html              # escaped form is present


def test_assets_are_cache_busted_and_copied(tmp_path):
    import pathlib, re
    root = pathlib.Path(__file__).resolve().parent.parent
    locs = _pool()
    sched = build_schedule(locs, date(2026, 7, 7), 3, config.RAMP, seed=0)
    html = render_site(locs, sched, {}, config, docs_dir=tmp_path,
                       template_dir=root / "templates", static_dir=root / "static").read_text()
    for asset in ("style.css", "scoring.js", "game.js"):
        assert re.search(rf'{re.escape(asset)}\?v=[0-9a-f]{{10}}"', html), asset
        assert (tmp_path / asset).exists()


def test_payload_carries_epoch_and_categories():
    locs = _pool()
    payload = build_payload(locs, {}, {}, config)
    assert payload["config"]["epoch"] == config.EPOCH
    assert payload["config"]["categories"]["peak"]
    assert payload["config"]["startBounds"] == config.START_BOUNDS


def _render(tmp_path, locs=None):
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    locs = locs or _pool()
    sched = build_schedule(locs, date(2026, 7, 7), 3, config.RAMP, seed=0)
    html = render_site(locs, sched, {}, config, docs_dir=tmp_path,
                       template_dir=root / "templates", static_dir=root / "static").read_text()
    return root, html


def test_geometry_ships_as_polylines(tmp_path):
    from pnwtap.geometry import decode_polyline
    locs = [Location("Loop" + d, "hike", d, [(48.09, -121.62), (48.06, -121.47), (48.09, -121.62)], None, "b")
            for d in ["easy", "medium", "hard", "hard"]]
    _, html = _render(tmp_path, locs)
    payload = json.loads(html.split("window.PNWTAP = ", 1)[1].split(";</script>", 1)[0])
    geom = payload["locations"][0]["geometry"]
    assert isinstance(geom, str)
    assert decode_polyline(geom) == [[48.09, -121.62], [48.06, -121.47], [48.09, -121.62]]


def test_page_loads_only_first_party_code_in_order(tmp_path):
    import re
    root, html = _render(tmp_path)
    head = html.split("</head>", 1)[0]
    scripts = re.findall(r'<script defer src="([^"?]+)\?v=[0-9a-f]{10}"></script>', head)
    assert scripts == ["leaflet.js", "scoring.js", "game.js"]      # deferred, so they run in this order
    assert "unpkg.com" not in html and "fonts.googleapis" not in html and "fonts.gstatic" not in html
    for sheet in ("leaflet.css", "style.css"):
        assert re.search(rf'<link rel="stylesheet" href="{sheet}\?v=[0-9a-f]{{10}}">', head), sheet
    # every self-hosted font the stylesheet names exists, and the preload matches one exactly
    css = (root / "static" / "style.css").read_text()
    fonts = re.findall(r'url\("([^"]+\.woff2)"\)', css)
    assert fonts and all((root / "static" / f).exists() and (tmp_path / f).exists() for f in fonts)
    preload = re.search(r'<link rel="preload" href="([^"]+)" as="font" type="font/woff2" crossorigin>', head)
    assert preload and preload.group(1) in fonts


def test_phone_start_tiles_are_preloaded(tmp_path):
    import re
    _, html = _render(tmp_path)
    hrefs = re.findall(r'<link rel="preload" as="image" href="([^"]+)" media="[^"]+">', html)
    t = config.PHONE_START_TILES
    expected = {config.TILE_URL.format(z=t["z"], x=x, y=y)
                for x in range(t["x"][0], t["x"][1] + 1) for y in range(t["y"][0], t["y"][1] + 1)}
    assert set(hrefs) == expected and len(hrefs) == 6
    origin = "/".join(config.TILE_URL.split("/")[:3])
    assert f'<link rel="preconnect" href="{origin}">' in html


def test_any_of_places_ship_their_members(tmp_path):
    from pnwtap.geometry import decode_polyline
    from pnwtap.sheet import Member
    locs = _pool()
    locs[3] = Location("Any growing glacier", "glacier", "hard", [(46.2, -122.19), (60.02, -139.5)], None, "b",
                       members=[Member("Crater Glacier", [(46.2, -122.19)], "point"),
                                Member("Hubbard Glacier", [(60.02, -139.5)], "point")])
    _, html = _render(tmp_path, locs)
    payload = json.loads(html.split("window.PNWTAP = ", 1)[1].split(";</script>", 1)[0])
    loc = payload["locations"][3]
    assert loc["kind"] == "any" and loc["geometry"] == ""
    assert [(m["name"], decode_polyline(m["geometry"]), m["kind"]) for m in loc["members"]] == [
        ("Crater Glacier", [[46.2, -122.19]], "point"), ("Hubbard Glacier", [[60.02, -139.5]], "point")]


def test_a_prompt_ships_only_when_set():
    locs = _pool()
    locs[0].prompt = "In 1971 a hijacker jumped from a 727 over here."
    payload = build_payload(locs, {}, {}, config)
    assert payload["locations"][0]["prompt"].startswith("In 1971") and "prompt" not in payload["locations"][1]
