"""Read and validate the location database (a published-CSV Google Sheet)."""
import csv
import io
from dataclasses import dataclass

import requests

from pnwtap.geometry import parse_geometry, within_bbox

DIFFICULTIES = {"easy", "medium", "hard"}


@dataclass
class Location:
    name: str
    category: str
    difficulty: str
    geometry: list[tuple[float, float]]
    image: str | None
    blurb: str


def parse_locations(csv_text: str, bbox) -> list[Location]:
    """Parse CSV text into validated Location records. Raises ValueError naming the offending row."""
    reader = csv.DictReader(io.StringIO(csv_text))
    locations: list[Location] = []
    for line_no, row in enumerate(reader, start=2):  # header is line 1
        name = (row.get("name") or "").strip()
        if not name:
            raise ValueError(f"row {line_no}: missing name")

        difficulty = (row.get("difficulty") or "").strip().lower()
        if difficulty not in DIFFICULTIES:
            raise ValueError(f"row {line_no} ({name}): bad difficulty {difficulty!r}")

        category = (row.get("category") or "").strip().lower() or "poi"

        try:
            geometry = parse_geometry(row.get("geometry") or "")
        except ValueError as exc:
            raise ValueError(f"row {line_no} ({name}): {exc}") from exc
        for pt in geometry:
            if not within_bbox(pt, bbox):
                raise ValueError(f"row {line_no} ({name}): point {pt} outside PNW bbox")

        image = (row.get("image") or "").strip() or None
        blurb = (row.get("blurb") or "").strip()
        locations.append(Location(name, category, difficulty, geometry, image, blurb))
    return locations


def fetch_csv(url: str) -> str:
    """Fetch the published-CSV sheet as text."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text
