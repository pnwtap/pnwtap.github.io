# OSM footprints — towns and extended features

Candidate geometries in `data/candidates/osm_footprints.csv` (`name,geometry`) for 53 rows of
`data/locations.csv`. That is 42 of the 45 towns (Mazama, Bella Coola and Waterton skipped: no usable boundary),
plus Hoh Rainforest and Three Sisters as **lines**, and Goat Rocks, Discovery Park, Painted Hills and all six ski
areas as closed rings. Names match the CSV exactly. Nothing else in the project was edited.

**Source.** OpenStreetMap via the Overpass API: overpass-api.de, with the kumi and maps.mail.ru mirrors as
fallbacks when it returned 504. OSM data timestamps are 2026-09-28. © OpenStreetMap contributors, ODbL.

**Method.**
- **Towns.** Boundaries were found with Overpass `is_in` at each current point, which lists every boundary
  containing it:
  - US: the incorporated place (`boundary=administrative`, admin_level 8). For Fall City and Marblemount,
    which are unincorporated, the census-designated place (`boundary=census`).
  - BC: the municipality (admin_level 8).
  - Alberta and Yukon: the town or city (admin_level 6).
  - Jasper is the exception; see its section.
- **Ring.** The outer ring of the polygon containing the current point, built from the relation's `outer`
  members. Holes and enclaves (`inner` members) are filled, and detached pieces dropped; both are listed per
  town.
- **Simplification.** Douglas–Peucker in a local km projection, run on the ring as two open halves so the
  tolerance holds all the way round:
  - Towns: 0.2 km, stepped up (max 0.5) only to stay at or under 120 points. The tiniest towns step down so
    they keep at least ~8 points.
  - Goat Rocks: 0.5 km.
  - Parks and ski areas: 0.1–0.15 km.
  - Coordinates rounded to 4 dp, first point == last.
- **Validity.** Every rounded ring is a valid simple polygon (shapely `.is_valid`). Where plain DP pinched a
  spot after rounding, GEOS's topology-preserving simplifier was used (or the tolerance nudged by 0.05 km).
- **Lines.** Open polylines (first ≠ last), so the game keeps them as lines.
- **Validation.** A scratch copy of `locations.csv` with all 53 geometries swapped in passes
  `pnwtap.sheet.parse_locations` with bbox, region mask and categories. Kinds come out as expected: 51 `area`,
  2 `line`.

**Flag rule (towns).** Flagged if the boundary reaches more than 8 km from the current point and has fewer
than 400 people/km² (OSM population), or if it is over 1,000 km² (none are). Such a boundary takes in a lot of
land far from the settlement. Flagged towns are still included, as asked. Calgary, Edmonton and Portland are
large but dense, so they are not flagged.

## Towns

| Town | OSM boundary | pts raw → out | DP tol | area km² | pop / density | current point | flag |
|---|---|---|---|---|---|---|---|
| Astoria | [r186203](https://www.openstreetmap.org/relation/186203) Astoria (`administrative 8 city`) | 109 → 21 | 0.2 km | 26.2 | 9,477 / 361 | inside (1.2 km from edge) | includes part of the Columbia estuary |
| Banff | [r8452792](https://www.openstreetmap.org/relation/8452792) Banff (`administrative 6`) | 184 → 18 | 0.2 km | 4.9 | 7,847 / 1,605 | inside (0.26 km from edge) |  |
| Bellingham | [r237440](https://www.openstreetmap.org/relation/237440) Bellingham (`administrative 8 city`) | 381 → 46 | 0.2 km | 78.9 | 91,482 / 1,160 | inside (1.06 km from edge) |  |
| Bend | [r186761](https://www.openstreetmap.org/relation/186761) Bend (`administrative 8 city`) | 669 → 82 | 0.2 km | 90.6 | 111,823 / 1,234 | inside (3.21 km from edge) |  |
| Calgary | [r3227127](https://www.openstreetmap.org/relation/3227127) Calgary (`administrative 6`) | 1259 → 82 | 0.2 km | 853.6 | 1,267,344 / 1,485 | inside (8.86 km from edge) | large but urban |
| Edmonton | [r2564500](https://www.openstreetmap.org/relation/2564500) Edmonton (`administrative 6 city`) | 824 → 65 | 0.2 km | 780.5 | 1,010,899 / 1,295 | inside (5.91 km from edge) | large but urban |
| Eugene | [r186706](https://www.openstreetmap.org/relation/186706) Eugene (`administrative 8 city`) | 1916 → 120 | 0.3 km | 116.7 | 159,150 / 1,363 | inside (0.95 km from edge) |  |
| Jasper | [n51971014](https://www.openstreetmap.org/node/51971014) Jasper townsite: outline of OSM built-up landuse around the place=town node (`derived`) | 257 → 12 | 0.1 km | 1.8 | 4,590 / 2,491 | inside (0.13 km from edge) | ⚠ official boundary is 749 km² of park → **townsite used** |
| Kamloops | [r2230726](https://www.openstreetmap.org/relation/2230726) Kamloops (`administrative 8`) | 320 → 69 | 0.2 km | 312.3 | 97,902 / 314 | inside (0.53 km from edge) | ⚠ 312 km², 314/km²: grassland hills |
| Kelowna | [r2221794](https://www.openstreetmap.org/relation/2221794) Kelowna (`administrative 8`) | 981 → 62 | 0.2 km | 259.9 | 144,576 / 556 | inside (1.47 km from edge) | large (260 km²) incl. rural uplands, but 556/km²: not flagged |
| Leavenworth | [r237799](https://www.openstreetmap.org/relation/237799) Leavenworth (`administrative 8 city`) | 402 → 21 | 0.2 km | 3.3 | 2,263 / 692 | inside (0.47 km from edge) |  |
| Nanaimo | [r2221210](https://www.openstreetmap.org/relation/2221210) Nanaimo (`administrative 8`) | 508 → 73 | 0.2 km | 125.7 | 99,863 / 795 | inside (3.37 km from edge) |  |
| Penticton | [r2229870](https://www.openstreetmap.org/relation/2229870) Penticton (`administrative 8`) | 283 → 40 | 0.2 km | 46.0 | 43,313 / 942 | inside (0.7 km from edge) |  |
| Portland | [r186579](https://www.openstreetmap.org/relation/186579) Portland (`administrative 8 city`) | 2403 → 109 | 0.3 km | 374.0 | 652,503 / 1,744 | inside (3.01 km from edge) |  |
| Prince George | [r2243544](https://www.openstreetmap.org/relation/2243544) Prince George (`administrative 8`) | 265 → 56 | 0.2 km | 327.9 | 76,708 / 234 | inside (4.24 km from edge) | ⚠ 328 km², 234/km²: forest & rural |
| Salem | [r186479](https://www.openstreetmap.org/relation/186479) Salem (`administrative 8 city`) | 1535 → 111 | 0.35 km | 127.2 | 155,469 / 1,223 | inside (1.65 km from edge) |  |
| Spokane | [r237599](https://www.openstreetmap.org/relation/237599) Spokane (`administrative 8 city`) | 1457 → 99 | 0.25 km | 179.6 | 228,989 / 1,275 | inside (2.95 km from edge) |  |
| Vancouver | [r1852574](https://www.openstreetmap.org/relation/1852574) Vancouver (`administrative 8`) | 217 → 29 | 0.2 km | 137.1 | 631,486 / 4,608 | inside (4.36 km from edge) |  |
| Victoria | [r2221062](https://www.openstreetmap.org/relation/2221062) Victoria (`administrative 8`) | 712 → 20 | 0.2 km | 21.5 | 85,792 / 3,992 | inside (1.83 km from edge) |  |
| Whistler | [r7858397](https://www.openstreetmap.org/relation/7858397) Whistler Resort Municipality (`administrative 8`) | 49 → 25 | 0.2 km | 242.9 | 9,824 / 40 | inside (3.64 km from edge) | ⚠ 243 km², 40/km²: valley + Whistler & Blackcomb |
| Whitehorse | [r9561268](https://www.openstreetmap.org/relation/9561268) Whitehorse (`administrative 6`) | 131 → 25 | 0.2 km | 425.6 | 27,889 / 66 | inside (5.49 km from edge) | ⚠ 426 km², 66/km²: mostly forest & hills |
| Canmore | [r8452489](https://www.openstreetmap.org/relation/8452489) Town of Canmore (`administrative 6`) | 293 → 45 | 0.25 km | 68.9 | 13,992 / 203 | inside (1.79 km from edge) | ⚠ 69 km², 203/km²: mountain slopes |
| Cannon Beach | [r186503](https://www.openstreetmap.org/relation/186503) Cannon Beach (`administrative 8 city`) | 553 → 15 | 0.2 km | 4.3 | 1,720 / 395 | inside (0.07 km from edge) |  |
| Dawson City | [r9457300](https://www.openstreetmap.org/relation/9457300) Dawson City (`administrative 6`) | 378 → 17 | 0.2 km | 37.6 | — | inside (0.95 km from edge) | ⚠ 38 km², ~42/km² (no OSM pop; 2021 census 1,577) |
| Drumheller | [r6633892](https://www.openstreetmap.org/relation/6633892) Drumheller (`administrative 6`) | 221 → 53 | 0.2 km | 107.5 | 7,932 / 74 | inside (1.18 km from edge) | ⚠ 25 km of badlands valley, 74/km² |
| Fernie | [r2221420](https://www.openstreetmap.org/relation/2221420) Fernie (`administrative 8`) | 153 → 19 | 0.2 km | 14.8 | 6,320 / 426 | inside (1.01 km from edge) |  |
| Golden | [r2238685](https://www.openstreetmap.org/relation/2238685) Golden (`administrative 8`) | 71 → 17 | 0.2 km | 12.2 | — | inside (1.07 km from edge) |  |
| Nelson | [r2221423](https://www.openstreetmap.org/relation/2221423) Nelson (`administrative 8`) | 220 → 23 | 0.2 km | 9.9 | 11,198 / 1,128 | inside (0.73 km from edge) |  |
| North Bend | [r237364](https://www.openstreetmap.org/relation/237364) North Bend (`administrative 8 city`) | 241 → 29 | 0.2 km | 8.2 | 5,731 / 695 | inside (0.05 km from edge) |  |
| Pemberton | [r2230698](https://www.openstreetmap.org/relation/2230698) Pemberton (`administrative 8`) | 2861 → 101 | 0.2 km | 51.6 | — | inside (0.66 km from edge) | ⚠ 52 km², ~66/km² (no OSM pop; 2021 census 3,407) |
| Port Hardy | [r2221303](https://www.openstreetmap.org/relation/2221303) Port Hardy (`administrative 8`) | 157 → 29 | 0.2 km | 46.8 | 4,008 / 86 | inside (0.74 km from edge) | ⚠ 47 km², 86/km²: forest south of town |
| Revelstoke | [r2240574](https://www.openstreetmap.org/relation/2240574) Revelstoke (`administrative 8`) | 199 → 50 | 0.2 km | 47.0 | 8,275 / 176 | inside (0.59 km from edge) | ⚠ 47 km², 176/km²: incl. ski-hill slopes |
| Sisters | [r186776](https://www.openstreetmap.org/relation/186776) Sisters (`administrative 8 city`) | 100 → 22 | 0.2 km | 4.9 | 3,064 / 629 | inside (0.64 km from edge) |  |
| Squamish | [r2238688](https://www.openstreetmap.org/relation/2238688) Squamish (`administrative 8`) | 384 → 75 | 0.2 km | 120.2 | 23,819 / 198 | inside (2.12 km from edge) | ⚠ 120 km², 198/km²: valley north + slopes |
| Tofino | [r2221212](https://www.openstreetmap.org/relation/2221212) Tofino (`administrative 8`) | 312 → 28 | 0.2 km | 18.6 | 2,650 / 143 | inside (1.03 km from edge) |  |
| Winthrop | [r237891](https://www.openstreetmap.org/relation/237891) Winthrop (`administrative 8 town`) | 120 → 11 | 0.2 km | 2.3 | 371 / 159 | inside (0.27 km from edge) |  |
| Yakima | [r237752](https://www.openstreetmap.org/relation/237752) Yakima (`administrative 8 city`) | 423 → 79 | 0.2 km | 71.5 | 96,968 / 1,356 | inside (1.94 km from edge) |  |
| Darrington | [r237657](https://www.openstreetmap.org/relation/237657) Darrington (`administrative 8 town`) | 182 → 15 | 0.2 km | 2.4 | — | inside (0.3 km from edge) |  |
| Fall City | [r238168](https://www.openstreetmap.org/relation/238168) Fall City (`census`) | 279 → 15 | 0.2 km | 3.3 | 1,993 / 606 | inside (0.15 km from edge) | US census CDP (unincorporated) |
| Gold Bar | [r237236](https://www.openstreetmap.org/relation/237236) Gold Bar (`administrative 8 city`) | 312 → 14 | 0.2 km | 2.8 | 2,403 / 871 | inside (0.16 km from edge) |  |
| Index | [r237661](https://www.openstreetmap.org/relation/237661) Index (`administrative 8 town`) | 58 → 10 | 0.1 km | 0.6 | 155 / 242 | inside (0.18 km from edge) |  |
| Marblemount | [r238164](https://www.openstreetmap.org/relation/238164) Marblemount (`census`) | 340 → 20 | 0.2 km | 6.2 | — | inside (0.15 km from edge) | US census CDP (unincorporated) |

*pop / density*: OSM `population` (boundary tag, else the town's place node) and people per km² of the ring; a low density usually means the boundary takes in a lot of empty land.

### Skipped towns (no usable boundary)

- **Mazama**: no admin or census boundary contains the point (only Okanogan County); unincorporated, and OSM has no Mazama CDP. The current point 48.5922,-120.4039 stays.
- **Bella Coola**: unincorporated; the only boundary is Central Coast RD Electoral Area D (East Bella Coola), a huge rural district. The current point 52.3667,-126.7500 stays.
- **Waterton**: Waterton Park is an unincorporated hamlet (pop ~105); the only boundary is Improvement District No. 4 = all of Waterton Lakes National Park. The current point 49.0509,-113.9070 stays.

## Extended features

| Feature | OSM | kind | pts raw → out | tol | size | current point |
|---|---|---|---|---|---|---|
| Hoh Rainforest | [r14526701](https://www.openstreetmap.org/relation/14526701) | line | 868 → 45 | 0.3 km | 66.3 km long | 0.12 km from the line |
| Three Sisters | [n357312944](https://www.openstreetmap.org/node/357312944), [n357312388](https://www.openstreetmap.org/node/357312388), [n357315877](https://www.openstreetmap.org/node/357315877) | line | 3 → 3 | exact | 7.4 km long | 0.0 km from the line |
| Goat Rocks | [r6109176](https://www.openstreetmap.org/relation/6109176) | area | 2591 → 72 | 0.5 km | 438.00 km² | inside (0.51 km from edge) |
| Discovery Park | [r4874562](https://www.openstreetmap.org/relation/4874562) | area | 221 → 15 | 0.1 km | 2.51 km² | inside (0.45 km from edge) |
| Painted Hills | [r13917927](https://www.openstreetmap.org/relation/13917927) | area | 484 → 27 | 0.15 km | 12.17 km² | inside (1.33 km from edge) |
| Alpental | [r6855067](https://www.openstreetmap.org/relation/6855067) | area | 97 → 14 | 0.1 km | 1.74 km² | inside (0.12 km from edge) |
| Crystal Mountain | [r11518092](https://www.openstreetmap.org/relation/11518092) | area | 131 → 19 | 0.15 km | 8.96 km² | inside (0.98 km from edge) |
| Mission Ridge | [r15657511](https://www.openstreetmap.org/relation/15657511) | area | 167 → 18 | 0.1 km | 4.19 km² | inside (0.0 km from edge) |
| Mt Baker Ski Area | [r19108017](https://www.openstreetmap.org/relation/19108017) | area | 31 → 13 | 0.1 km | 4.14 km² | inside (0.31 km from edge) |
| Summit at Snoqualmie | [w1361868120](https://www.openstreetmap.org/way/1361868120) | area | 147 → 25 | 0.1 km | 3.96 km² | **outside, 0.02 km** |
| White Pass Ski Area | [w1254864194](https://www.openstreetmap.org/way/1254864194) | area | 18 → 17 | 0.1 km | 5.72 km² | inside (0.17 km from edge) |

## Per-feature details

### Astoria

- **OSM:** [r186203](https://www.openstreetmap.org/relation/186203) — Astoria; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=9477`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 109 → 21 points, DP 0.2 km, max deviation 0.138 km; valid simple polygon after rounding; first == last.
- **Size:** 26.23 km² (raw outer ring 26.07 km²), perimeter 29.6 km, reaches 5.5 km from the current point. Population 9,477 (boundary tag), 361/km².
- **Current point** 46.1883,-123.8100: inside, 1.2 km from the edge.
- **Notes:** US city limits often extend into water: the ring is 26.2 km² while Astoria's land area is only ~16 km² (US Census), because the city limits take in a slice of the Columbia River estuary. Taps just off the waterfront count as inside.

### Banff

- **OSM:** [r8452792](https://www.openstreetmap.org/relation/8452792) — Banff; `boundary=administrative`, `admin_level=6`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 184 → 18 points, DP 0.2 km, max deviation 0.191 km; valid simple polygon after rounding; first == last.
- **Size:** 4.89 km² (raw outer ring 4.86 km²), perimeter 13.8 km, reaches 2.4 km from the current point. Population 7,847 (place node (town)), 1,605/km².
- **Current point** 51.1778,-115.5736: inside, 0.26 km from the edge.
- **Notes:** Town of Banff (admin_level 6 in OSM), 4.9 km²: the townsite only, not the national park.

### Bellingham

- **OSM:** [r237440](https://www.openstreetmap.org/relation/237440) — Bellingham; `boundary=administrative`, `admin_level=8`, `border_type=city`, `place=city`, `type=boundary`, `population=91482`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 381 → 46 points, DP 0.2 km, max deviation 0.2 km; valid simple polygon after rounding; first == last.
- **Size:** 78.87 km² (raw outer ring 78.76 km²), perimeter 57.0 km, reaches 8.0 km from the current point. Population 91,482 (boundary tag), 1,160/km².
- **Current point** 48.7500,-122.4833: inside, 1.06 km from the edge.

### Bend

- **OSM:** [r186761](https://www.openstreetmap.org/relation/186761) — Bend; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=111823`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 669 → 82 points, DP 0.2 km, max deviation 0.181 km; valid simple polygon after rounding; first == last. Filled 3 inner member(s) (holes/enclaves).
- **Size:** 90.62 km² (raw outer ring 90.18 km²), perimeter 65.6 km, reaches 8.1 km from the current point. Population 111,823 (boundary tag), 1,234/km².
- **Current point** 44.0582,-121.3153: inside, 3.21 km from the edge.

### Calgary

- **OSM:** [r3227127](https://www.openstreetmap.org/relation/3227127) — Calgary; `boundary=administrative`, `admin_level=6`, `type=boundary`, `population=1267344`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 1259 → 82 points, DP 0.2 km, max deviation 0.198 km; valid simple polygon after rounding; first == last. Filled 9 inner member(s) (holes/enclaves).
- **Size:** 853.63 km² (raw outer ring 853.36 km²), perimeter 174.3 km, reaches 25.4 km from the current point. Population 1,267,344 (boundary tag), 1,485/km².
- **Current point** 51.0475,-114.0625: inside, 8.86 km from the edge.
- **Notes:** 853.6 km² with 9 holes filled. Large, but urban (1,485/km²), so the footprint is fair.

### Edmonton

- **OSM:** [r2564500](https://www.openstreetmap.org/relation/2564500) — Edmonton; `boundary=administrative`, `admin_level=6`, `border_type=city`, `type=boundary`, `population=1010899`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 824 → 65 points, DP 0.2 km, max deviation 0.196 km; valid simple polygon after rounding; first == last.
- **Size:** 780.45 km² (raw outer ring 780.8 km²), perimeter 162.8 km, reaches 25.3 km from the current point. Population 1,010,899 (boundary tag), 1,295/km².
- **Current point** 53.5344,-113.4903: inside, 5.91 km from the edge.
- **Notes:** 780.5 km², urban (1,295/km²). The current point is in Rossdale, by the river valley.

### Eugene

- **OSM:** [r186706](https://www.openstreetmap.org/relation/186706) — Eugene; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=159150`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 1916 → 120 points, DP 0.3 km (GEOS topology-preserving), max deviation 0.283 km; valid simple polygon after rounding; first == last. Dropped 170 detached part(s), 3.617 km²; filled 106 inner member(s) (holes/enclaves).
- **Size:** 116.73 km² (raw outer ring 115.71 km²), perimeter 108.4 km, reaches 8.7 km from the current point. Population 159,150 (boundary tag), 1,363/km².
- **Current point** 44.0564,-123.1175: inside, 0.95 km from the edge.
- **Notes:** The OSM city boundary is fragmented: 170 small detached pieces (3.6 km² in total) and 106 inner holes (unincorporated islands). Per the rules the main polygon's outer ring is used, so the holes are filled and the parcels dropped. Topology-preserving simplification at 0.3 km (120 points).

### Jasper

- **OSM:** [n51971014](https://www.openstreetmap.org/node/51971014) — Jasper townsite: outline of OSM built-up landuse around the place=town node; `derived_from=landuse=residential/commercial/industrial/railway`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 257 → 12 points, DP 0.1 km, max deviation 0.096 km; valid simple polygon after rounding; first == last. Dropped 1 detached part(s), 0.021 km².
- **Size:** 1.84 km² (raw outer ring 1.8 km²), perimeter 7.7 km, reaches 2.4 km from the current point. Population 4,590 (place node (town)), 2,491/km².
- **Current point** 52.8731,-118.0822: inside, 0.13 km from the edge.
- **Notes:** The only OSM boundary is r6282024 "Municipality of Jasper" (admin_level 6). It covers 749 km² of Jasper National Park and reaches 29 km from town, with 6 people/km², so a tap 25 km up the Athabasca would score 100. You asked for the townsite and OSM has no townsite boundary, so I built one: 51 built-up landuse polygons (residential, commercial, industrial and the rail yard) merged with a 150 m morphological closing. That gives 1.84 km², 12 points, containing the current point. It is derived, not an official line. The municipality ring is below if you prefer it.
- **Alternative (not used):** the official boundary [r6282024](https://www.openstreetmap.org/relation/6282024) Municipality of Jasper, 22 points at 0.2 km, 748.71 km², reaching 29.3 km from the town, 6/km². Paste this `geometry` instead to use it:

  ```
  52.8429,-118.4025; 52.8472,-118.3841; 52.8515,-118.4033; 52.8499,-118.4393; 52.8580,-118.4552; 52.8686,-118.4645; 52.8759,-118.4533; 52.8825,-118.4502; 52.8869,-118.4530; 52.8889,-118.4613; 52.8989,-118.4750; 52.9019,-118.4930; 52.9058,-118.4982; 52.9058,-118.5080; 52.9302,-118.5079; 52.9302,-118.2903; 53.0174,-118.2904; 53.0177,-117.9182; 52.7559,-117.9182; 52.7556,-118.1453; 52.8429,-118.1453; 52.8429,-118.4025
  ```

### Kamloops

- **OSM:** [r2230726](https://www.openstreetmap.org/relation/2230726) — Kamloops; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 320 → 69 points, DP 0.2 km, max deviation 0.195 km; valid simple polygon after rounding; first == last.
- **Size:** 312.28 km² (raw outer ring 313.37 km²), perimeter 140.6 km, reaches 22.1 km from the current point. Population 97,902 (place node (city)), 314/km².
- **Current point** 50.6758,-120.3394: inside, 0.53 km from the edge.
- **Notes:** 312 km²; much of it is the grassland and sage hills around the river valleys (314/km²).

### Kelowna

- **OSM:** [r2221794](https://www.openstreetmap.org/relation/2221794) — Kelowna; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 981 → 62 points, DP 0.2 km, max deviation 0.201 km; valid simple polygon after rounding; first == last. Filled 1 inner member(s) (holes/enclaves).
- **Size:** 259.85 km² (raw outer ring 259.03 km²), perimeter 97.8 km, reaches 17.1 km from the current point. Population 144,576 (place node (city)), 556/km².
- **Current point** 49.8881,-119.4956: inside, 1.47 km from the edge.

### Leavenworth

- **OSM:** [r237799](https://www.openstreetmap.org/relation/237799) — Leavenworth; `boundary=administrative`, `admin_level=8`, `border_type=city`, `place=city`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 402 → 21 points, DP 0.2 km, max deviation 0.194 km; valid simple polygon after rounding; first == last. Filled 1 inner member(s) (holes/enclaves).
- **Size:** 3.27 km² (raw outer ring 3.37 km²), perimeter 13.7 km, reaches 2.4 km from the current point. Population 2,263 (place node (town)), 692/km².
- **Current point** 47.5950,-120.6628: inside, 0.47 km from the edge.

### Nanaimo

- **OSM:** [r2221210](https://www.openstreetmap.org/relation/2221210) — Nanaimo; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 508 → 73 points, DP 0.2 km, max deviation 0.198 km; valid simple polygon after rounding; first == last.
- **Size:** 125.68 km² (raw outer ring 124.85 km²), perimeter 76.5 km, reaches 13.1 km from the current point. Population 99,863 (place node (city)), 795/km².
- **Current point** 49.1642,-123.9364: inside, 3.37 km from the edge.

### Penticton

- **OSM:** [r2229870](https://www.openstreetmap.org/relation/2229870) — Penticton; `boundary=administrative`, `admin_level=8`, `type=boundary`, `population=43313`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 283 → 40 points, DP 0.2 km, max deviation 0.161 km; valid simple polygon after rounding; first == last. Filled 1 inner member(s) (holes/enclaves).
- **Size:** 45.98 km² (raw outer ring 45.61 km²), perimeter 49.5 km, reaches 8.9 km from the current point. Population 43,313 (boundary tag), 942/km².
- **Current point** 49.5008,-119.5939: inside, 0.7 km from the edge.

### Portland

- **OSM:** [r186579](https://www.openstreetmap.org/relation/186579) — Portland; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=652503`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 2403 → 109 points, DP 0.3 km, max deviation 0.299 km; valid simple polygon after rounding; first == last. Dropped 1 detached part(s), 0.001 km²; filled 17 inner member(s) (holes/enclaves).
- **Size:** 374.04 km² (raw outer ring 374.47 km²), perimeter 135.6 km, reaches 16.9 km from the current point. Population 652,503 (boundary tag), 1,744/km².
- **Current point** 45.5200,-122.6819: inside, 3.01 km from the edge.
- **Notes:** Outer ring of the main polygon; 17 holes filled and one 0.001 km² sliver dropped. Includes Forest Park and reaches north to the Columbia River. 109 points at 0.3 km.

### Prince George

- **OSM:** [r2243544](https://www.openstreetmap.org/relation/2243544) — Prince George; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 265 → 56 points, DP 0.2 km, max deviation 0.191 km; valid simple polygon after rounding; first == last.
- **Size:** 327.87 km² (raw outer ring 327.91 km²), perimeter 104.9 km, reaches 15.7 km from the current point. Population 76,708 (place node (city)), 234/km².
- **Current point** 53.9131,-122.7453: inside, 4.24 km from the edge.
- **Notes:** 328 km² of city limits, much of it forest and rural land (234/km²).

### Salem

- **OSM:** [r186479](https://www.openstreetmap.org/relation/186479) — Salem; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=155469`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 1535 → 111 points, DP 0.35 km, max deviation 0.344 km; valid simple polygon after rounding; first == last. Filled 7 inner member(s) (holes/enclaves).
- **Size:** 127.15 km² (raw outer ring 127.17 km²), perimeter 116.9 km, reaches 10.2 km from the current point. Population 155,469 (boundary tag), 1,223/km².
- **Current point** 44.9400,-123.0389: inside, 1.65 km from the edge.
- **Notes:** 7 holes filled. Needed 0.35 km to get to 111 points.

### Spokane

- **OSM:** [r237599](https://www.openstreetmap.org/relation/237599) — Spokane; `boundary=administrative`, `admin_level=8`, `border_type=city`, `place=city`, `type=boundary`, `population=228989`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 1457 → 99 points, DP 0.25 km, max deviation 0.245 km; valid simple polygon after rounding; first == last.
- **Size:** 179.59 km² (raw outer ring 179.55 km²), perimeter 119.9 km, reaches 14.3 km from the current point. Population 228,989 (boundary tag), 1,275/km².
- **Current point** 47.6589,-117.4250: inside, 2.95 km from the edge.
- **Notes:** 0.25 km for 99 points.

### Vancouver

- **OSM:** [r1852574](https://www.openstreetmap.org/relation/1852574) — Vancouver; `boundary=administrative`, `admin_level=8`, `type=boundary`, `population=631486`, `official_name=City of Vancouver`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 217 → 29 points, DP 0.2 km, max deviation 0.168 km; valid simple polygon after rounding; first == last.
- **Size:** 137.05 km² (raw outer ring 136.54 km²), perimeter 55.5 km, reaches 9.4 km from the current point. Population 631,486 (boundary tag), 4,608/km².
- **Current point** 49.2608,-123.1139: inside, 4.36 km from the edge.
- **Notes:** 137 km², more than the city's ~115 km² of land: the OSM boundary takes in some harbour and bay water. Its west edge is at -123.225.

### Victoria

- **OSM:** [r2221062](https://www.openstreetmap.org/relation/2221062) — Victoria; `boundary=administrative`, `admin_level=8`, `type=boundary`, `population=85792`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 712 → 20 points, DP 0.2 km, max deviation 0.187 km; valid simple polygon after rounding; first == last. Filled 1 inner member(s) (holes/enclaves).
- **Size:** 21.49 km² (raw outer ring 21.28 km²), perimeter 20.2 km, reaches 3.5 km from the current point. Population 85,792 (boundary tag), 3,992/km².
- **Current point** 48.4283,-123.3647: inside, 1.83 km from the edge.

### Whistler

- **OSM:** [r7858397](https://www.openstreetmap.org/relation/7858397) — Whistler Resort Municipality; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 49 → 25 points, DP 0.2 km, max deviation 0.195 km; valid simple polygon after rounding; first == last.
- **Size:** 242.91 km² (raw outer ring 242.69 km²), perimeter 72.5 km, reaches 16.5 km from the current point. Population 9,824 (place node (town)), 40/km².
- **Current point** 50.1167,-122.9542: inside, 3.64 km from the edge.
- **Notes:** r7858397 "Whistler Resort Municipality": 243 km², stretching 23.5 km end to end along the valley and taking in Whistler and Blackcomb mountains; 9,824 people (40/km²).

### Whitehorse

- **OSM:** [r9561268](https://www.openstreetmap.org/relation/9561268) — Whitehorse; `boundary=administrative`, `admin_level=6`, `type=boundary`, `population=27889`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 131 → 25 points, DP 0.2 km, max deviation 0.195 km; valid simple polygon after rounding; first == last.
- **Size:** 425.65 km² (raw outer ring 425.22 km²), perimeter 92.3 km, reaches 19.0 km from the current point. Population 27,889 (boundary tag), 66/km².
- **Current point** 60.7242,-135.0561: inside, 5.49 km from the edge.
- **Notes:** r9561268 (admin_level 6): 426 km² of mostly forest, lakes and hills; 27,889 people (66/km²).

### Canmore

- **OSM:** [r8452489](https://www.openstreetmap.org/relation/8452489) — Town of Canmore; `boundary=administrative`, `admin_level=6`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 293 → 45 points, DP 0.25 km, max deviation 0.196 km; valid simple polygon after rounding; first == last.
- **Size:** 68.92 km² (raw outer ring 68.66 km²), perimeter 65.4 km, reaches 12.0 km from the current point. Population 13,992 (place node (town)), 203/km².
- **Current point** 51.0883,-115.3478: inside, 1.79 km from the edge.
- **Notes:** 69 km², including a lot of mountainside on both sides of the Bow valley (203/km²).

### Cannon Beach

- **OSM:** [r186503](https://www.openstreetmap.org/relation/186503) — Cannon Beach; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=1720`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 553 → 15 points, DP 0.2 km, max deviation 0.174 km; valid simple polygon after rounding; first == last.
- **Size:** 4.35 km² (raw outer ring 3.96 km²), perimeter 15.3 km, reaches 3.3 km from the current point. Population 1,720 (boundary tag), 395/km².
- **Current point** 45.8819,-123.9594: inside, 0.07 km from the edge.

### Dawson City

- **OSM:** [r9457300](https://www.openstreetmap.org/relation/9457300) — Dawson City; `boundary=administrative`, `admin_level=6`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 378 → 17 points, DP 0.2 km, max deviation 0.197 km; valid simple polygon after rounding; first == last.
- **Size:** 37.6 km² (raw outer ring 37.5 km²), perimeter 32.6 km, reaches 8.2 km from the current point.
- **Current point** 64.0600,-139.4319: inside, 0.95 km from the edge.
- **Notes:** 37.6 km² around the townsite, mostly hillside. OSM has no population; the 2021 census gives 1,577 (~42/km²).

### Drumheller

- **OSM:** [r6633892](https://www.openstreetmap.org/relation/6633892) — Drumheller; `boundary=administrative`, `admin_level=6`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 221 → 53 points, DP 0.2 km (GEOS topology-preserving), max deviation 0.181 km; valid simple polygon after rounding; first == last.
- **Size:** 107.5 km² (raw outer ring 108.04 km²), perimeter 90.5 km, reaches 24.2 km from the current point. Population 7,932 (place node (town)), 74/km².
- **Current point** 51.4636,-112.7194: inside, 1.18 km from the edge.
- **Notes:** The Town of Drumheller (amalgamated with the other valley communities) stretches along the Red Deer River badlands valley, reaching 24 km from the current point (74/km²).

### Fernie

- **OSM:** [r2221420](https://www.openstreetmap.org/relation/2221420) — Fernie; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 153 → 19 points, DP 0.2 km, max deviation 0.185 km; valid simple polygon after rounding; first == last. Dropped 1 detached part(s), 0.534 km².
- **Size:** 14.82 km² (raw outer ring 14.91 km²), perimeter 19.5 km, reaches 3.5 km from the current point. Population 6,320 (place node (city)), 426/km².
- **Current point** 49.5042,-115.0628: inside, 1.01 km from the edge.
- **Notes:** Dropped a 0.53 km² detached parcel south-west of town.

### Golden

- **OSM:** [r2238685](https://www.openstreetmap.org/relation/2238685) — Golden; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 71 → 17 points, DP 0.2 km, max deviation 0.203 km; valid simple polygon after rounding; first == last.
- **Size:** 12.15 km² (raw outer ring 11.79 km²), perimeter 16.3 km, reaches 3.3 km from the current point.
- **Current point** 51.3019,-116.9667: inside, 1.07 km from the edge.
- **Notes:** OSM has no population for this boundary.

### Nelson

- **OSM:** [r2221423](https://www.openstreetmap.org/relation/2221423) — Nelson; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 220 → 23 points, DP 0.2 km, max deviation 0.188 km; valid simple polygon after rounding; first == last. Dropped 1 detached part(s), 5.997 km².
- **Size:** 9.93 km² (raw outer ring 9.98 km²), perimeter 21.7 km, reaches 4.6 km from the current point. Population 11,198 (place node (city)), 1,128/km².
- **Current point** 49.5000,-117.2833: inside, 0.73 km from the edge.
- **Notes:** Dropped a 6.0 km² detached piece ~16 km down the Kootenay River (49.460,-117.498); that is where the city's Bonnington Falls hydro plant is.

### North Bend

- **OSM:** [r237364](https://www.openstreetmap.org/relation/237364) — North Bend; `boundary=administrative`, `admin_level=8`, `border_type=city`, `place=town`, `type=boundary`, `population=5731`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 241 → 29 points, DP 0.2 km, max deviation 0.169 km; valid simple polygon after rounding; first == last.
- **Size:** 8.25 km² (raw outer ring 8.43 km²), perimeter 18.6 km, reaches 3.6 km from the current point. Population 5,731 (boundary tag), 695/km².
- **Current point** 47.4956,-121.7700: inside, 0.05 km from the edge.

### Pemberton

- **OSM:** [r2230698](https://www.openstreetmap.org/relation/2230698) — Pemberton; `boundary=administrative`, `admin_level=8`, `type=boundary`, `official_name=Pemberton Township`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 2861 → 101 points, DP 0.2 km (GEOS topology-preserving), max deviation 0.202 km; valid simple polygon after rounding; first == last.
- **Size:** 51.65 km² (raw outer ring 50.52 km²), perimeter 97.7 km, reaches 13.0 km from the current point.
- **Current point** 50.3203,-122.8075: inside, 0.66 km from the edge.
- **Notes:** 51.7 km², mostly valley farmland and forest around the village. OSM has no population; the 2021 census gives 3,407 (~66/km²). Topology-preserving simplification at 0.2 km (101 points; 2,861 raw vertices).

### Port Hardy

- **OSM:** [r2221303](https://www.openstreetmap.org/relation/2221303) — Port Hardy; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 157 → 29 points, DP 0.2 km, max deviation 0.2 km; valid simple polygon after rounding; first == last. Dropped 1 detached part(s), 0.996 km²; filled 11 inner member(s) (holes/enclaves).
- **Size:** 46.78 km² (raw outer ring 47.12 km²), perimeter 41.6 km, reaches 13.9 km from the current point. Population 4,008 (place node (town)), 86/km².
- **Current point** 50.7244,-127.4976: inside, 0.74 km from the edge.
- **Notes:** 47 km², mostly forest south of town (86/km²). Dropped: a 1.0 km² detached parcel 14 km south; 11 holes filled.

### Revelstoke

- **OSM:** [r2240574](https://www.openstreetmap.org/relation/2240574) — Revelstoke; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 199 → 50 points, DP 0.2 km, max deviation 0.193 km; valid simple polygon after rounding; first == last.
- **Size:** 47.03 km² (raw outer ring 47.5 km²), perimeter 52.2 km, reaches 9.1 km from the current point. Population 8,275 (place node (city)), 176/km².
- **Current point** 50.9981,-118.1956: inside, 0.59 km from the edge.
- **Notes:** 47 km², including hillsides around the town (176/km²).

### Sisters

- **OSM:** [r186776](https://www.openstreetmap.org/relation/186776) — Sisters; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=3064`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 100 → 22 points, DP 0.2 km (GEOS topology-preserving), max deviation 0.184 km; valid simple polygon after rounding; first == last.
- **Size:** 4.87 km² (raw outer ring 4.97 km²), perimeter 16.7 km, reaches 2.9 km from the current point. Population 3,064 (boundary tag), 629/km².
- **Current point** 44.2909,-121.5493: inside, 0.64 km from the edge.

### Squamish

- **OSM:** [r2238688](https://www.openstreetmap.org/relation/2238688) — Squamish; `boundary=administrative`, `admin_level=8`, `type=boundary`, `official_name=Squamish District Municipality`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 384 → 75 points, DP 0.2 km, max deviation 0.199 km; valid simple polygon after rounding; first == last.
- **Size:** 120.22 km² (raw outer ring 121.05 km²), perimeter 103.4 km, reaches 19.1 km from the current point. Population 23,819 (place node (city)), 198/km².
- **Current point** 49.7017,-123.1589: inside, 2.12 km from the edge.
- **Notes:** 120 km², running north up the Squamish valley and including steep slopes on both sides (198/km²).

### Tofino

- **OSM:** [r2221212](https://www.openstreetmap.org/relation/2221212) — Tofino; `boundary=administrative`, `admin_level=8`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 312 → 28 points, DP 0.2 km, max deviation 0.199 km; valid simple polygon after rounding; first == last.
- **Size:** 18.59 km² (raw outer ring 18.96 km²), perimeter 28.5 km, reaches 7.9 km from the current point. Population 2,650 (place node (town)), 143/km².
- **Current point** 49.1531,-125.9044: inside, 1.03 km from the edge.

### Winthrop

- **OSM:** [r237891](https://www.openstreetmap.org/relation/237891) — Winthrop; `boundary=administrative`, `admin_level=8`, `border_type=town`, `place=town`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 120 → 11 points, DP 0.2 km, max deviation 0.153 km; valid simple polygon after rounding; first == last. Dropped 2 detached part(s), 0.139 km²; filled 2 inner member(s) (holes/enclaves).
- **Size:** 2.33 km² (raw outer ring 2.29 km²), perimeter 7.7 km, reaches 1.4 km from the current point. Population 371 (place node (village)), 159/km².
- **Current point** 48.4717,-120.1792: inside, 0.27 km from the edge.
- **Notes:** Dropped two tiny detached parcels (0.14 km²) and filled 2 holes.

### Yakima

- **OSM:** [r237752](https://www.openstreetmap.org/relation/237752) — Yakima; `boundary=administrative`, `admin_level=8`, `border_type=city`, `place=city`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 423 → 79 points, DP 0.2 km, max deviation 0.191 km; valid simple polygon after rounding; first == last. Filled 1 inner member(s) (holes/enclaves).
- **Size:** 71.5 km² (raw outer ring 71.22 km²), perimeter 63.5 km, reaches 11.3 km from the current point. Population 96,968 (place node (city)), 1,356/km².
- **Current point** 46.6016,-120.5108: inside, 1.94 km from the edge.

### Darrington

- **OSM:** [r237657](https://www.openstreetmap.org/relation/237657) — Darrington; `boundary=administrative`, `admin_level=8`, `border_type=town`, `place=town`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 182 → 15 points, DP 0.2 km, max deviation 0.197 km; valid simple polygon after rounding; first == last.
- **Size:** 2.39 km² (raw outer ring 2.5 km²), perimeter 8.8 km, reaches 1.7 km from the current point.
- **Current point** 48.2522,-121.6031: inside, 0.3 km from the edge.
- **Notes:** OSM has no population for this boundary.

### Fall City

- **OSM:** [r238168](https://www.openstreetmap.org/relation/238168) — Fall City; `boundary=census`, `type=boundary`, `population=1993`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 279 → 15 points, DP 0.2 km, max deviation 0.128 km; valid simple polygon after rounding; first == last.
- **Size:** 3.29 km² (raw outer ring 3.32 km²), perimeter 9.6 km, reaches 2.6 km from the current point. Population 1,993 (boundary tag), 606/km².
- **Current point** 47.5661,-121.8886: inside, 0.15 km from the edge.
- **Notes:** Unincorporated. Uses the census-designated place (`boundary=census`, r238168; population 1,993).

### Gold Bar

- **OSM:** [r237236](https://www.openstreetmap.org/relation/237236) — Gold Bar; `boundary=administrative`, `admin_level=8`, `border_type=city`, `type=boundary`, `population=2403`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 312 → 14 points, DP 0.2 km, max deviation 0.195 km; valid simple polygon after rounding; first == last.
- **Size:** 2.76 km² (raw outer ring 2.83 km²), perimeter 11.6 km, reaches 1.9 km from the current point. Population 2,403 (boundary tag), 871/km².
- **Current point** 47.8542,-121.6933: inside, 0.16 km from the edge.

### Index

- **OSM:** [r237661](https://www.openstreetmap.org/relation/237661) — Index; `boundary=administrative`, `admin_level=8`, `border_type=town`, `place=village`, `type=boundary`, `population=155`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 58 → 10 points, DP 0.1 km, max deviation 0.075 km; valid simple polygon after rounding; first == last.
- **Size:** 0.64 km² (raw outer ring 0.61 km²), perimeter 3.8 km, reaches 0.8 km from the current point. Population 155 (boundary tag), 242/km².
- **Current point** 47.8208,-121.5539: inside, 0.18 km from the edge.
- **Notes:** Tiny (0.64 km²); DP stepped down to 0.1 km to keep 10 points.

### Marblemount

- **OSM:** [r238164](https://www.openstreetmap.org/relation/238164) — Marblemount; `boundary=census`, `border_type=census`, `place=locality`, `type=boundary`; data as of 2026-09-28T19:15:46Z.
- **Ring:** 340 → 20 points, DP 0.2 km, max deviation 0.189 km; valid simple polygon after rounding; first == last.
- **Size:** 6.21 km² (raw outer ring 6.07 km²), perimeter 18.9 km, reaches 4.4 km from the current point.
- **Current point** 48.5417,-121.4397: inside, 0.15 km from the edge.
- **Notes:** Unincorporated. Uses the census-designated place (`boundary=census`, r238164), 6.2 km².

### Hoh Rainforest

- **OSM:** [r14526701](https://www.openstreetmap.org/relation/14526701) — Hoh River; `type=waterway`, `waterway=river`; data as of 2026-09-28T19:12:51Z.
- **Line:** 868 → 45 points (DP 0.3 km), 66.3 km, open (first != last) so it stays a line.
- **Current point** 47.8614,-123.9247: 0.12 km from the line.
- **Notes:** The Hoh River's `type=waterway` relation (r14526701; 10 main_stream ways, all connected). The line runs from the mouth at the Pacific (47.7482,-124.4340) up the valley to the river node nearest the "Olympus Ranger Station Camp" node 5633448526 (Olympus Guard Station; 0.14 km away), past the visitor center and Happy Four Shelter (0.06 km from the line). The line is 66.3 km after simplification; the raw river is 72.9 km. The current point (visitor center area) is 0.12 km from the line. The upper river beyond Olympus Guard Station (to Glacier Meadows) is not included. Category stays `poi`; with first ≠ last it scores as a line.

### Three Sisters

- **OSM:** [n357312944](https://www.openstreetmap.org/node/357312944), [n357312388](https://www.openstreetmap.org/node/357312388), [n357315877](https://www.openstreetmap.org/node/357315877) — North Sister → Middle Sister → South Sister; data as of 2026-09-28T19:11:51Z.
- **Line:** 3 → 3 points (exact summit nodes), 7.4 km, open (first != last) so it stays a line.
- **Current point** 44.1484,-121.7841: 0.0 km from the line.
- **Notes:** The three summit nodes in the order asked: North Sister (n357312944, 3,075 m), Middle Sister (n357312388, 3,064 m), South Sister (n357315877, 3,158.5 m), all `natural=volcano`. 7.4 km. The current point is exactly the Middle Sister node, so it lies on the line.

### Goat Rocks

- **OSM:** [r6109176](https://www.openstreetmap.org/relation/6109176) — Goat Rocks Wilderness; `boundary=protected_area`, `leisure=nature_reserve`, `protect_class=1b`, `protection_title=Wilderness Area`, `type=boundary`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 2591 → 72 points, DP 0.5 km, max deviation 0.497 km; valid simple polygon after rounding; first == last.
- **Size:** 438.0 km² (raw outer ring 436.61 km²), perimeter 158.6 km, reaches 22.8 km from the current point.
- **Current point** 46.4886,-121.4058: inside, 0.51 km from the edge.
- **Notes:** r6109176 "Goat Rocks Wilderness" (`boundary=protected_area`, protect_class 1b). 438 km², matching the official 108,096 acres. 72 points at 0.5 km. The current point (the Goat Rocks massif) is inside. Note: OSM also has the rocky massif itself as w530065677 `natural=bare_rock` "Goat Rocks" (1.4 km²), if you'd rather have the rocks than the whole wilderness. The current point is 0.08 km outside that polygon.

### Discovery Park

- **OSM:** [r4874562](https://www.openstreetmap.org/relation/4874562) — Discovery Park; `leisure=park`, `type=multipolygon`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 221 → 15 points, DP 0.1 km, max deviation 0.098 km; valid simple polygon after rounding; first == last. Filled 6 inner member(s) (holes/enclaves).
- **Size:** 2.51 km² (raw outer ring 2.48 km²), perimeter 7.8 km, reaches 1.5 km from the current point.
- **Current point** 47.6583,-122.4189: inside, 0.45 km from the edge.
- **Notes:** r4874562 (`leisure=park` multipolygon). Its 6 inner members (enclaves within the park) are filled. 2.5 km², 15 points.

### Painted Hills

- **OSM:** [r13917927](https://www.openstreetmap.org/relation/13917927) — John Day Fossil Beds - Painted Hills Unit; `boundary=protected_area`, `leisure=nature_reserve`, `protect_class=3`, `protection_title=National Monument`, `type=multipolygon`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 484 → 27 points, DP 0.15 km, max deviation 0.115 km; valid simple polygon after rounding; first == last.
- **Size:** 12.17 km² (raw outer ring 12.17 km²), perimeter 19.3 km, reaches 3.1 km from the current point.
- **Current point** 44.6481,-120.2654: inside, 1.33 km from the edge.
- **Notes:** r13917927 "John Day Fossil Beds - Painted Hills Unit" (`protected_area`, National Monument). 12.2 km², close to the published 3,132 acres (12.7 km²). 27 points at 0.15 km. The current point (overlook) is inside.

### Alpental

- **OSM:** [r6855067](https://www.openstreetmap.org/relation/6855067) — Alpental; `landuse=winter_sports`, `type=multipolygon`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 97 → 14 points, DP 0.1 km, max deviation 0.09 km; valid simple polygon after rounding; first == last. Filled 1 inner member(s) (holes/enclaves).
- **Size:** 1.74 km² (raw outer ring 1.74 km²), perimeter 5.9 km, reaches 1.7 km from the current point.
- **Current point** 47.4443,-121.4255: inside, 0.12 km from the edge.
- **Notes:** r6855067 `landuse=winter_sports` "Alpental" (not the separate "Alpental Backcountry" r6855066). 1.7 km², 14 points.

### Crystal Mountain

- **OSM:** [r11518092](https://www.openstreetmap.org/relation/11518092) — Crystal Mountain; `landuse=winter_sports`, `type=multipolygon`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 131 → 19 points, DP 0.15 km, max deviation 0.15 km; valid simple polygon after rounding; first == last.
- **Size:** 8.96 km² (raw outer ring 8.96 km²), perimeter 15.4 km, reaches 2.8 km from the current point.
- **Current point** 46.9328,-121.4880: inside, 0.98 km from the edge.
- **Notes:** r11518092 `landuse=winter_sports`. 9.0 km², 19 points.

### Mission Ridge

- **OSM:** [r15657511](https://www.openstreetmap.org/relation/15657511) — Mission Ridge; `landuse=winter_sports`, `type=multipolygon`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 167 → 18 points, DP 0.1 km, max deviation 0.102 km; valid simple polygon after rounding; first == last.
- **Size:** 4.19 km² (raw outer ring 4.15 km²), perimeter 9.6 km, reaches 3.0 km from the current point.
- **Current point** 47.2924,-120.3999: inside, 0.0 km from the edge.
- **Notes:** r15657511 `landuse=winter_sports`. 4.2 km², 18 points. The current point is on the edge, just inside.

### Mt Baker Ski Area

- **OSM:** [r19108017](https://www.openstreetmap.org/relation/19108017) — Mt Baker; `landuse=winter_sports`, `type=multipolygon`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 31 → 13 points, DP 0.1 km, max deviation 0.092 km; valid simple polygon after rounding; first == last.
- **Size:** 4.14 km² (raw outer ring 4.18 km²), perimeter 8.8 km, reaches 1.9 km from the current point.
- **Current point** 48.8600,-121.6650: inside, 0.31 km from the edge.
- **Notes:** r19108017 `landuse=winter_sports` "Mt Baker". 4.1 km², 13 points.

### Summit at Snoqualmie

- **OSM:** [w1361868120](https://www.openstreetmap.org/way/1361868120) — Three Summits; `landuse=winter_sports`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 147 → 25 points, DP 0.1 km, max deviation 0.093 km; valid simple polygon after rounding; first == last.
- **Size:** 3.96 km² (raw outer ring 3.97 km²), perimeter 13.4 km, reaches 4.9 km from the current point.
- **Current point** 47.4243,-121.4162: **outside**, 0.02 km from the edge.
- **Notes:** Slightly messy in OSM, but usable. w1361868120 "Three Summits" (`landuse=winter_sports`, 3.96 km²) covers Summit West, Central and East; r20445212 is an unnamed duplicate of the same outline, and "Summit West" (w1499174311) and the Sahalie Ski Club (r6447055) are small pieces inside or next to it. Alpental has its own row, so it isn't included here. The current point (the pass base area) is 20 m outside the ring's northern edge.

### White Pass Ski Area

- **OSM:** [w1254864194](https://www.openstreetmap.org/way/1254864194) — White Pass Ski Area; `landuse=winter_sports`; data as of 2026-09-28T19:12:51Z.
- **Ring:** 18 → 17 points, DP 0.1 km, max deviation 0.029 km; valid simple polygon after rounding; first == last.
- **Size:** 5.72 km² (raw outer ring 5.75 km²), perimeter 11.9 km, reaches 4.0 km from the current point.
- **Current point** 46.6372,-121.3909: inside, 0.17 km from the edge.
- **Notes:** w1254864194 `landuse=winter_sports`. 5.7 km², 17 points. The current point (base lodge by US-12) is inside, 0.17 km from the edge.

## Queries

Discovery: an `is_in` query at every town point (all admin/census boundaries containing it, plus nearby `place` nodes) and a tags-only query for the extended features. Geometry:

```
[out:json][timeout:900];
rel(id:186203,237440,186761,186706,237799,186579,186479,237599,186503,237364,186776,237891,237752,237657,237236,237661,238168,238164);out geom;
```

```
[out:json][timeout:900];
rel(id:2230726,2221794,2221210,2229870,2243544,1852574,2221062,7858397,2221420,2238685,2221423,2230698,2221303,2240574,2238688,2221212,8452792,3227127,2564500,6282024,8452489,6633892,9561268,9457300);out geom;
```

```
[out:json][timeout:900];
(rel(id:14526701,6109176,4874562,13917927,6855067,11518092,15657511,19108017,20445212,6447055);way(id:1254864194,1361868120,1499174311,530065677););out geom;
```

Jasper townsite (built-up landuse):

```
[out:json][timeout:180];
(
  way["landuse"~"^(residential|commercial|retail|industrial|railway)$"](52.860,-118.105,52.895,-118.050);
  rel["landuse"~"^(residential|commercial|retail|industrial|railway)$"](52.860,-118.105,52.895,-118.050);
);
out geom;
```

