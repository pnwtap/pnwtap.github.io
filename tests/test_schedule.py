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



# ---- same-day variety ----
from pnwtap.geometry import haversine_km


def _grid_pool():
    """Locations on a 1-degree grid (~75-110 km apart), cycling through three categories."""
    locs, n = [], 0
    for diff, count in (("easy", 12), ("medium", 12), ("hard", 24)):
        for k in range(count):
            lat, lng = 45.0 + (n % 8), -124.0 + (n // 8)
            locs.append(Location(f"{diff}{k}", ["peak", "town", "lake"][n % 3], diff, [(lat, lng)], None, ""))
            n += 1
    return locs


def test_days_are_spread_out_when_possible():
    locs = _grid_pool()
    sched = build_schedule(locs, date(2026, 7, 7), 120, RAMP, seed=0, spread_km=70)
    for ids in sched.values():
        pts = [locs[i].geometry[0] for i in ids]
        assert min(haversine_km(a, b) for k, a in enumerate(pts) for b in pts[k + 1:]) >= 70


def test_category_cap_when_possible():
    locs = _grid_pool()
    sched = build_schedule(locs, date(2026, 7, 7), 120, RAMP, seed=0, max_per_category=2)
    from collections import Counter
    for ids in sched.values():
        assert max(Counter(locs[i].category for i in ids).values()) <= 2


def test_variety_rules_relax_instead_of_failing():
    locs = _big_pool()          # everything within a few km: spread can never be met
    sched = build_schedule(locs, date(2026, 7, 7), 60, RAMP, seed=0, spread_km=500, max_per_category=1)
    assert len(sched) == 60
    for ids in sched.values():
        assert len(set(ids)) == len(ids)



def test_a_batch_of_new_locations_is_introduced_one_a_day():
    locs = _big_pool()
    before = build_schedule(locs, date(2026, 7, 7), 60, RAMP, seed=0)
    lock = lock_through(before, locs, date(2026, 8, 31))
    batch = [_loc("medium", 100 + i) for i in range(4)] + [_loc("hard", 100 + i) for i in range(6)]
    grown = locs + batch
    locked, _ = resolve_lock(lock, grown)
    after = _names(grown, build_schedule(grown, date(2026, 7, 7), 120, RAMP, seed=0, locked=locked))
    new = {l.name for l in batch}
    firsts = {}
    for day in sorted(after):
        if day <= "2026-08-31":
            continue
        fresh_today = [n for n in after[day] if n in new and n not in firsts]
        assert len(fresh_today) <= 1                     # never more than one debut a day
        for n in fresh_today:
            firsts[n] = day
    assert set(firsts) == new                            # ...and every one does debut
    assert max(firsts.values()) <= "2026-09-12"          # within about ten days
