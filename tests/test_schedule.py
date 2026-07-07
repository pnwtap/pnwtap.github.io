from datetime import date
import pytest
from pnwtap.sheet import Location
from pnwtap.schedule import build_schedule

RAMP = ["easy", "medium", "hard", "hard"]


def _loc(diff, i):
    return Location(f"{diff}{i}", "peak", diff, [(48.0 + i * 0.01, -121.0)], None, "")


def _pool():
    # 3 easy, 3 medium, 4 hard
    locs = []
    locs += [_loc("easy", i) for i in range(3)]
    locs += [_loc("medium", i) for i in range(3)]
    locs += [_loc("hard", i) for i in range(4)]
    return locs


def test_is_deterministic():
    a = build_schedule(_pool(), date(2026, 7, 7), 30, RAMP, seed=0)
    b = build_schedule(_pool(), date(2026, 7, 7), 30, RAMP, seed=0)
    assert a == b


def test_each_day_matches_ramp_difficulties():
    locs = _pool()
    sched = build_schedule(locs, date(2026, 7, 7), 30, RAMP, seed=0)
    day = sched["2026-07-07"]
    assert [locs[i].difficulty for i in day] == RAMP


def test_no_duplicate_within_a_day():
    sched = build_schedule(_pool(), date(2026, 7, 7), 30, RAMP, seed=0)
    for ids in sched.values():
        assert len(set(ids)) == len(ids)


def test_horizon_length():
    sched = build_schedule(_pool(), date(2026, 7, 7), 30, RAMP, seed=0)
    assert len(sched) == 30
    assert "2026-07-07" in sched


def test_raises_when_tier_too_small():
    locs = [_loc("easy", 0), _loc("medium", 0), _loc("hard", 0)]  # only 1 hard, ramp needs 2
    with pytest.raises(ValueError, match="hard"):
        build_schedule(locs, date(2026, 7, 7), 5, RAMP, seed=0)


def test_no_intra_day_duplicate_with_odd_tier_pool():
    # 3 hard (odd) exercises the reshuffle-boundary duplicate bug
    locs = [_loc("easy", 0), _loc("medium", 0)] + [_loc("hard", i) for i in range(3)]
    sched = build_schedule(locs, date(2026, 7, 7), 400, RAMP, seed=0)
    for ids in sched.values():
        assert len(set(ids)) == len(ids)     # no location repeats within a day
