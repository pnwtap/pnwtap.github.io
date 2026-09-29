"""Location facts: parse the sheet's `facts` cell and render the prompt clues and reveal card.

A `facts` cell looks like ``elevation_m: 4392 | prominence_m: 4026 | range: Cascade Range``.
Keys, labels, units and which facts count as clues live in ``config.FACTS``; each
category's card order lives in ``config.CARDS``.
"""
import re

M_TO_FT = 3.28084
KM_TO_MI = 0.621371
KM2_TO_MI2 = 0.386102
KM2_TO_ACRES = 247.105
NUMERIC = {"m", "km", "km2", "int"}


def parse_facts(cell: str, registry: dict | None = None) -> dict[str, str]:
    """Parse "key: value | key: value" into an ordered dict. Raises ValueError on a bad pair,
    a duplicate or (given a registry) an unknown key or a non-numeric number."""
    facts: dict[str, str] = {}
    for chunk in (cell or "").split("|"):
        chunk = chunk.strip()
        if not chunk:
            continue
        key, sep, value = chunk.partition(":")
        key, value = key.strip(), value.strip()
        if not sep or not key or not value:
            raise ValueError(f"bad fact {chunk!r} (want 'key: value')")
        if key in facts:
            raise ValueError(f"fact {key!r} given twice")
        if registry is not None:
            if key not in registry:
                raise ValueError(f"unknown fact {key!r} (allowed: {', '.join(registry)})")
            if registry[key][1] in NUMERIC:
                try:
                    float(value.replace(",", ""))
                except ValueError:
                    raise ValueError(f"fact {key!r} should be a number, got {value!r}") from None
        facts[key] = value
    return facts


def _num(value: str) -> float:
    return float(value.replace(",", ""))


def _fmt(x: float) -> str:
    """Thousands separators; one decimal below 10, whole numbers above."""
    return f"{x:,.1f}".replace(".0", "") if abs(x) < 10 else f"{round(x):,}"


def _fmt_area(km2: float) -> str:
    """km²: as _fmt, but two significant figures below 1 km² (a tarn isn't '0 km²')."""
    return _fmt(km2) if km2 >= 1 else f"{km2:.2g}"


def full_value(kind: str, value: str) -> str:
    """The reveal-card value: metric with imperial alongside."""
    if kind == "m":
        return f"{_fmt(_num(value))} m ({_fmt(_num(value) * M_TO_FT)} ft)"
    if kind == "km":
        return f"{_fmt(_num(value))} km ({_fmt(_num(value) * KM_TO_MI)} mi)"
    if kind == "km2":
        km2 = _num(value)
        mi2 = km2 * KM2_TO_MI2   # small areas (most lakes) read better in acres
        imperial = f"{_fmt(mi2)} sq mi" if mi2 >= 1 else f"{_fmt(km2 * KM2_TO_ACRES)} acres"
        return f"{_fmt_area(km2)} km² ({imperial})"
    if kind == "int":
        return f"{round(_num(value)):,}"
    return value


def clue_text(key: str, value: str, category: str) -> str:
    """The short form used in the prompt's clue line."""
    if key == "pitches":
        n = round(_num(value))
        return f"{n} pitch" if n == 1 else f"{n} pitches"
    if key == "population":
        return "pop. " + re.sub(r"\s*\(.*\)\s*$", "", value)
    if key == "days":
        return f"{value} days"
    if key == "area_km2":
        return f"{_fmt_area(_num(value))} km²"
    if key == "length_km":
        return f"{_fmt(_num(value))} km"
    m = _fmt(_num(value)) + " m" if key.endswith("_m") else None
    if key == "elevation_m":
        return m if category in ("peak", "pass") else f"elev. {m}"
    if key == "height_m":
        return f"{m} drop" if category == "waterfall" else f"{m} tall"
    if key == "length_m":
        return f"{m} long"
    if key == "gain_m":
        return f"{m} gain"
    if key == "high_point_m":
        return f"tops out at {m}"
    if key == "vertical_m":
        return f"{m} vertical"
    return value


def card(facts: dict[str, str], category: str, registry: dict, cards: dict, max_clues: int = 3) -> dict:
    """{tagline, clues, rows} for the page: rows are [label, value] in the category's card order."""
    order = [k for k in cards.get(category, []) if k in facts]
    order += [k for k in registry if k in facts and k not in order]
    rows, clues = [], []
    for key in order:
        if key == "tagline":
            continue
        label, kind, is_clue = registry[key]
        rows.append([label, full_value(kind, facts[key])])
        if is_clue and len(clues) < max_clues:
            clues.append(clue_text(key, facts[key], category))
    return {"tagline": facts.get("tagline"), "clues": clues, "rows": rows}
