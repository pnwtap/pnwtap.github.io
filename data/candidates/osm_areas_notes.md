# OSM area outlines — notes

Candidate closed rings in `data/candidates/osm_areas.csv` (`name,geometry`) to replace the single-point `geometry`
of 17 rows in `data/locations.csv`: the 12 requested plus 5 of the optional small lakes (Joffre Lakes skipped —
see the end). Names match the CSV exactly. Nothing else in the project was edited.

**Source.** OpenStreetMap via the Overpass API: overpass-api.de, plus the overpass.kumi.systems mirror for Haida
Gwaii after 504 "too busy" errors. OSM data timestamps are 2026-09-28 (everything else) and 2026-07-15
(Haida Gwaii). © OpenStreetMap contributors, ODbL.

**Method.**
1. One `out tags center` discovery query to find the OSM ids, then two geometry queries (at the end of this file).
2. Ring: the outer ring of the feature's largest polygon, built by polygonizing the outer members of the way or
   multipolygon. Inner members (lake islands) are ignored, so a tap on Wizard Island, Spirit Island etc. counts
   as inside. Haida Gwaii is built differently; see its section.
3. Simplification: Douglas–Peucker in a local km projection, run on the ring as two open halves so the
   tolerance bound holds all the way round. Base tolerance is 0.3 km (0.15 km for features under ~10 km²
   or ~5 km across). It is stepped up just enough to stay at or under 120 points, and for tiny lakes stepped
   down (to a 0.05 km floor) to keep at least ~8 points. Then 4-decimal rounding, first point == last point.
4. Validity: every rounded ring is a valid simple polygon (shapely `.is_valid` on the lon/lat ring). Where
   plain DP self-intersected after rounding, GEOS's topology-preserving simplifier was used at the same
   tolerance: Kluane Lake and San Juan Island.
5. Validation: a scratch copy of `locations.csv` with these 17 rings swapped in passes
   `pnwtap.sheet.parse_locations` with bbox, region mask and categories. All 17 rows come out as
   `kind == "area"`; every category is `lake`, `island` or `poi`, none of which are route categories.

## Summary

| Feature (CSV `name`) | OSM | pts raw → out | DP tol | area km² (raw OSM) | perimeter km | current point | farthest correct tap: old score | new decay |
|---|---|---|---|---|---|---|---|---|
| Okanagan Lake | [r2903374](https://www.openstreetmap.org/relation/2903374) | 9270 → 120 | 0.3 km | 344.6 (348.8) | 253.0 | inside, 1.07 km from edge | 50.7 km: 28 | 15.52 km |
| Kluane Lake | [r3087341](https://www.openstreetmap.org/relation/3087341) | 4398 → 117 | 0.35 km | 400.5 (400.8) | 261.5 | inside, 1.35 km from edge | 42.2 km: 35 | 14.99 km |
| Maligne Lake | [r5760911](https://www.openstreetmap.org/relation/5760911) | 4273 → 29 | 0.3 km | 19.9 (20.6) | 48.0 | inside, 0.58 km from edge | 11.4 km: 75 | 33.01 km |
| Lake Crescent | [r15009108](https://www.openstreetmap.org/relation/15009108) | 1110 → 20 | 0.3 km | 20.2 (20.4) | 34.0 | inside, 0.81 km from edge | 7.1 km: 84 | 34.87 km |
| Crater Lake | [r147401](https://www.openstreetmap.org/relation/147401) | 1072 → 13 | 0.3 km | 53.2 (54.3) | 27.5 | inside, 3.3 km from edge | 5.4 km: 87 | 35.65 km |
| Diablo Lake | [r443823](https://www.openstreetmap.org/relation/443823) | 619 → 19 | 0.15 km | 2.8 (2.9) | 15.7 | inside, 0.09 km from edge | 5.0 km: 88 | 37.57 km |
| Garibaldi Lake | [r2161893](https://www.openstreetmap.org/relation/2161893) | 1180 → 25 | 0.15 km | 10.4 (10.1) | 17.4 | inside, 0.55 km from edge | 4.1 km: 90 | 37.28 km |
| San Juan Island | [r3958317](https://www.openstreetmap.org/relation/3958317) | 4308 → 74 | 0.3 km | 144.3 (143.5) | 90.6 | inside, 4.69 km from edge | 12.8 km: 73 | 27.55 km |
| Haida Gwaii | [r6439518](https://www.openstreetmap.org/relation/6439518) | 2943 → 113 | 1.0 km | 13396.2 (13325.4) | 805.9 | inside, 25.12 km from edge | 157.7 km: 2 | 10.0 km |
| Tombstone Park | [r9527815](https://www.openstreetmap.org/relation/9527815) | 198 → 80 | 0.3 km | 2105.3 (2103.5) | 262.7 | **outside, 28.3 km** | 88.1 km: 11 | 10.0 km |
| Alvord Desert | [w183794375](https://www.openstreetmap.org/way/183794375) | 150 → 25 | 0.3 km | 104.5 (106.8) | 48.4 | inside, 3.95 km from edge | 9.2 km: 79 | 32.62 km |
| Stanley Park | [w37063023](https://www.openstreetmap.org/way/37063023) | 881 → 13 | 0.15 km | 4.0 (3.9) | 8.9 | inside, 0.53 km from edge | 1.7 km: 96 | 38.59 km |
| Lake O'Hara | [w356689552](https://www.openstreetmap.org/way/356689552) | 291 → 9 | 0.075 km | 0.3 (0.3) | 2.6 | inside, 0.19 km from edge | 0.6 km: 99 | 39.59 km |
| Moraine Lake | [w356877446](https://www.openstreetmap.org/way/356877446) | 120 → 8 | 0.1 km | 0.4 (0.4) | 3.2 | inside, 0.13 km from edge | 0.8 km: 98 | 39.49 km |
| Lake Louise | [r18238904](https://www.openstreetmap.org/relation/18238904) | 344 → 8 | 0.075 km | 0.7 (0.8) | 4.3 | inside, 0.19 km from edge | 1.0 km: 98 | 39.32 km |
| Colchuck Lake | [r17094764](https://www.openstreetmap.org/relation/17094764) | 443 → 8 | 0.1 km | 0.4 (0.4) | 2.9 | inside, 0.2 km from edge | 0.7 km: 98 | 39.54 km |
| Lake Serene | [r16680239](https://www.openstreetmap.org/relation/16680239) | 113 → 7 | 0.05 km | 0.2 (0.2) | 2.0 | inside, 0.15 km from edge | 0.5 km: 99 | 39.68 km |

*farthest correct tap: old score* = the farthest point of the real feature from the current single point, and what a tap there scores today (point decay 40 km). With the ring, any tap inside scores 100; *new decay* is the game's size-calibrated decay for the area (`decay_km(..., area=True)`), used for taps outside the ring.

## Okanagan Lake

- **OSM:** [r2903374](https://www.openstreetmap.org/relation/2903374) (Okanagan Lake; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 9270 raw vertices → 120 points (first == last) after Douglas–Peucker at 0.3 km; max boundary deviation 0.3 km; valid simple polygon after rounding: True.
- **Area:** 344.65 km² (raw OSM outer ring 348.82 km²), perimeter 253.0 km. Category `lake` → kind `area`; decay 40 → 15.52 km.
- **Sanity:** current point 49.9111,-119.5125 is inside the ring (1.07 km from its edge). Farthest point of the feature from it: 50.7 km (scores 28 today; 100 with the ring).
- **Notes:** Relation 2903374 (46 outer ways; 6 islands ignored). A separate 0.01 km² way also named "Okanagan Lake" (w614093993) is a stray fragment and was ignored. 120 points at 0.3 km. The current point (Kelowna) is inside, 1.1 km from shore. Today the far ends score badly: the Vernon Arm tip (50.349,-119.316) is 50.7 km away and scores 28; the Penticton end (49.501,-119.613) is 46.2 km away and scores 32. With the ring, both score 100.

## Kluane Lake

- **OSM:** [r3087341](https://www.openstreetmap.org/relation/3087341) (Kluane Lake; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 4398 raw vertices → 117 points (first == last) after Douglas–Peucker at 0.35 km (GEOS topology-preserving fallback); max boundary deviation 0.352 km; valid simple polygon after rounding: True.
- **Area:** 400.53 km² (raw OSM outer ring 400.76 km²), perimeter 261.5 km. Category `lake` → kind `area`; decay 40 → 14.99 km.
- **Sanity:** current point 61.2639,-138.7444 is inside the ring (1.35 km from its edge). Farthest point of the feature from it: 42.2 km (scores 35 today; 100 with the ring).
- **Notes:** Relation 3087341 (3 outer ways; 14 islands ignored). Plain DP self-intersected in narrows after rounding, so GEOS topology-preserving simplification was used at 0.35 km (117 points). The ring covers the whole lake, both northern arms included. The current point (61.2639,-138.7444) is inside, 1.35 km from shore.

## Maligne Lake

- **OSM:** [r5760911](https://www.openstreetmap.org/relation/5760911) (Maligne Lake; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 4273 raw vertices → 29 points (first == last) after Douglas–Peucker at 0.3 km; max boundary deviation 0.285 km; valid simple polygon after rounding: True.
- **Area:** 19.86 km² (raw OSM outer ring 20.65 km²), perimeter 48.0 km. Category `lake` → kind `area`; decay 40 → 33.01 km.
- **Sanity:** current point 52.6644,-117.5336 is inside the ring (0.58 km from its edge). Farthest point of the feature from it: 11.4 km (scores 75 today; 100 with the ring).
- **Notes:** Relation 5760911 (105 outer ways; 15 islands, Spirit Island among them, ignored so they count as inside). 29 points at 0.3 km. The current point is inside, 0.6 km from shore.

## Lake Crescent

- **OSM:** [r15009108](https://www.openstreetmap.org/relation/15009108) (Lake Crescent; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 1110 raw vertices → 20 points (first == last) after Douglas–Peucker at 0.3 km; max boundary deviation 0.282 km; valid simple polygon after rounding: True.
- **Area:** 20.23 km² (raw OSM outer ring 20.38 km²), perimeter 34.0 km. Category `lake` → kind `area`; decay 40 → 34.87 km.
- **Sanity:** current point 48.0600,-123.8300 is inside the ring (0.81 km from its edge). Farthest point of the feature from it: 7.1 km (scores 84 today; 100 with the ring).
- **Notes:** Relation 15009108. 20 points at 0.3 km. The current point is inside, 0.8 km from shore.

## Crater Lake

- **OSM:** [r147401](https://www.openstreetmap.org/relation/147401) (Crater Lake; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 1072 raw vertices → 13 points (first == last) after Douglas–Peucker at 0.3 km; max boundary deviation 0.3 km; valid simple polygon after rounding: True.
- **Area:** 53.23 km² (raw OSM outer ring 54.33 km²), perimeter 27.5 km. Category `lake` → kind `area`; decay 40 → 35.65 km.
- **Sanity:** current point 42.9415,-122.0988 is inside the ring (3.3 km from its edge). Farthest point of the feature from it: 5.4 km (scores 87 today; 100 with the ring).
- **Notes:** Relation 147401: the lake's water polygon, not the park. Its 15 inner members (Wizard Island, Phantom Ship, rocks) are ignored, so they count as inside. 13 points at 0.3 km; the lake is nearly round. Area 53.2 km² matches the published 53 km². The current point is inside, 3.3 km from the rim.

## Diablo Lake

- **OSM:** [r443823](https://www.openstreetmap.org/relation/443823) (Diablo Lake; `natural=water`, `water=reservoir`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 619 raw vertices → 19 points (first == last) after Douglas–Peucker at 0.15 km; max boundary deviation 0.141 km; valid simple polygon after rounding: True.
- **Area:** 2.8 km² (raw OSM outer ring 2.88 km²), perimeter 15.7 km. Category `lake` → kind `area`; decay 40 → 37.57 km.
- **Sanity:** current point 48.7142,-121.1311 is inside the ring (0.09 km from its edge). Farthest point of the feature from it: 5.0 km (scores 88 today; 100 with the ring).
- **Notes:** Relation 443823 (2 outer, 11 inner). 19 points at 0.15 km. OSM's shoreline gives 2.9 km², less than the often-quoted 910 acres (3.7 km²); the ring follows OSM. The current point is Diablo Dam at the west end, just inside (0.09 km). The narrow gorge arm up toward Ross Dam simplifies to a thin spike, which is expected.

## Garibaldi Lake

- **OSM:** [r2161893](https://www.openstreetmap.org/relation/2161893) (Garibaldi Lake; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 1180 raw vertices → 25 points (first == last) after Douglas–Peucker at 0.15 km; max boundary deviation 0.142 km; valid simple polygon after rounding: True.
- **Area:** 10.4 km² (raw OSM outer ring 10.08 km²), perimeter 17.4 km. Category `lake` → kind `area`; decay 40 → 37.28 km.
- **Sanity:** current point 49.9250,-123.0100 is inside the ring (0.55 km from its edge). Farthest point of the feature from it: 4.1 km (scores 90 today; 100 with the ring).
- **Notes:** Relation 2161893 (2 outer, 2 inner: the Battleship Islands). 25 points at 0.15 km. Lesser Garibaldi Lake, a separate water body, is not included. The current point is inside, 0.55 km from shore.

## San Juan Island

- **OSM:** [r3958317](https://www.openstreetmap.org/relation/3958317) (San Juan Island; `place=island`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 4308 raw vertices → 74 points (first == last) after Douglas–Peucker at 0.3 km (GEOS topology-preserving fallback); max boundary deviation 0.293 km; valid simple polygon after rounding: True.
- **Area:** 144.29 km² (raw OSM outer ring 143.5 km²), perimeter 90.6 km. Category `island` → kind `area`; decay 40 → 27.55 km.
- **Sanity:** current point 48.5333,-123.0833 is inside the ring (4.69 km from its edge). Farthest point of the feature from it: 12.8 km (scores 73 today; 100 with the ring).
- **Notes:** Relation 3958317 (`place=island`, 192 coastline ways). Plain DP self-intersected after rounding, so the topology-preserving simplifier was used: 74 points at 0.3 km. Area 144.3 km² (raw 143.5; published ~143 km²). The current point is inside, 4.7 km from the coast.

## Haida Gwaii

- **OSM:** [r6439518](https://www.openstreetmap.org/relation/6439518) (Haida Gwaii; `place=archipelago`), data as of 2026-07-15T15:22:01Z.
- **Ring:** 2943 raw vertices → 113 points (first == last) after Douglas–Peucker at 1.0 km; max boundary deviation 0.995 km; valid simple polygon after rounding: True.
- **Area:** 13396.17 km² (raw OSM outer ring 13325.35 km²), perimeter 805.9 km. Category `island` → kind `area`; decay 40 → 10.0 km.
- **Sanity:** current point 53.0000,-132.0000 is inside the ring (25.12 km from its edge). Farthest point of the feature from it: 157.7 km (scores 2 today; 100 with the ring).
- **Notes:** Relation 6439518, a `place=archipelago` multipolygon: 4,693 coastline ways forming 3,671 island polygons, 10,011 km² in total (published ~10,180 km²). Using the archipelago relation, rather than every island in a bounding box, keeps out the mainland-coast islands across Hecate Strait (Banks, Porcher, Dundas...). **Construction:** drop the 3,499 islets under 0.05 km² (12 km² in total); buffer each of the other 172 islands by +4 km, union, then shrink by 2.5 km (a morphological closing), and keep the single resulting component's outer ring. The outline therefore sits ~1.5 km offshore (the requested ~1–2 km margin), and every channel or inlet narrower than ~8 km is filled. That merges Graham and Moresby across Skidegate Channel, Kunghit across Houston Stewart Channel and Langara across Parry Passage. Masset Inlet, Masset Sound, Skidegate Inlet, Juan Perez Sound and Rennell Sound all test inside. I preferred this to a plain 1.5 km buffer, which needed a 1.8 km DP tolerance to get under 120 points; the closing simplifies to 113 points at 1.0 km. **Coverage:** 99.998% of all mapped land, tiny islets included, is inside the ring; only 29 rocks (each ≤ 0.03 km²) are outside. The ring encloses 13,396 km², as it includes the filled channels and the 1.5 km margin. The current point (53.0,-132.0, on Moresby) is inside, 25 km from the edge. The farthest correct tap is 158 km away and scores 2 today.

## Tombstone Park

- **OSM:** [r9527815](https://www.openstreetmap.org/relation/9527815) (Tombstone Territorial Park; `leisure=nature_reserve`, `boundary=national_park`, `protect_class=2`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 198 raw vertices → 80 points (first == last) after Douglas–Peucker at 0.3 km; max boundary deviation 0.299 km; valid simple polygon after rounding: True.
- **Area:** 2105.28 km² (raw OSM outer ring 2103.54 km²), perimeter 262.7 km. Category `poi` → kind `area`; decay 40 → 10.0 km.
- **Sanity:** current point 64.0829,-138.5109 is **OUTSIDE** the ring (28.3 km from its edge). Farthest point of the feature from it: 88.1 km (scores 11 today; 100 with the ring).
- **Notes:** Relation 9527815, "Tombstone Territorial Park" (`boundary=national_park`, a single 198-vertex outer way). 80 points at 0.3 km; the boundary is mostly long straight segments. 2,105 km², close to the published ~2,200 km². **The current point is wrong:** 64.0829,-138.5109 is 28.3 km outside the park. It is about 21 km south of the park's southernmost latitude (64.27°N), near the south end of the Dempster Highway, and 36.8 km from Tombstone Mountain. The ring replaces it with the actual park.

## Alvord Desert

- **OSM:** [w183794375](https://www.openstreetmap.org/way/183794375) (Alvord Desert; `natural=mud`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 150 raw vertices → 25 points (first == last) after Douglas–Peucker at 0.3 km; max boundary deviation 0.292 km; valid simple polygon after rounding: True.
- **Area:** 104.53 km² (raw OSM outer ring 106.8 km²), perimeter 48.4 km. Category `poi` → kind `area`; decay 40 → 32.62 km.
- **Sanity:** current point 42.5377,-118.4651 is inside the ring (3.95 km from its edge). Farthest point of the feature from it: 9.2 km (scores 79 today; 100 with the ring).
- **Notes:** Way 183794375, tagged `natural=mud` and named "Alvord Desert": OSM's polygon for the playa (dry lakebed) itself. 25 points at 0.3 km; 104.5 km² (raw 106.8). The current point is inside, 3.95 km from the edge. Not used: Alvord Lake (w183794567, the separate seasonal lake to the south-west) and the much larger Alvord Desert / East Alvord Wilderness Study Area polygons (r6077379, r6077403), which are administrative boundaries.

## Stanley Park

- **OSM:** [w37063023](https://www.openstreetmap.org/way/37063023) (Stanley Park; `leisure=park`, `boundary=protected_area`, `protect_class=22`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 881 raw vertices → 13 points (first == last) after Douglas–Peucker at 0.15 km; max boundary deviation 0.146 km; valid simple polygon after rounding: True.
- **Area:** 3.98 km² (raw OSM outer ring 3.9 km²), perimeter 8.9 km. Category `poi` → kind `area`; decay 40 → 38.59 km.
- **Sanity:** current point 49.3000,-123.1400 is inside the ring (0.53 km from its edge). Farthest point of the feature from it: 1.7 km (scores 96 today; 100 with the ring).
- **Notes:** Way 37063023 (`leisure=park`, `boundary=protected_area`). 13 points at 0.15 km; 3.98 km², matching the published ~400 ha. The current point is inside.

## Lake O'Hara

- **OSM:** [w356689552](https://www.openstreetmap.org/way/356689552) (Lake O'Hara; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 291 raw vertices → 9 points (first == last) after Douglas–Peucker at 0.075 km; max boundary deviation 0.074 km; valid simple polygon after rounding: True.
- **Area:** 0.29 km² (raw OSM outer ring 0.3 km²), perimeter 2.6 km. Category `lake` → kind `area`; decay 40 → 39.59 km.
- **Sanity:** current point 51.3559,-116.3304 is inside the ring (0.19 km from its edge). Farthest point of the feature from it: 0.6 km (scores 99 today; 100 with the ring).
- **Notes:** Way 356689552. 9 points at 0.075 km. The current point is inside. At this size the change barely affects scoring (decay stays ~39.6 km).

## Moraine Lake

- **OSM:** [w356877446](https://www.openstreetmap.org/way/356877446) (Moraine Lake; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 120 raw vertices → 8 points (first == last) after Douglas–Peucker at 0.1 km; max boundary deviation 0.091 km; valid simple polygon after rounding: True.
- **Area:** 0.42 km² (raw OSM outer ring 0.39 km²), perimeter 3.2 km. Category `lake` → kind `area`; decay 40 → 39.49 km.
- **Sanity:** current point 51.3225,-116.1856 is inside the ring (0.13 km from its edge). Farthest point of the feature from it: 0.8 km (scores 98 today; 100 with the ring).
- **Notes:** Way 356877446. 8 points at 0.1 km. The current point is inside.

## Lake Louise

- **OSM:** [r18238904](https://www.openstreetmap.org/relation/18238904) (Lake Louise; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 344 raw vertices → 8 points (first == last) after Douglas–Peucker at 0.075 km; max boundary deviation 0.071 km; valid simple polygon after rounding: True.
- **Area:** 0.71 km² (raw OSM outer ring 0.79 km²), perimeter 4.3 km. Category `lake` → kind `area`; decay 40 → 39.32 km.
- **Sanity:** current point 51.4117,-116.2281 is inside the ring (0.19 km from its edge). Farthest point of the feature from it: 1.0 km (scores 98 today; 100 with the ring).
- **Notes:** Relation 18238904: the lake, not the hamlet. 8 points at 0.075 km. The current point is inside.

## Colchuck Lake

- **OSM:** [r17094764](https://www.openstreetmap.org/relation/17094764) (Colchuck Lake; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 443 raw vertices → 8 points (first == last) after Douglas–Peucker at 0.1 km; max boundary deviation 0.082 km; valid simple polygon after rounding: True.
- **Area:** 0.39 km² (raw OSM outer ring 0.37 km²), perimeter 2.9 km. Category `lake` → kind `area`; decay 40 → 39.54 km.
- **Sanity:** current point 47.4922,-120.8331 is inside the ring (0.2 km from its edge). Farthest point of the feature from it: 0.7 km (scores 98 today; 100 with the ring).
- **Notes:** Relation 17094764; Little Colchuck Lake (w310632521) is separate and not included. 8 points at 0.1 km. The current point is inside.

## Lake Serene

- **OSM:** [r16680239](https://www.openstreetmap.org/relation/16680239) (Lake Serene; `natural=water`, `water=lake`), data as of 2026-09-28T09:01:50Z.
- **Ring:** 113 raw vertices → 7 points (first == last) after Douglas–Peucker at 0.05 km; max boundary deviation 0.045 km; valid simple polygon after rounding: True.
- **Area:** 0.22 km² (raw OSM outer ring 0.22 km²), perimeter 2.0 km. Category `lake` → kind `area`; decay 40 → 39.68 km.
- **Sanity:** current point 47.7819,-121.5703 is inside the ring (0.15 km from its edge). Farthest point of the feature from it: 0.5 km (scores 99 today; 100 with the ring).
- **Notes:** Relation 16680239. 7 points at the 0.05 km floor; the lake is only 0.22 km². The current point is inside.

## Skipped: Joffre Lakes

OSM maps Joffre Lakes as three separate water bodies spread over ~3 km: Lower w30492335 (0.11 km²), Middle r9587007
(0.05 km²) and Upper r5507903 (0.25 km²). One ring can't cover all three without taking in the land and forest
between them, so I skipped it as allowed. For reference, the current point (50.3413,-122.4762) is 0.29 km south of
Upper Joffre Lake, not on any of the three. At this size, making it an area would barely change scoring anyway.

## Queries

Discovery (ids; `out tags center`), then two geometry queries:

```
[out:json][timeout:600];
(rel(id:2903374,3087341,5760911,15009108,147401,443823,2161893,3958317,9527815,18238904,17094764,16680239,5507903,9587007);way(id:614093993,183794375,37063023,356689552,356877446,30492335););out geom;
```

```
[out:json][timeout:600];
rel(6439518);out geom;
```

