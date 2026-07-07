# pnwtap — Design Spec

**Date:** 2026-07-06
**Status:** Approved, ready for implementation planning

## Summary

`pnwtap` is a daily geography tapping game in the style of [MapTap](https://maptap.gg),
scoped to the Pacific Northwest (Oregon, Washington, British Columbia, Alberta). Each day
presents 5 rounds; in each round the player is shown the *name* of a location and taps where
they think it is on an unlabeled terrain map. They are scored 0–100 per round on how close the
tap was, with harder locations worth more via difficulty multipliers. After 5 rounds the player
gets a final score (max 1000) and a Wordle-style share string to paste into a group chat.

The location set is intentionally regional and eclectic: notable peaks (Vesper, Baker, Sahale,
Assiniboine, Temple…), hikes/traverses (Wapta…), roads (Mountain Loop Highway, I-5 exits),
climbs (FlyBoys…), rivers, and specific points of interest (Fremont Troll, Microsoft Campus,
Stevens Pass ski area…).

It is built for a small group of friends. It is an honor-system game — there is no anti-cheat.

## Goals & non-goals

**Goals**
- A fun, shareable daily game that rewards deep local knowledge of PNW mountains and places.
- Maximize readable Python. All game *logic* (data loading, validation, puzzle selection) lives
  in Python. The browser holds only the unavoidable interactive glue (map rendering, tap
  handling, and a ~15-line scoring function).
- A Google Sheet is the database — easy to edit, no real DBMS.
- Zero ongoing maintenance to keep the game running; rebuild only to add locations.
- Trivially cheap and simple to host (GitHub Pages).

**Non-goals (YAGNI)**
- No live/shared leaderboard, accounts, or backend server. Competition is social, via the share
  string (like Wordle).
- No anti-cheat. Answers are baked into the public site by design.
- No curation UI now (the schedule is auto-generated), but the code is structured so a curation
  override is a clean future drop-in.
- No mobile app; it is a responsive web page.

## Gameplay & scoring

- **Rounds per day:** 5.
- **Distance:** haversine distance from the player's tap to the *nearest point on the location's
  geometry*. For a single-point location (a peak, a POI) this is distance to that point. For a
  linear location (river, road, traverse) it is the distance to the nearest point on the
  connecting polyline (nearest segment), so tapping anywhere along the feature scores well.
- **Round score:** `round(100 * exp(-distance_km / D))`, with `D = 40` km to start. 100 = a
  bullseye; ~78 at 10 km off; ~37 at 40 km off. `D` and all other tunables live in one config
  block.
- **Difficulty tiers & multipliers:** each location is tagged `easy` / `medium` / `hard`. The
  daily set ramps easy→hard with shape **1 easy / 2 medium / 2 hard**, and per-round scores are
  multiplied **×1 / ×1 / ×2 / ×3 / ×3**, giving a max daily score of **1000**. (Ramp shape and
  multipliers are tunable.)
- **Emoji tiers:** each round's difficulty is marked by an emoji in the share string (exact
  glyphs, e.g. 🏅/🔥/🏆, chosen during implementation). The emoji marks *difficulty*, not
  performance.

## Daily puzzle selection

- The Python build script bakes a `date → [location ids]` schedule roughly one year ahead and
  embeds it in the page. The browser looks up today's date — **no server and no daily rebuild**.
- Selection is **deterministic from the date**: a date-seeded shuffle of the location pool, from
  which a valid easy→hard ramp is drawn while avoiding recent repeats until the pool cycles.
  Every player on a given date gets the identical set.
- **Rebuild cadence:** only needed to add new locations (or later, curated days). The pre-baked
  schedule keeps serving fresh daily puzzles with no action.
- **Curation-ready:** structure the selection code so that an optional `curation` tab
  (`date → named locations`) can override the auto pick for specific dates later, without a
  rewrite. Not implemented now.

## The database: Google Sheet

One tab with these columns:

| column | meaning |
|--------|---------|
| `name` | Display name shown to the player (e.g. `Mt Baker`, `Wapta Traverse`). |
| `category` | `peak` / `hike` / `traverse` / `road` / `climb` / `river` / `poi` — drives pin icon/flavor. |
| `difficulty` | `easy` / `medium` / `hard` — drives the ramp and multiplier. |
| `geometry` | One-or-more `lat,lng` points, semicolon-separated. One point = a point feature; several = a line sketch (3–8 points is plenty). |
| `blurb` | Short writeup shown on the reveal (like MapTap's little writeups). |

Example rows:

| name | category | difficulty | geometry | blurb |
|------|----------|-----------|----------|-------|
| Mt Baker | peak | easy | `48.7767,-121.8144` | Glaciated stratovolcano… |
| Wapta Traverse | traverse | hard | `51.68,-116.45; 51.60,-116.40; 51.53,-116.34` | Classic icefield ski traverse… |
| Mountain Loop Hwy | road | medium | `48.09,-121.62; 48.06,-121.47; 47.93,-121.09` | Scenic loop through the Mountain Loop… |

**Access:** the Sheet is exposed via **File → Share → Publish to web → CSV**. The Python build
fetches that CSV URL with no credentials (no service account, no OAuth). Tradeoff: the CSV URL is
publicly readable — harmless here, since every answer is baked into the public site anyway. (A
private sheet via `gspread` + service-account key was rejected as unnecessary auth overhead.)

## The page / UX flow

- **Basemap:** a flat Leaflet map (not a globe — the region is a ~1500 km subregion) using
  **terrain/shaded-relief tiles with place-name labels off**, from a free tile provider. The
  player reads ridgelines, glaciers, and coastline to locate a peak — labels would give the
  answer away. The tile source is swappable.
- **Per round:** show the location `name` (blurb hidden) → player pans/zooms the unlabeled
  terrain map and taps → locks it in → reveal shows the **true geometry, the player's tap, a line
  between them, the round score, and the `blurb`** → Next.
- **After round 5:** final score (out of 1000) and a Wordle-style share string with a copy
  button, e.g. `pnwtap Jul 6 · 95🏅 88🔥 97🔥 95🏆 92🏆 · Final 862`.
- **Replay guard:** `localStorage` records today's completed result so a page refresh shows the
  result rather than letting the player replay (like Wordle).
- **No puzzle for a date** (before the schedule starts / after it ends): show a friendly
  "no puzzle today" message.

## Architecture & data flow

```
Google Sheet (published CSV)
      │  fetched once, at build time
      ▼
build.py  →  parse & validate geometry, build date→puzzle schedule, render page
      │
      ▼
docs/  (index.html with data baked in, + game.js, style.css)
      │  git push
      ▼
GitHub Pages  →  Friend's browser: today's date → 5 rounds → local scoring → share string
```

Python owns all editable logic. The browser owns rendering, taps, and the small scoring
function. The location data and the schedule are baked into the page as JSON at build time.

## Project structure

```
pnwtap/
  build.py                # orchestrates: read sheet → schedule → render docs/
  pnwtap/
    sheet.py              # fetch + parse the published CSV into location records
    geometry.py           # parse geometry strings; haversine; nearest-point-on-path
    schedule.py           # deterministic date-seeded selection + easy→hard ramp
    render.py             # fill the HTML template, write docs/
  templates/
    index.html.jinja      # page template (data injected as JSON)
  static/
    game.js               # Leaflet map, round loop, tap handling, scoring, share string
    style.css
  docs/                   # build output = GitHub Pages source
    index.html
    game.js  style.css
  tests/
    test_geometry.py
    test_schedule.py
  requirements.txt
  README.md               # how to set up the sheet, build, and publish
```

## Error handling

Validation happens at **build time and fails loudly** — better to break the build than ship a
broken day:

- Malformed `geometry` (unparseable coords, wrong field count) → error naming the offending row.
- Coordinates outside a PNW bounding box → error/warning (guards against lat/lng typos and
  swaps).
- A tier lacking enough locations to fill the ramp → error explaining what's missing.
- Missing required columns or empty required fields → error naming the row.

Runtime (browser) failure modes are minimal: if tiles fail to load the map is degraded but the
game still functions; an unavailable date shows the friendly message above.

## Testing

- **pytest** for the Python logic:
  - `test_geometry.py`: geometry-string parsing (points and lines), haversine correctness against
    known distances, nearest-point-on-path for linear features.
  - `test_schedule.py`: determinism (same date → same set), correct ramp shape, no near-term
    repeats, and behavior at pool-cycle boundaries.
- **Manual:** open the built `docs/index.html` locally and play a full round to sanity-check the
  map, taps, reveal, and share string.

## Tunable configuration (single block)

Collected in one place for easy tweaking: `D` (score decay km), rounds per day, ramp shape,
multipliers, PNW bounding box, tile URL/attribution, schedule horizon (days ahead), and emoji
glyphs per tier.

## Deployment

GitHub Pages serving from the `docs/` folder of the author's personal GitHub Pages repo. Workflow
each time: run `python build.py` → `git add docs && git commit && git push`.
