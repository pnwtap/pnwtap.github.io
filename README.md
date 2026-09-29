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
- Everything the page needs is served from the site itself: Leaflet 1.9.4 and a subset of Open Sans
  are vendored in `static/` (fonts made with `scripts/subset_fonts.py`), each linked with a content
  hash (`?v=`) so browsers cache them until they actually change. Only the map imagery (Esri) and
  the hit counter come from elsewhere.

## The sheet

One tab, columns: `name, category, difficulty, geometry, image, blurb, facts`.

- `name`: must be unique — it's how played days are remembered (see *Schedule* below).
- `category`: `peak / hike / traverse / road / climb / river / town / poi / lake / glacier / pass /
  island / ski / waterfall / park` (icons and labels live in `CATEGORIES` in `pnwtap/config.py`).
- `difficulty`: `easy / medium / hard`. The day is 1 easy, 1 medium, 2 hard, so keep roughly twice
  as many hard rows as easy or medium ones.
- `geometry`: one or more `lat,lng` points, semicolon-separated. Quote the cell — it contains commas.
  Coordinates are kept to 4 decimals (~10 m).
  - one point = a point (peak, town, crag);
  - several = a line (river, road, traverse) scored by distance to its nearest part;
  - several with the **last point equal to the first** = an area (lake, island, park): a tap
    inside scores 100. Exception: for routes (`traverse / hike / road / river / climb`) a closed
    ring is just a loop — the Timberline Trail scores along the trail, not across Mt Hood.
- `image` (optional): a URL. If set, that round shows the image instead of the name.
- `blurb`: a line or two shown on the reveal.
- `facts` (optional): `key: value | key: value`, e.g. `grade: 5.9 | style: sport | pitches: 18`.
  The reveal shows them as a card laid out for the category (a peak's card leads with elevation
  and prominence, a climb's with grade, style and pitches, a town's with population). Facts that
  say *what* a place is rather than *where* (grade, height, population…) also appear as a short
  clue line on the guess prompt, and `tagline` adds a one-liner there ("Hardest sport route in
  Washington"). Keys, units and which are clues: `FACTS` / `CARDS` in `pnwtap/config.py`,
  documented for editors in `data/FACTS_SPEC.md`. Numbers are metric; the page adds ft/mi.

## Scoring

Each round scores on how far the tap is from the feature — measured to the nearest point of a
line, and 0 anywhere inside an area (towns, lakes, parks, islands):

    score = 100 × (1 − ln(1 + (d / 25 km)²) / ln(1 + (1500 km / 25 km)²))

A near miss costs almost nothing; further out every halving of the miss is worth the same ~16
points, so knowing the right valley, the right region and even the right province all count,
and a 0 takes a miss of 1,500 km:

| miss | 10 km | 25 km | 50 km | 100 km | 200 km | 500 km | 1000 km | 1500 km |
|---|---|---|---|---|---|---|---|---|
| score | 98 | 92 | 80 | 65 | 49 | 27 | 10 | 0 |

Rounds are multiplied ×1 / ×2 / ×3 / ×4 (easy → hard), for a maximum of 1000. Tune with
`SCORE_NEAR_KM` / `SCORE_ZERO_KM` / `SCORE_SHAPE` in `pnwtap/config.py`.

The build fails loudly, naming the row, on: a missing name, a duplicate name, an unknown category
or difficulty, malformed coordinates, a point outside the map's region (usually a lat/lng typo),
or an unknown / non-numeric fact.
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

Enable GitHub Pages on the repo with **Settings → Pages → Source: GitHub Actions**.

`.github/workflows/rebuild.yml` then does the rest, every night (just after midnight Pacific) and on
every push to `main`: it runs the tests, rebuilds from the sheet, commits
`data/schedule_lock.json` (plus `docs/` when the page changed), and deploys `docs/` to Pages —
only when the page differs from the live one, so unchanged nights don't redeploy and returning
players' browsers keep their cached files. So once the sheet URL is set, editing the sheet is all
it takes: new places are live the next morning, or immediately via **Actions → Rebuild site → Run
workflow** (which always deploys).

The site keeps working with no rebuilds for `HORIZON_DAYS` (400) days (the schedule is extended in
100-day steps, so most nightly rebuilds leave `docs/` untouched); rebuild whenever you add locations. Add `?date=YYYY-MM-DD` to the URL to play a past day (future days are refused).

## Playtesting

Open `?playtest` (e.g. `http://localhost:8000/?playtest`) to play any location on demand: pick
from the list or step with ◀ ▶ 🎲, check its prompt clues and fact card, and tick **show all
answers** to overlay every location on the map — the quickest way to spot a bad coordinate.
Nothing is saved in this mode.

## Curated days

`data/curated.csv` pins hand-picked puzzles to dates — `date,round_1,round_2,round_3,round_4`,
by location name, in play order (round 1 is ×1 … round 4 is ×4). Curated days win over the
auto-picker and over the lock, so you can re-curate a day even after it's been played (players'
saves for the old puzzle are ignored, so they get the new one). A day whose difficulties don't
follow the easy/medium/hard/hard ramp is allowed and noted in the build output. Curated days
before `EPOCH` are "practice" puzzles (reachable with `?date=`; they don't get a number and the
"missed yesterday?" link never points at them).

## Schedule

Puzzle #1 is `EPOCH` (2026-09-28, launch day). Each slot draws from the least-recently-used half of its
difficulty tier, seeded by the date — so nothing repeats until at least half its tier has been
played. On top of that:

- **new locations debut one per day** — add one and it shows up tomorrow; add forty and they're
  blended in over the next forty days rather than taking over;
- **days are varied** — places on the same day prefer to be `SPREAD_KM` (80 km) apart, with at most
  `MAX_PER_CATEGORY` (2) of one category. Both are soft rules that relax only when nothing
  eligible satisfies them (on the current data they always hold).

Every build writes the puzzles for **today and earlier** into `data/schedule_lock.json` (by
location name) and honours that lock on the next build. So you can add, remove, or reorder sheet
rows at any time without changing a puzzle someone has already played — only future days move.
**Commit the lock file.** Use `--no-lock` for throwaway experiments and `--today YYYY-MM-DD` to
pretend it's another date.

## Hit counting

Set `GOATCOUNTER` in `pnwtap/config.py` to a [GoatCounter](https://www.goatcounter.com) site
code (currently `pnwtap` → pnwtap.goatcounter.com). The page then counts views (`/`, `/archive`)
and a few events: `/start/<n>`, `/finish/<n>`, `/share/<n>` and `/score/<n>/<band>` (final score
in 50-point bands, per puzzle — enough to draw a score histogram later). No cookies; nothing is
counted in `?playtest` or on localhost. Empty string = no counting.

## Feedback

The results screen ends with two small links, **Suggest a place** and **Report a bug**. They open
the repo's GitHub issue forms (`.github/ISSUE_TEMPLATE/place.yml` and `bug.yml`); the bug form
arrives pre-filled with the puzzle, its four places and the player's browser. To take reports from
people without a GitHub account, point `FEEDBACK_PLACE_URL` / `FEEDBACK_BUG_URL` in
`pnwtap/config.py` at a Google Form (or anything else) instead.

## Tuning

All knobs live in `pnwtap/config.py`: the score curve `SCORE_NEAR_KM` / `SCORE_ZERO_KM`, `RAMP`,
`MULTIPLIERS`, `FACTS` / `CARDS`, `EPOCH`,
`HORIZON_DAYS`, `SEED`, `EMOJI`, `CATEGORIES`, the `BBOX`, `START_BOUNDS` (initial map framing),
`PHONE_START_TILES` (imagery a phone's first view preloads — re-check if you change the framing),
zoom limits, and the tile URLs. The region stencil is `data/region_mask.json`
(regenerate with `scripts/build_region_mask.py`, which needs `shapely`).

## Tests

```bash
.venv/bin/python -m pytest
```
