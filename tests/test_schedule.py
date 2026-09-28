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


# ---- stability & spacing ----
from pnwtap.schedule import resolve_lock, lock_through


def _names(locs, sched):
    return {d: [locs[i].name for i in ids] for d, ids in sched.items()}


def _big_pool(n_easy=8, n_medium=10, n_hard=20):
    return ([_loc("easy", i) for i in range(n_easy)]
            + [_loc("medium", i) for i in range(n_medium)]
            + [_loc("hard", i) for i in range(n_hard)])


def test_row_order_does_not_change_schedule():
    locs = _big_pool()
    shuffled = list(reversed(locs))
    a = _names(locs, build_schedule(locs, date(2026, 7, 7), 60, RAMP, seed=0))
    b = _names(shuffled, build_schedule(shuffled, date(2026, 7, 7), 60, RAMP, seed=0))
    assert a == b


def test_locked_days_survive_adding_locations():
    locs = _big_pool()
    before = build_schedule(locs, date(2026, 7, 7), 60, RAMP, seed=0)
    lock = lock_through(before, locs, date(2026, 7, 20))
    assert len(lock) == 14

    grown = locs + [_loc("hard", 100 + i) for i in range(5)] + [_loc("easy", 100)]
    locked, dropped = resolve_lock(lock, grown)
    assert dropped == []
    after = build_schedule(grown, date(2026, 7, 7), 60, RAMP, seed=0, locked=locked)
    assert {d: n for d, n in _names(grown, after).items() if d <= "2026-07-20"} == lock


def test_new_locations_surface_soon():
    locs = _big_pool()
    before = build_schedule(locs, date(2026, 7, 7), 60, RAMP, seed=0)
    lock = lock_through(before, locs, date(2026, 8, 31))
    grown = locs + [_loc("hard", 100)]
    locked, _ = resolve_lock(lock, grown)
    after = _names(grown, build_schedule(grown, date(2026, 7, 7), 90, RAMP, seed=0, locked=locked))
    first = min(d for d, names in after.items() if "hard100" in names)
    assert first == "2026-09-01"          # unseen locations go first


def test_spacing_within_tier():
    locs = _big_pool()
    sched = build_schedule(locs, date(2026, 7, 7), 200, RAMP, seed=0)
    days = sorted(sched)
    last = {}
    for n, d in enumerate(days):
        for i in sched[d]:
            if i in last:
                tier_size = sum(1 for l in locs if l.difficulty == locs[i].difficulty)
                per_day = RAMP.count(locs[i].difficulty)
                assert n - last[i] >= (tier_size // 2) // per_day
            last[i] = n


def test_every_location_gets_used():
    locs = _big_pool()
    sched = build_schedule(locs, date(2026, 7, 7), 60, RAMP, seed=0)
    used = {i for ids in sched.values() for i in ids}
    assert used == set(range(len(locs)))


def test_resolve_lock_reports_missing_names():
    locs = _big_pool()
    locked, dropped = resolve_lock({"2026-07-07": ["easy0", "gone", "hard0", "hard1"]}, locs)
    assert locked == {}
    assert dropped == ["2026-07-07"]
