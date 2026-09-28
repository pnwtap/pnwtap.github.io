# pnwtap

A daily Pacific-Northwest map-tapping game (a MapTap clone) for a small group of friends.
Each day gives 4 rounds: you're shown a place (or a photo of one) and tap where it is on an
unlabeled satellite map of WA / OR / BC / AB / YT. Closer taps score more; later rounds are harder
and worth more. Share your result Wordle-style.

## How it works

- The location database is a **Google Sheet** published as CSV, or `data/locations.csv` if no sheet
  URL is configured.
- `build.py` reads it, validates every row, downloads any prompt images locally, builds the
  `date → puzzle` schedule, and renders a self-contained static site into `docs/`.
- `docs/` is served by **GitHub Pages**. The browser only renders the map, handles taps, and scores
  them (`static/scoring.js`, a mirror of `pnwtap/geometry.py` — a test keeps them in sync).

## The sheet

One tab, columns: `name, category, difficulty, geometry, image, blurb`.

- `name`: must be unique — it's how played days are remembered (see *Schedule* below).
- `category`: `peak / hike / traverse / road / climb / river / town / poi / lake / glacier / pass / island`
  (the list and icons live in `CATEGORIES` in `pnwtap/config.py`).
- `difficulty`: `easy / medium / hard`. The day is 1 easy, 1 medium, 2 hard, so keep roughly twice
  as many hard rows as easy or medium ones.
- `geometry`: one or more `lat,lng` points, semicolon-separated (one = a point; several = a line
  that you score against anywhere along). Quote the cell — it contains commas.
- `image` (optional): a URL. If set, that round shows the image instead of the name.
- `blurb`: a line or two shown on the reveal.

The build fails loudly, naming the row, on: a missing name, a duplicate name, an unknown category
or difficulty, malformed coordinates, or a point outside the map's region (usually a lat/lng typo).
Blank rows are ignored.

Publish the sheet via **File → Share → Publish to web → entire document as CSV**, then paste the
URL into `SHEET_CSV_URL` in `pnwtap/config.py`. `data/locations.csv` is a ready-made starting set
(every coordinate checked against Wikipedia / OSM / Mountain Project) you can paste into the sheet.

## Build & publish

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

.venv/bin/python build.py                       # sheet if configured, else data/locations.csv
.venv/bin/python -m http.server -d docs 8000    # preview at http://localhost:8000/

git add docs data/schedule_lock.json && git commit -m "Rebuild" && git push
```

Enable GitHub Pages on the repo with **Settings → Pages → Source: Deploy from branch → /docs**.

The site keeps working with no rebuilds for `HORIZON_DAYS` (400) days; rebuild whenever you add
locations. Add `?date=YYYY-MM-DD` to the URL to play a past day (future days are refused).

## Schedule

Puzzle #1 is `EPOCH` (2026-07-07). Each day draws, per difficulty tier, from the least-recently-used
half of that tier, seeded by the date — so nothing repeats until at least half its tier has been
played, and newly added locations are used first.

Every build writes the puzzles for **today and earlier** into `data/schedule_lock.json` (by
location name) and honours that lock on the next build. So you can add, remove, or reorder sheet
rows at any time without changing a puzzle someone has already played — only future days move.
**Commit the lock file.** Use `--no-lock` for throwaway experiments and `--today YYYY-MM-DD` to
pretend it's another date.

## Tuning

All knobs live in `pnwtap/config.py`: score decay `D_KM`, `RAMP`, `MULTIPLIERS`, `EPOCH`,
`HORIZON_DAYS`, `SEED`, `EMOJI`, `CATEGORIES`, the `BBOX`, `START_BOUNDS` (initial map framing),
zoom limits, and the tile URLs. The region stencil is `data/region_mask.json`
(regenerate with `scripts/build_region_mask.py`, which needs `shapely`).

## Tests

```bash
.venv/bin/python -m pytest
```
