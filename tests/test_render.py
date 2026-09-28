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
