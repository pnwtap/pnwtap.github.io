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
- freshness: a never-used location is drawn first, one per day — so a new
  addition appears within days, and a big batch of additions is blended in
  over the following weeks instead of taking over; the very first pass through
  a tier (everything new) is still a permutation;
- variety: within the eligible set, a day prefers places at least `spread_km`
  apart and no more than `max_per_category` of one category, and — strongest of
  all — places at least `recent_km` from anything played in the previous
  `recent_days` days, so a cluster of neighbours (say, four lakes in one basin)
  is spread across weeks rather than served back to back. These are soft — if
  nothing eligible satisfies them they're dropped, never the rules above.
"""
import csv
import io
import random
import zlib
from collections import Counter
from datetime import date, timedelta

from pnwtap.geometry import haversine_km

NEVER = -10**9


def _key(*parts) -> int:
    return zlib.crc32(":".join(str(p) for p in parts).encode())


def _centroids(loc) -> list[tuple[float, float]]:
    """Where a place is, for the variety rules: one point, or one per member of an "any of" place."""
    parts = [m.geometry for m in loc.members] if getattr(loc, "members", None) else [loc.geometry]
    return [(sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)) for pts in parts]


def build_schedule(
    locations,
    start_date: date,
    horizon_days: int,
    ramp: list[str],
    seed: int = 0,
    locked: dict[str, list[int]] | None = None,
    spread_km: float = 0.0,
    max_per_category: int | None = None,
    recent_days: int = 0,
    recent_km: float = 0.0,
) -> dict[str, list[int]]:
    """Map each ISO date in [start_date, start_date + horizon_days) to location indices, one per ramp slot."""
    locked = locked or {}
    centroids = [_centroids(loc) for loc in locations]

    def gap(a: int, b: int) -> float:
        """How far apart two places are (an "any of" place is as close as its nearest member)."""
        return min(haversine_km(p, q) for p in centroids[a] for q in centroids[b])

    def far(c: int, today: list[int]) -> bool:
        return all(gap(c, t) >= spread_km for t in today)

    def cat_ok(c: int, today: list[int]) -> bool:
        if max_per_category is None:
            return True
        return sum(locations[t].category == locations[c].category for t in today) < max_per_category

    def away(c: int, recent: list[int]) -> bool:
        return all(gap(c, r) >= recent_km for r in recent)

    def pick(options: list[list[int]], today: list[int], recent: list[int], rng: random.Random) -> int:
        """Choose from the first candidate set that keeps today (and the last few days) varied;
        else relax the soft rules, the cross-day one first."""
        rules = [lambda c: far(c, today) and cat_ok(c, today) and away(c, recent),
                 lambda c: far(c, today) and cat_ok(c, today)]
        for rule in rules:
            for cands in options:
                good = [c for c in cands if rule(c)]
                if good:
                    return rng.choice(good)
        widest = options[-1]
        spread = [c for c in widest if far(c, today)]
        return rng.choice(spread or widest)

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
    history: list[list[int]] = []
    for offset in range(horizon_days):
        day = (start_date + timedelta(days=offset)).isoformat()
        recent = [i for ids in history[-recent_days:] for i in ids] if recent_days and recent_km else []
        if day in locked:
            ids = list(locked[day])
        else:
            ids = []
            for slot, tier in enumerate(ramp):
                pool = sorted(
                    (i for i in by_tier[tier] if i not in ids),
                    key=lambda i: (last_used.get(i, NEVER), _key(seed, locations[i].name)),
                )
                # Candidates come from the least-recently-used half of the tier (never-used
                # ones sort first). One never-used place a day gets priority; once today has
                # one, prefer played ones — unless never-used places fill the whole half.
                fresh = [i for i in pool if i not in last_used]
                stale_half = pool[: max(1, len(by_tier[tier]) // 2)]
                old = [i for i in stale_half if i in last_used]
                new_today = any(t not in last_used for t in ids)
                if fresh and not new_today:
                    options = [fresh, stale_half]
                elif fresh and old:
                    options = [old, stale_half]
                else:
                    options = [stale_half]
                ids.append(pick(options, ids, recent, random.Random(_key(seed, day, slot))))
        for i in ids:
            last_used[i] = offset
        schedule[day] = ids
        history.append(ids)
    return schedule


def parse_curated(csv_text: str, locations, ramp: list[str]) -> tuple[dict[str, list[int]], list[str]]:
    """Read hand-picked days (`date,round_1,...,round_N` by location name) into {date: [indices]}.

    Raises ValueError on a bad date, an unknown or repeated name, or the wrong number of
    rounds. A day whose difficulties don't follow the ramp is allowed — curation is a
    deliberate choice — but comes back as a warning.
    """
    index = {loc.name: i for i, loc in enumerate(locations)}
    curated: dict[str, list[int]] = {}
    warnings: list[str] = []
    for line_no, row in enumerate(csv.reader(io.StringIO(csv_text)), start=1):
        cells = [c.strip() for c in row]
        if not any(cells) or cells[0] == "date":
            continue
        day, names = cells[0], [c for c in cells[1:] if c]
        try:
            date.fromisoformat(day)
        except ValueError:
            raise ValueError(f"curated line {line_no}: bad date {day!r}") from None
        if day in curated:
            raise ValueError(f"curated line {line_no}: {day} listed twice")
        if len(names) != len(ramp):
            raise ValueError(f"curated {day}: {len(names)} rounds, the game has {len(ramp)}")
        missing = [n for n in names if n not in index]
        if missing:
            raise ValueError(f"curated {day}: unknown location(s) {', '.join(map(repr, missing))}")
        if len(set(names)) != len(names):
            raise ValueError(f"curated {day}: a location appears twice")
        ids = [index[n] for n in names]
        tiers = [locations[i].difficulty for i in ids]
        if tiers != list(ramp):
            warnings.append(f"curated {day}: difficulties {'/'.join(tiers)} (the ramp is {'/'.join(ramp)})")
        curated[day] = ids
    return curated, warnings


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
