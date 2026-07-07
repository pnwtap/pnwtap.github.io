# pnwtap

A daily Pacific-Northwest map-tapping game (a MapTap clone) for a small group of friends.
Each day gives 4 rounds: you're shown a place (or a photo of one) and tap where it is on an
unlabeled terrain map. Closer taps score more; harder places are worth more. Share your result
Wordle-style.

## How it works

- The location database is a **Google Sheet**, published as CSV.
- `build.py` (Python) reads the sheet, validates it, downloads any prompt images locally,
  computes a deterministic ~1-year `date → puzzle` schedule, and renders a self-contained static
  site into `docs/`.
- `docs/` is served by **GitHub Pages**. The browser only renders the map, handles taps, and
  scores them.

## The sheet

One tab, columns: `name, category, difficulty, geometry, image, blurb`.

- `category`: `peak / hike / traverse / road / climb / river / town / poi`
- `difficulty`: `easy / medium / hard`
- `geometry`: one or more `lat,lng` points, semicolon-separated (one = a point; several = a line).
  Quote the cell if your editor needs it — it contains commas.
- `image` (optional): a URL. If set, that round shows the image instead of the name.

Publish it via **File → Share → Publish to web → entire document as CSV**, then paste the CSV URL
into `SHEET_CSV_URL` in `pnwtap/config.py`.

## Build & publish

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# build from the live sheet:
.venv/bin/python build.py
# ...or from the bundled sample data, no sheet needed:
.venv/bin/python build.py --csv data/sample_locations.csv

# preview locally:
.venv/bin/python -m http.server -d docs 8000    # then open http://localhost:8000/

# publish:
git add docs && git commit -m "Rebuild" && git push
```

Enable GitHub Pages on the repo with **Settings → Pages → Source: Deploy from branch → /docs**.

## Tuning

All knobs live in `pnwtap/config.py`: score decay `D_KM`, `RAMP`, `MULTIPLIERS`, `HORIZON_DAYS`,
`SEED`, `EMOJI`, the PNW `BBOX`, map `CENTER`/`DEFAULT_ZOOM`, and the tile URL.

## Tests

```bash
python -m pytest
```
