"""Deterministic date → puzzle schedule.

Days are filled in date order. For each day and difficulty tier we pick at
random (seeded by the date) from the *least-recently-used half* of that tier's
pool. That gives:

- determinism: same locations + same locks → same schedule;
- spacing: a location can't come back until at least half its tier has been
  played since, and never twice in one day;
- stability: randomness and tie-breaks are keyed on location *names*, not sheet
  row order, and already-played days can be pinned with `locked` so adding or
  reordering sheet rows never rewrites a puzzle someone has already seen;
- freshness: never-used locations are drawn first, so the first pass through
  a tier is a permutation and newly added locations appear right away.
"""
import random
import zlib
from collections import Counter
from datetime import date, timedelta

NEVER = -10**9


def _key(*parts) -> int:
    return zlib.crc32(":".join(str(p) for p in parts).encode())


def build_schedule(
    locations,
    start_date: date,
    horizon_days: int,
    ramp: list[str],
    seed: int = 0,
    locked: dict[str, list[int]] | None = None,
) -> dict[str, list[int]]:
    """Map each ISO date in [start_date, start_date + horizon_days) to location indices, one per ramp slot."""
    locked = locked or {}
    by_tier: dict[str, list[int]] = {"easy": [], "medium": [], "hard": []}
    for idx, loc in enumerate(locations):
        by_tier[loc.difficulty].append(idx)

    need = Counter(ramp)
    for tier, count in need.items():
        if len(by_tier[tier]) < count:
            raise ValueError(
                f"need at least {count} '{tier}' locations for the ramp, have {len(by_tier[tier])}"
            )

    last_used: dict[int, int] = {}
    schedule: dict[str, list[int]] = {}
    for offset in range(horizon_days):
        day = (start_date + timedelta(days=offset)).isoformat()
        if day in locked:
            ids = list(locked[day])
        else:
            picks = {}
            for tier, count in need.items():
                pool = sorted(
                    by_tier[tier],
                    key=lambda i: (last_used.get(i, NEVER), _key(seed, locations[i].name)),
                )
                rng = random.Random(_key(seed, day, tier))
                fresh = [i for i in pool if i not in last_used]
                if len(fresh) >= count:
                    chosen = rng.sample(fresh, count)
                else:
                    stale = pool[len(fresh):]
                    eligible = stale[: max(count - len(fresh), len(pool) // 2)]
                    chosen = fresh + rng.sample(eligible, count - len(fresh))
                    rng.shuffle(chosen)
                picks[tier] = iter(chosen)
            ids = [next(picks[tier]) for tier in ramp]
        for i in ids:
            last_used[i] = offset
        schedule[day] = ids
    return schedule


def resolve_lock(lock: dict[str, list[str]], locations) -> tuple[dict[str, list[int]], list[str]]:
    """Turn a {date: [names]} lock into {date: [indices]}; return dates whose names no longer all exist."""
    index = {loc.name: i for i, loc in enumerate(locations)}
    resolved, dropped = {}, []
    for day, names in lock.items():
        if all(n in index for n in names):
            resolved[day] = [index[n] for n in names]
        else:
            dropped.append(day)
    return resolved, sorted(dropped)


def lock_through(schedule: dict[str, list[int]], locations, through: date) -> dict[str, list[str]]:
    """The {date: [names]} lock for every scheduled day on or before `through`."""
    cutoff = through.isoformat()
    return {
        day: [locations[i].name for i in ids]
        for day, ids in schedule.items()
        if day <= cutoff
    }
