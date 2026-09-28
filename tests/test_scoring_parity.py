"""The browser scores taps with static/scoring.js; make sure it agrees with pnwtap/geometry.py."""
import json
import math
import random
import shutil
import subprocess
from pathlib import Path

import pytest

from pnwtap import config
from pnwtap.geometry import nearest_point_km

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
        f"  const n = S.nearest(t, p, a); return [n.km, S.score(n.km, {config.D_KM})]; }})));"
    )
    out = json.loads(subprocess.run(["node", "-e", script], capture_output=True, text=True, check=True).stdout)
    assert len(out) == len(cases)
    for (tap, path, area), (js_km, js_score) in zip(cases, out):
        py_km = nearest_point_km(tap, path, area=area)
        assert js_km == pytest.approx(py_km, rel=1e-9, abs=1e-9)
        assert js_score == round(100 * math.exp(-py_km / config.D_KM))
