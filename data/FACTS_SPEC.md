# pnwtap facts reference

Each location gets an optional `facts` cell: `key: value | key: value | ...`
(first `:` splits key from value; ` | ` separates pairs; no `|` inside values).

The game shows **clue** facts in a short line on the guess prompt (they must not give away
*where* the place is), and every fact on the reveal card.

## Rules

- Only use keys from the table. Omit anything you can't verify from a real source — no guessing.
- Numeric keys: a plain number in the stated unit, no units, no thousands separators
  (`elevation_m: 4392`, `length_km: 1375`, `area_km2: 344.6`).
- Metric only; the game converts to feet/miles itself. When the source's figure is in feet or
  miles, keep extra precision so the imperial display round-trips to the well-known number:
  metres to one decimal (Rainier 14,410 ft → `elevation_m: 4392.2`), km to two (`length_km: 19.79`).
- Keep strings short (≤ 40 chars; `tagline` ≤ 60).
- Every fact needs a source (Wikipedia, peakbagger, bivouac, Mountain Project, census, official
  park/resort pages). List them per row in your `*_sources.md`.

## Keys

| key | clue? | use for | example |
|---|---|---|---|
| tagline | yes | a genuine superlative / claim to fame only (≈1 row in 8 at most). May name a state/province, never a nearby town, range, park or valley | `Highest peak in the Canadian Rockies` |
| type | yes | short descriptor of what it is | `stratovolcano`, `granite spire`, `cinder cone`, `sport crag`, `glacial lake`, `reservoir`, `concrete gravity dam`, `plunge waterfall`, `ski area`, `urban park`, `fjord` |
| elevation_m | yes | summit / lake surface / pass / town elevation | `4392` |
| prominence_m | no | peaks | `4026` |
| height_m | yes | waterfall total drop, structure height, cliff/wall height | `189` |
| length_km | yes | rivers, roads, traverses, long hikes, lakes (long axis), glaciers | `1375` |
| length_m | yes | a climbing route's length | `790` |
| gain_m | yes | total elevation gain of a hike / route / traverse | `1200` |
| high_point_m | yes | highest point of a road / traverse / hike | `1668` |
| vertical_m | yes | ski area lift-served vertical | `948` |
| lifts | no | ski area lift count | `10` |
| area_km2 | yes | lakes, islands, parks, glaciers (under 1 sq mi the card shows acres; from an acreage keep 4 significant figures: 25.10 ac → `0.1016`) | `344.6` |
| depth_m | no | lake max depth | `594` |
| grade | yes | climbs: YDS `5.14d` / `5.10a`; alpine `III 5.7` or `II, 35° snow`; scrambles `Class 3` | `5.9` |
| style | yes | one of: `sport`, `trad`, `sport & trad`, `alpine rock`, `mountaineering`, `glacier climb`, `scramble`, `ski tour`, `ski mountaineering`, `hike`, `boulder` | `sport` |
| pitches | yes | **multipitch routes only** (omit for single pitch and for crags) | `18` |
| rock | no | rock type | `granite`, `basalt`, `gneiss`, `limestone`, `welded tuff` |
| classic | no | crags / formations / big peaks: the signature route with grade (and pitches if multipitch) | `Grand Wall, 5.11a, 10 pitches` |
| days | yes | typical duration of a traverse / long hike | `2–4` |
| season | no | usual season | `Apr–Jun` |
| population | yes | municipality population with census year | `1,010,899 (2021)` |
| founded | no | founded / incorporated | `1904` |
| range | no | mountain range or subrange | `North Cascades` |
| region | no | broader region | `Methow Valley, WA` |
| first_ascent | no | year + party | `1870, Hazard Stevens & P. B. Van Trump` |
| first_done | no | traverses / routes: first completion | `1938, Ptarmigan Climbing Club` |
| built | no | structures / roads | `1933–42`, `opened 1972` |
| last_eruption | no | volcanoes, only if well established | `2008` |
| source | no | rivers: where it rises | `Fraser Pass, Rockies` |
| mouth | no | rivers: where it ends | `Strait of Georgia` |
| road | no | passes: highway over it | `I-90` |

## Where facts live

In the sheet's `facts` column (or `data/locations.csv`). The build validates every key against
`FACTS` in `pnwtap/config.py` and fails naming the row on an unknown key or a non-numeric number.
The research behind the current facts, with a source for every figure, is in
`data/candidates/facts_*_sources.md`.
