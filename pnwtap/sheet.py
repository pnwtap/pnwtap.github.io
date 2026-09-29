"""Read and validate the location database (a published-CSV Google Sheet)."""
import csv
import io
from dataclasses import dataclass, field

import requests

from pnwtap.facts import parse_facts
from pnwtap.geometry import in_region, is_closed, parse_geometry, within_bbox

DIFFICULTIES = {"easy", "medium", "hard"}
# Routes stay lines even when they loop back to the start (Timberline Trail, Magic S Loop);
# a closed ring in any other category (lake, island, park...) is an area.
ROUTE_CATEGORIES = {"traverse", "hike", "road", "river", "climb"}


def shape_kind(geometry, category: str) -> str:
    """"point", "line" or "area": how a geometry is scored and drawn."""
    if len(geometry) == 1:
        return "point"
    if is_closed(geometry) and category not in ROUTE_CATEGORIES:
        return "area"
    return "line"


@dataclass
class Member:
    """One target of an "any of" place (any growing glacier...): a tap scores by the nearest."""
    name: str
    geometry: list[tuple[float, float]]
    kind: str


@dataclass
class Location:
    name: str
    category: str
    difficulty: str
    geometry: list[tuple[float, float]]    # for an "any of" place: every member's points
    image: str | None
    blurb: str
    facts: dict[str, str] = field(default_factory=dict)
    members: list[Member] = field(default_factory=list)

    @property
    def kind(self) -> str:
        """"point", "line", "area", or "any" (several targets) — how it is scored and drawn."""
        return "any" if self.members else shape_kind(self.geometry, self.category)


def _coords(text: str) -> list[tuple[float, float]]:
    # 4 decimals (~10 m) is what the page ships (an encoded polyline at 1e4)
    return [(round(lat, 4), round(lng, 4)) for lat, lng in parse_geometry(text)]


def parse_members(text: str, category: str) -> list[Member]:
    """The members of an "any of" geometry cell: "Name: lat,lng; ... | Name: lat,lng; ...".
    A cell without "|" is an ordinary single place and has no members."""
    parts = [p.strip() for p in text.split("|")]
    if len(parts) < 2:
        return []
    members = []
    for k, part in enumerate(parts, start=1):
        label, sep, coords = part.partition(":")
        if not sep or not label.strip():
            raise ValueError(f"member {k} needs a name, as 'Name: lat,lng; ...'")
        points = _coords(coords)
        members.append(Member(label.strip(), points, shape_kind(points, category)))
    names = [m.name for m in members]
    if len(set(names)) != len(names):
        raise ValueError("two members share a name")
    return members


def parse_locations(csv_text: str, bbox, categories=None, region=None, facts_registry=None) -> list[Location]:
    """Parse CSV text into validated Location records. Raises ValueError naming the offending row.

    `categories`, if given, is the set of allowed category values; `region`, if given, is
    the list of mask rings every point must fall inside (so it's visible on the map);
    `facts_registry` (config.FACTS), if given, is used to validate the optional facts column.
    """
    reader = csv.DictReader(io.StringIO(csv_text))
    locations: list[Location] = []
    seen: dict[str, int] = {}
    for line_no, row in enumerate(reader, start=2):  # header is line 1
        name = (row.get("name") or "").strip()
        if not name:
            if not any((v or "").strip() for v in row.values() if isinstance(v, str)):
                continue  # skip fully blank rows (common at the bottom of a sheet)
            raise ValueError(f"row {line_no}: missing name")
        if name in seen:
            raise ValueError(f"row {line_no} ({name}): duplicate name (also row {seen[name]})")
        seen[name] = line_no

        difficulty = (row.get("difficulty") or "").strip().lower()
        if difficulty not in DIFFICULTIES:
            raise ValueError(f"row {line_no} ({name}): bad difficulty {difficulty!r}")

        category = (row.get("category") or "").strip().lower() or "poi"
        if categories is not None and category not in categories:
            raise ValueError(
                f"row {line_no} ({name}): bad category {category!r} (allowed: {', '.join(sorted(categories))})"
            )

        try:
            cell = row.get("geometry") or ""
            members = parse_members(cell, category)
            geometry = [pt for m in members for pt in m.geometry] if members else _coords(cell)
        except ValueError as exc:
            raise ValueError(f"row {line_no} ({name}): {exc}") from exc
        for pt in geometry:
            if not within_bbox(pt, bbox):
                raise ValueError(f"row {line_no} ({name}): point {pt} outside PNW bbox")
            if region and not in_region(pt, region):
                raise ValueError(f"row {line_no} ({name}): point {pt} outside the map region (lat/lng typo?)")

        image = (row.get("image") or "").strip() or None
        if members and image:
            raise ValueError(f"row {line_no} ({name}): an 'any of' place can't have an image (a photo shows one place)")
        blurb = (row.get("blurb") or "").strip()
        try:
            facts = parse_facts(row.get("facts") or "", facts_registry)
        except ValueError as exc:
            raise ValueError(f"row {line_no} ({name}): {exc}") from exc
        locations.append(Location(name, category, difficulty, geometry, image, blurb, facts, members))
    return locations


def fetch_csv(url: str) -> str:
    """Fetch the published-CSV sheet as text."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text
