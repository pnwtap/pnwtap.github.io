"""Deterministic date → puzzle schedule.

Each difficulty tier is drawn from its own reshuffling cycle seeded only by
`seed` + the tier name, then consumed in date order. This gives a stable
schedule (same inputs → same output) with no repeats until a tier's pool
cycles.
"""
import random
import zlib
from collections import Counter
from datetime import date, timedelta


def _tier_cycle(indices: list[int], seed: int, tier: str):
    """Yield indices forever, reshuffling the pool on each full pass."""
    rng = random.Random(zlib.crc32(f"{seed}:{tier}".encode()))
    while True:
        order = list(indices)
        rng.shuffle(order)
        yield from order


def build_schedule(locations, start_date: date, horizon_days: int, ramp: list[str], seed: int = 0) -> dict[str, list[int]]:
    by_tier: dict[str, list[int]] = {"easy": [], "medium": [], "hard": []}
    for idx, loc in enumerate(locations):
        by_tier[loc.difficulty].append(idx)

    need = Counter(ramp)
    for tier, count in need.items():
        if len(by_tier[tier]) < count:
            raise ValueError(
                f"need at least {count} '{tier}' locations for the ramp, have {len(by_tier[tier])}"
            )

    cycles = {tier: _tier_cycle(by_tier[tier], seed, tier) for tier in by_tier}

    schedule: dict[str, list[int]] = {}
    for offset in range(horizon_days):
        day = start_date + timedelta(days=offset)
        schedule[day.isoformat()] = [next(cycles[tier]) for tier in ramp]
    return schedule
