"""Read and validate the location database (a published-CSV Google Sheet)."""
import csv
import io
from dataclasses import dataclass

import requests

from pnwtap.geometry import in_region, is_closed, parse_geometry, within_bbox

DIFFICULTIES = {"easy", "medium", "hard"}
# Routes stay lines even when they loop back to the start (Timberline Trail, Magic S Loop);
# a closed ring in any other category (lake, island, park...) is an area.
ROUTE_CATEGORIES = {"traverse", "hike", "road", "river", "climb"}


@dataclass
class Location:
    name: str
    category: str
    difficulty: str
    geometry: list[tuple[float, float]]
    image: str | None
    blurb: str

    @property
    def kind(self) -> str:
        """"point", "line", or "area" — how the location is scored and drawn."""
        if len(self.geometry) == 1:
            return "point"
        if is_closed(self.geometry) and self.category not in ROUTE_CATEGORIES:
            return "area"
        return "line"


def parse_locations(csv_text: str, bbox, categories=None, region=None) -> list[Location]:
    """Parse CSV text into validated Location records. Raises ValueError naming the offending row.

    `categories`, if given, is the set of allowed category values; `region`, if given, is
    the list of mask rings every point must fall inside (so it's visible on the map).
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
            geometry = parse_geometry(row.get("geometry") or "")
        except ValueError as exc:
            raise ValueError(f"row {line_no} ({name}): {exc}") from exc
        for pt in geometry:
            if not within_bbox(pt, bbox):
                raise ValueError(f"row {line_no} ({name}): point {pt} outside PNW bbox")
            if region and not in_region(pt, region):
                raise ValueError(f"row {line_no} ({name}): point {pt} outside the map region (lat/lng typo?)")

        image = (row.get("image") or "").strip() or None
        blurb = (row.get("blurb") or "").strip()
        locations.append(Location(name, category, difficulty, geometry, image, blurb))
    return locations


def fetch_csv(url: str) -> str:
    """Fetch the published-CSV sheet as text."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text
