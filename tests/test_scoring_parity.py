"""The browser scores taps with static/scoring.js; make sure it agrees with pnwtap/geometry.py."""
import json
import random
import shutil
import subprocess
from pathlib import Path

import pytest

from pnwtap import config
from pnwtap.geometry import nearest_point_km, score

SCORING_JS = Path(__file__).resolve().parent.parent / "static" / "scoring.js"


def _cases():
    rng = random.Random(7)
    paths = [
        [(48.7767, -121.8144)],                                        # Mt Baker (point)
        [(48.09, -121.62), (48.06, -121.47), (47.93, -121.09)],        # Mountain Loop Hwy
        [(51.68, -116.45), (51.60, -116.40), (51.53, -116.34)],        # Wapta
        [(60.72, -135.05), (64.06, -139.43)],                          # long northern line
        [(49.9, -119.6), (50.3, -119.4), (49.5, -119.5), (49.9, -119.6)],  # closed ring
    ]
    cases = []
    for path in paths:
        for area in ([False, True] if len(path) >= 4 else [False]):   # ring as a loop route and as an area
            for _ in range(25):
                tap = (rng.uniform(42, 62), rng.uniform(-138, -112))
                cases.append((tap, path, area))
            cases.append((path[0], path, area))                         # bullseye
            cases.append(((49.9, -119.5), path, area))                  # inside the ring
    return cases


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
def test_js_scoring_matches_python():
    cases = _cases()
    script = (
        f"const S = require({json.dumps(str(SCORING_JS))});"
        f"const cases = {json.dumps(cases)};"
        f"console.log(JSON.stringify(cases.map(([t, p, a]) => {{"
        f"  const n = S.nearest(t, p, a);"
        f"  return [n.km, S.score(n.km, {config.SCORE_NEAR_KM}, {config.SCORE_ZERO_KM}, {config.SCORE_SHAPE})]; }})));"
    )
    out = json.loads(subprocess.run(["node", "-e", script], capture_output=True, text=True, check=True).stdout)
    assert len(out) == len(cases)
    for (tap, path, area), (js_km, js_score) in zip(cases, out):
        py_km = nearest_point_km(tap, path, area=area)
        assert js_km == pytest.approx(py_km, rel=1e-9, abs=1e-9)
        assert js_score == score(py_km, config.SCORE_NEAR_KM, config.SCORE_ZERO_KM, config.SCORE_SHAPE)


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
def test_js_decodes_every_path_exactly():
    import csv
    from pnwtap.geometry import decode_polyline, encode_polyline, parse_geometry
    root = Path(__file__).resolve().parent.parent
    rows = csv.DictReader((root / "data" / "locations.csv").open(encoding="utf-8"))
    paths = [[list(p) for p in parse_geometry(r["geometry"])] for r in rows]
    paths += json.loads((root / "data" / "region_mask.json").read_text())
    paths.append([[47.433612, -121.773598], [-0.00005, 179.99995]])   # finer than the page carries
    encoded = [encode_polyline(p) for p in paths]
    script = (
        f"const S = require({json.dumps(str(SCORING_JS))});"
        f"const encoded = JSON.parse(require('fs').readFileSync(0, 'utf8'));"
        f"console.log(JSON.stringify(encoded.map((e) => S.decode(e))));"
    )
    out = subprocess.run(["node", "-e", script], input=json.dumps(encoded),
                         capture_output=True, text=True, check=True).stdout
    assert json.loads(out) == [decode_polyline(e) for e in encoded]   # the browser sees what Python encoded


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
@pytest.mark.parametrize("host_tz", ["America/Los_Angeles", "America/New_York", "Europe/London", "Asia/Tokyo", "UTC"])
def test_puzzle_day_is_pacific_whatever_the_device_zone(host_tz):
    import os
    from datetime import datetime, timedelta
    from zoneinfo import ZoneInfo
    la = ZoneInfo("America/Los_Angeles")
    instants = [datetime(2026, 9, 29, 4, 30, tzinfo=ZoneInfo("Europe/London")),    # 20:30 Sep 28 in LA
                datetime(2026, 9, 28, 23, 59, 59, tzinfo=la), datetime(2026, 9, 29, 0, 0, 1, tzinfo=la),
                datetime(2026, 11, 1, 1, 30, tzinfo=la), datetime(2027, 3, 14, 3, 30, tzinfo=la)]
    days = ["2026-09-28", "2026-09-29", "2026-11-01", "2026-11-02", "2027-03-14", "2027-03-15"]
    script = (
        f"const S = require({json.dumps(str(SCORING_JS))}); const tz = 'America/Los_Angeles';"
        f"console.log(JSON.stringify({{ d: {json.dumps([int(i.timestamp() * 1000) for i in instants])}.map((t) => S.dayIn(t, tz)),"
        f"  s: {json.dumps(days)}.map((d) => S.dayStart(d, tz)) }}));"
    )
    out = json.loads(subprocess.run(["node", "-e", script], capture_output=True, text=True, check=True,
                                    env={**os.environ, "TZ": host_tz}).stdout)
    assert out["d"] == [i.astimezone(la).date().isoformat() for i in instants]
    for day, ms in zip(days, out["s"]):
        start = datetime.fromisoformat(day).replace(tzinfo=la)       # local midnight, DST-aware
        assert ms == int(start.timestamp() * 1000), day
    # the fall-back day (Nov 1) is 25 hours long, spring-forward (Mar 14) 23
    assert out["s"][3] - out["s"][2] == 25 * 3600e3 and out["s"][5] - out["s"][4] == 23 * 3600e3
