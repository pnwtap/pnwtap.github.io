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
    assert payload["config"]["D_km"] == config.D_KM
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
