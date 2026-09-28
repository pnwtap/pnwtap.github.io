# OSM line geometries — notes

Candidate geometries in `data/candidates/osm_lines.csv` (`name,geometry`) to replace the hand-sketched
`geometry` of 18 rows in `data/locations.csv` (names match exactly). Nothing else in the project was edited.

**Source.** OpenStreetMap via the Overpass API — overpass-api.de, with overpass.kumi.systems and (after both
kept returning 504 "server too busy") maps.mail.ru as fallbacks. Fetched 2026-09-28; OSM data timestamps
range 2026-06 … 2026-09 depending on the mirror. © OpenStreetMap contributors, ODbL.

**Method.**
1. One cheap `out tags` discovery query to find relation ids, then one Overpass query per feature (shown under
   each feature; Sea-to-Sky and Duffey Lake share the Hwy 99 query; the Coquihalla needed two more small ones):
   the river's `type=waterway` relation or the road's `type=route` relation, plus its member ways with `out geom`.
2. Rivers keep only member ways with role `main_stream` (side streams, distributaries and the Gorge power
   tunnel dropped; exceptions noted per feature). Roads keep all member ways.
3. Stitching: the kept ways become a graph joined at shared OSM nodes; the line is the shortest path (Dijkstra)
   between the start and end nodes. That orders the ways source→mouth and automatically skips side channels,
   the second carriageway of divided sections, ramps and spurs. Gaps are bridged only where listed.
4. Ends: nearest graph node to the original row's first/last point unless the notes say otherwise
   (full-stem rivers run source→mouth; the Columbia is clipped at 49.0°N).
5. Simplification: Douglas–Peucker in a local sinusoidal km projection (so the tolerance means the same at
   45°N and 64°N), tolerance 0.5–1.0 km, stepped up just enough to keep ≲150 points (1.1 km Columbia,
   1.5 km Fraser); coordinates rounded to 4 dp (~11 m).
6. Validation: a scratch copy of `locations.csv` with these 18 geometries swapped in passes
   `pnwtap.sheet.parse_locations` with bbox, region mask and categories (all rows parse). Every row stays
   `kind == "line"` except Whidbey Island, which becomes an `area` (closed ring, category `island`).

## Summary

| Feature (CSV `name`) | OSM source | pts raw → out | DP tol | length km (old sketch) | max anchor→new line | old sketch's worst miss |
|---|---|---|---|---|---|---|
| Columbia River | [r2183775](https://www.openstreetmap.org/relation/2183775) | 4270 → 141 | 1.1 km | 1153 (951) | 5.36 km | 20.5 km |
| Fraser River | [r5991467](https://www.openstreetmap.org/relation/5991467) | 6109 → 147 | 1.5 km | 1211 (892) | 6.41 km | 47.5 km |
| Skeena River | [r10783922](https://www.openstreetmap.org/relation/10783922) | 5108 → 137 | 0.7 km | 573 (201) | 2.09 km | 11.4 km |
| Skagit River | [r6425328](https://www.openstreetmap.org/relation/6425328) | 1123 → 59 | 0.5 km | 152 (111) | 2.14 km | 6.8 km |
| Skykomish River | [r14650523](https://www.openstreetmap.org/relation/14650523), [r14650593](https://www.openstreetmap.org/relation/14650593) | 654 → 31 | 0.5 km | 65 (57) | 1.61 km | 2.4 km |
| Deschutes River | [r7809705](https://www.openstreetmap.org/relation/7809705) | 4780 → 138 | 0.6 km | 342 (260) | 6.3 km | 13.2 km |
| Yukon River | [r3319121](https://www.openstreetmap.org/relation/3319121) | 1940 → 143 | 0.9 km | 714 (493) | 1.65 km | 70.9 km |
| North Cascades Hwy (SR-20) | [r2644277](https://www.openstreetmap.org/relation/2644277) | 3133 → 45 | 0.5 km | 199 (168) | 1.13 km | 10.8 km |
| US-2 (Stevens Pass Hwy) | [r2307088](https://www.openstreetmap.org/relation/2307088) | 2611 → 40 | 0.5 km | 154 (130) | 1.3 km | 13.7 km |
| Chinook Pass Hwy (SR-410) | [r1728708](https://www.openstreetmap.org/relation/1728708) | 2490 → 30 | 0.5 km | 140 (127) | 7.82 km | 20.7 km |
| Mountain Loop Hwy | [r8328743](https://www.openstreetmap.org/relation/8328743) | 1757 → 21 | 0.5 km | 81 (72) | 1.54 km | 3.8 km |
| Sea-to-Sky Hwy | [r8746146](https://www.openstreetmap.org/relation/8746146), [r8746147](https://www.openstreetmap.org/relation/8746147) | 2995 → 31 | 0.5 km | 126 (114) | 1.04 km | 2.7 km |
| Duffey Lake Rd | [r8746146](https://www.openstreetmap.org/relation/8746146), [r8746147](https://www.openstreetmap.org/relation/8746147) | 1565 → 25 | 0.5 km | 83 (72) | 1.32 km | 5.1 km |
| Coquihalla Hwy | [r417855](https://www.openstreetmap.org/relation/417855), [r20057078](https://www.openstreetmap.org/relation/20057078) | 1940 → 42 | 0.5 km | 189 (167) | 5.79 km | 7.9 km |
| Icefields Parkway | [r15588](https://www.openstreetmap.org/relation/15588), [r8725770](https://www.openstreetmap.org/relation/8725770) | 3114 → 45 | 0.5 km | 225 (210) | 2.58 km | 6.3 km |
| Historic Columbia River Highway | [r1661228](https://www.openstreetmap.org/relation/1661228), [r12219633](https://www.openstreetmap.org/relation/12219633), [r19609957](https://www.openstreetmap.org/relation/19609957) | 3919 → 30 | 0.5 km | 107 (100) | 3.71 km | 4.5 km |
| Lake Chelan | [r446718](https://www.openstreetmap.org/relation/446718) | 608 → 17 | 0.5 km | 81 (73) | 0.84 km | 5.1 km |
| Whidbey Island | [r3954595](https://www.openstreetmap.org/relation/3954595) | 4871 → 74 | 0.5 km | 215 (64) | 0.38 km | n/a |

*max anchor→new line* = the largest distance (game metric, `nearest_point_km`) from any point of the ORIGINAL row to the new geometry. *old sketch's worst miss* = the largest distance from the real (raw OSM) course to the old hand-sketched line, over the stretch the old row covered — i.e. how badly a correct tap used to be scored.

## Columbia River

- **OSM:** [r2183775](https://www.openstreetmap.org/relation/2183775); 58 ways on the final path (58 kept after role/tag filtering).
- **Extent:** 49.0000,-117.6312 → 46.2493,-124.0861 (OSM data as of 2026-09-28T08:15:51Z)
- **Points:** 4270 raw → 141 after Douglas–Peucker at 1.1 km (max deviation from raw OSM 1.094 km), rounded to 4 dp.
- **Length:** 1153.1 km simplified (1191.1 km raw); old sketch 951.1 km. Kind line → line; decay 10.0 → 10.0 km.
- **Sanity (original anchors → new geometry, km):** [0.7, 4.71, 0.9, 0.16, 0.49, 1.7, 0.07, 0.33, 0.85, 1.23, 0.31, 5.36, 0.31, 2.93, 0.7, 0.99, 1.06, 0.77, 0.24, 0.15, 1.0, 3.19] — max **5.36 km** at 46.6300,-119.5500.
- **Old sketch's worst miss:** 20.5 km (real course at 48.1515,-119.1307).
- **Notes:** US part only, per the brief: the main stem is clipped where it crosses 49.0°N (the BC border, ~16 km upstream of Northport; a point is interpolated on the border) and runs to the end of OSM's main stem at the bar between the jetties (46.2493,-124.0861), ~20 km past Astoria. Through the reservoirs (Roosevelt, Rufus Woods, Wanapum, Wallula, …) OSM's main_stream follows the old channel. **Far anchors are the old sketch's fault:** (46.63,-119.55) lies inside the Hanford Site ~5 km south of the river, because the old line cut the corner of the Hanford Reach bend (the river swings NE to 46.73,-119.51 and back). (48.6108,-118.0558) is Kettle Falls *town*, which sits on a bench ~4.7 km east of Lake Roosevelt's channel. Astoria (3.2 km) is the town waterfront vs. the mid-estuary channel. The old sketch's worst miss (20.5 km, 48.15,-119.13) is where it went straight from Grand Coulee Dam to Chief Joseph Dam across the northward loop of Rufus Woods Lake.

```
[out:json][timeout:300];
rel(2183775);out body;way(r)(45.4,-124.3,49.05,-116.8);out geom;
```

## Fraser River

- **OSM:** [r5991467](https://www.openstreetmap.org/relation/5991467); 82 ways on the final path (82 kept after role/tag filtering).
- **Extent:** 52.5258,-118.3143 → 49.1210,-123.1971 (OSM data as of 2026-07-15T15:22:01Z)
- **Points:** 6109 raw → 147 after Douglas–Peucker at 1.5 km (max deviation from raw OSM 1.5 km), rounded to 4 dp.
- **Length:** 1211.4 km simplified (1404.0 km raw); old sketch 892.0 km. Kind line → line; decay 10.0 → 10.0 km.
- **Sanity (original anchors → new geometry, km):** [0.97, 2.16, 1.79, 0.27, 0.02, 0.52, 1.01, 6.41] — max **6.41 km** at 49.1778,-123.2125.
- **Old sketch's worst miss:** 47.5 km (real course at 54.2188,-122.1491).
- **Notes:** Full main stem, from the source below Fraser Pass (52.5258,-118.3143), ~130 km of river upstream of the old start at Tête Jaune Cache, up the Rocky Mountain Trench past McBride, round the big northern bend (to 54.26°N) to Prince George, then the canyon, Hope and the lower valley to the end of OSM's main stem at Garry Point, Steveston. **Arm choice:** OSM gives the Main (South) Arm role `main_stream`; the North Arm is a `distributary`, so the line follows the Main Arm. The only far anchor is the old mouth point (49.1778,-123.2125). It is 0.8 km from the mouth of the *Middle* Arm (Morey Channel, between Sea Island and Lulu Island), 4.8 km from the North Arm and 6.4 km from the Main Arm line. Neither the anchor nor the line is wrong. It is an arm choice; say if you'd rather end on the North Arm. At 1.0 km tolerance this would be 239 points, so I used 1.5 km (147 points). The old sketch missed by up to 47.5 km (54.22,-122.15): its straight Tête Jaune → Prince George segment skipped the whole trench and the northern bend.

```
[out:json][timeout:300];
rel(5991467);out body;way(r);out geom;
```

## Skeena River

- **OSM:** [r10783922](https://www.openstreetmap.org/relation/10783922); 13 ways on the final path (13 kept after role/tag filtering).
- **Extent:** 57.1119,-128.6744 → 54.1348,-130.1027 (OSM data as of 2026-06-01T08:52:28Z)
- **Points:** 5108 raw → 137 after Douglas–Peucker at 0.7 km (max deviation from raw OSM 0.694 km), rounded to 4 dp.
- **Length:** 572.6 km simplified (621.4 km raw); old sketch 200.8 km. Kind line → line; decay 11.48 → 10.0 km.
- **Sanity (original anchors → new geometry, km):** [0.36, 0.25, 2.09, 1.48, 1.64] — max **2.09 km** at 54.5164,-128.5997.
- **Old sketch's worst miss:** 11.4 km (real course at 54.9642,-128.3931).
- **Notes:** Full stem, from the source in the Skeena Mountains (57.1119,-128.6744), which adds ~350 km of river above the old start at Hazelton, to the end of OSM's main stem in the estuary (54.1348,-130.1027), ~16 km SE of Port Edward. All five old anchors are within 2.1 km. The old sketch missed by up to 11.4 km near Cedarvale (54.96,-128.39).

```
[out:json][timeout:300];
rel(10783922);out body;way(r);out geom;
```

## Skagit River

- **OSM:** [r6425328](https://www.openstreetmap.org/relation/6425328); 18 ways on the final path (32 kept after role/tag filtering).
- **Extent:** 48.7322,-121.0676 → 48.3094,-122.3934 (OSM data as of 2026-09-28T08:20:51Z)
- **Points:** 1123 raw → 59 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.493 km), rounded to 4 dp.
- **Length:** 152.0 km simplified (164.3 km raw); old sketch 111.1 km. Kind line → line; decay 18.03 → 14.39 km.
- **Sanity (original anchors → new geometry, km):** [0.05, 0.16, 0.13, 1.28, 0.88, 2.04, 2.14, 0.17] — max **2.14 km** at 48.4203,-122.3117.
- **Old sketch's worst miss:** 6.8 km (real course at 48.4781,-121.6434).
- **Gaps bridged:** 0.08 km 48.3380,-122.3495→48.3386,-122.3493
- **Notes:** Starts at Ross Dam (the old start) and runs through Diablo and Gorge lakes, Newhalem, Marblemount, Concrete, Sedro-Woolley and Mount Vernon to Skagit Bay. The Gorge Power Tunnel (`waterway=pressurised`) is excluded so the line stays in the gorge. **Below the Fir Island fork** (48.388,-122.366, where the old row ended), OSM's `main_stream` continues down the South Fork Skagit River (role `distributary`, included for this purpose) and then Freshwater Slough to the bay at 48.3094,-122.3934. I bridged an 80 m gap between two ways there that don't share a node. The North Fork, ending at 48.371,-122.492, would be the alternative. Max anchor 2.1 km at (48.4203,-122.3117), which is in east Mount Vernon; the river is at about -122.340 at that latitude, along the west edge of downtown.

```
[out:json][timeout:300];
rel(6425328);out body;way(r);out geom;
```

## Skykomish River

- **OSM:** [r14650523](https://www.openstreetmap.org/relation/14650523), [r14650593](https://www.openstreetmap.org/relation/14650593); 6 ways on the final path (6 kept after role/tag filtering).
- **Extent:** 47.7106,-121.3586 → 47.8220,-122.0343 (OSM data as of 2026-09-28T08:30:05Z)
- **Points:** 654 raw → 31 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.492 km), rounded to 4 dp.
- **Length:** 65.4 km simplified (72.8 km raw); old sketch 57.2 km. Kind line → line; decay 25.74 → 24.28 km.
- **Sanity (original anchors → new geometry, km):** [0.04, 0.21, 1.61, 0.36, 0.61, 1.31] — max **1.61 km** at 47.8208,-121.5539.
- **Old sketch's worst miss:** 2.4 km (real course at 47.8384,-121.8498).
- **Notes:** Starts on the South Fork at the node nearest Skykomish town, as asked (the South Fork itself begins 5.8 km upstream at the Tye/Foss confluence, 47.705,-121.307). It runs past Baring to Index, where the North Fork joins (47.813,-121.579), then down the Skykomish main stem past Gold Bar, Sultan and Monroe to its end at the Snoqualmie confluence (47.822,-122.034), where the Snohomish begins. The two relations share a node at Index, so no gap. Max anchor 1.6 km at Index, where the anchor is the town rather than the river.

```
[out:json][timeout:300];
rel(id:14650523,14650593);out body;way(r);out geom;
```

## Deschutes River

- **OSM:** [r7809705](https://www.openstreetmap.org/relation/7809705); 37 ways on the final path (41 kept after role/tag filtering).
- **Extent:** 43.9097,-121.7608 → 45.6403,-120.9142 (OSM data as of 2026-09-28T08:33:01Z)
- **Points:** 4780 raw → 138 after Douglas–Peucker at 0.6 km (max deviation from raw OSM 0.585 km), rounded to 4 dp.
- **Length:** 341.6 km simplified (408.0 km raw); old sketch 260.0 km. Kind line → line; decay 10.0 → 10.0 km.
- **Sanity (original anchors → new geometry, km):** [0.34, 0.42, 1.04, 0.44, 0.51, 6.3, 0.36, 0.11] — max **6.3 km** at 44.5891,-121.3650.
- **Old sketch's worst miss:** 13.2 km (real course at 44.8771,-121.0480).
- **Notes:** Full stem, from the outlet of Little Lava Lake (43.9097,-121.7608) south through Crane Prairie and Wickiup reservoirs (OSM's river line runs through both), then north past Sunriver, Bend, Lake Billy Chinook, Lake Simtustus, Warm Springs and Maupin to the Columbia (45.6403,-120.9142). **One far anchor, and the old anchor is wrong:** (44.5891,-121.3650) is 6.3 km from the river. At that latitude the Deschutes arm of Lake Billy Chinook is at about -121.28, so the anchor is ~7 km too far west, out toward the Metolius arm. The old sketch missed by up to 13.2 km between Warm Springs and Maupin (44.88,-121.05).

```
[out:json][timeout:300];
rel(7809705);out body;way(r);out geom;
```

## Yukon River

- **OSM:** [r3319121](https://www.openstreetmap.org/relation/3319121); 9 ways on the final path (12 kept after role/tag filtering).
- **Extent:** 60.4309,-134.2788 → 64.0649,-139.4377 (OSM data as of 2026-09-28T08:44:21Z)
- **Points:** 1940 raw → 143 after Douglas–Peucker at 0.9 km (max deviation from raw OSM 0.901 km), rounded to 4 dp.
- **Length:** 714.2 km simplified (767.3 km raw); old sketch 492.8 km. Kind line → line; decay 10.0 → 10.0 km.
- **Sanity (original anchors → new geometry, km):** [1.65, 0.05, 0.45, 0.44, 1.61, 0.46] — max **1.65 km** at 60.4361,-134.2506.
- **Old sketch's worst miss:** 70.9 km (real course at 63.0145,-139.5070).
- **Notes:** Relation 3319121 is the whole Yukon; only ways inside 59–64.4°N, 141–132°W were fetched. OSM's main stem here runs Atlin River, a Tagish Lake flowline, the Tagish River, a **Marsh Lake flowline**, the river through Whitehorse, a **Lake Laberge flowline**, then Thirty Mile, Carmacks and Fort Selkirk to Dawson. The two lake stretches are `waterway=flowline` centrelines through the lakes. The old row starts mid-Marsh Lake (60.4361,-134.2506), so the line starts at that anchor's projection onto the Marsh Lake flowline (1.65 km away; OSM's lake centreline is a sparse 10-vertex line). It ends at the river node nearest Dawson (0.46 km). Tolerance 0.9 km gives 143 points. The old sketch's worst miss was 70.9 km (63.01,-139.51): it cut straight from Fort Selkirk to Dawson, while the river first swings ~70 km further west toward the White River confluence.

```
[out:json][timeout:300];
rel(3319121);out body;way(r)(59.0,-141.0,64.4,-132.0);out geom;
```

## North Cascades Hwy (SR-20)

- **OSM:** [r2644277](https://www.openstreetmap.org/relation/2644277); 182 ways on the final path (264 kept after role/tag filtering).
- **Extent:** 48.5017,-122.2560 → 48.4722,-120.1779 (OSM data as of 2026-09-28T08:43:20Z)
- **Points:** 3133 raw → 45 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.466 km), rounded to 4 dp.
- **Length:** 199.3 km simplified (207.1 km raw); old sketch 168.2 km. Kind line → line; decay 13.29 → 11.56 km.
- **Sanity (original anchors → new geometry, km):** [0.04, 0.16, 1.13, 0.09, 0.34, 0.04, 0.22, 0.09] — max **1.13 km** at 48.5417,-121.4397.
- **Old sketch's worst miss:** 10.8 km (real course at 48.5979,-120.4360).
- **Notes:** Relation 2644277 (WA SR 20), members inside 48.3–48.85°N, 122.4–120.0°W. Runs from the node nearest the Sedro-Woolley anchor, through Concrete, Marblemount, Newhalem, Diablo, Rainy Pass, Washington Pass and Mazama, to the node nearest the last anchor. **Extent:** the old row's last point (48.4717,-120.1792) is Winthrop (south edge of town), not Twisp, so I matched the row. Running on to Twisp (48.3648,-120.1225) would make it 212 km and 48 points instead of 199 km and 45; say if you want that version. All anchors are within 1.13 km. The old sketch's worst miss was 10.8 km (48.60,-120.44): it went straight from Washington Pass to Winthrop, skipping the road's swing north through Mazama.

```
[out:json][timeout:300];
rel(2644277);out body;way(r)(48.3,-122.4,48.85,-120.0);out geom;
```

## US-2 (Stevens Pass Hwy)

- **OSM:** [r2307088](https://www.openstreetmap.org/relation/2307088); 246 ways on the final path (338 kept after role/tag filtering).
- **Extent:** 47.9795,-122.1858 → 47.5953,-120.6631 (OSM data as of 2026-09-28T08:44:21Z)
- **Points:** 2611 raw → 40 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.439 km), rounded to 4 dp.
- **Length:** 154.2 km simplified (159.6 km raw); old sketch 129.6 km. Kind line → line; decay 16.2 → 14.24 km.
- **Sanity (original anchors → new geometry, km):** [1.18, 0.68, 0.57, 0.01, 1.3, 0.06, 0.09, 0.04] — max **1.3 km** at 47.8208,-121.5539.
- **Old sketch's worst miss:** 13.7 km (real course at 47.7632,-120.7455).
- **Notes:** Relation 2307088 (US 2 in WA); the Montana and Idaho US 2 relations had no members inside the box. Divided sections contribute one carriageway. The line starts at the relation's west end at the I-5 interchange in Everett, 1.2 km east of the anchor, and runs past Snohomish, Monroe, Sultan, Gold Bar, Index, Skykomish, Stevens Pass, Nason Creek, Coles Corner and Tumwater Canyon to the node nearest the Leavenworth anchor. Max anchor 1.3 km at Index (47.8208,-121.5539); the town is off the highway. The old sketch's worst miss was 13.7 km (47.76,-120.75): it went straight from Stevens Pass to Leavenworth, skipping the Nason Creek, Coles Corner and Tumwater Canyon dog-leg.

```
[out:json][timeout:300];
rel(id:1266683,2307082,2307088);out body;way(r)(47.5,-122.3,48.1,-120.5);out geom;
```

## Chinook Pass Hwy (SR-410)

- **OSM:** [r1728708](https://www.openstreetmap.org/relation/1728708); 89 ways on the final path (122 kept after role/tag filtering).
- **Extent:** 47.1988,-121.9932 → 46.7483,-120.7885 (OSM data as of 2026-09-28T08:44:21Z)
- **Points:** 2490 raw → 30 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.493 km), rounded to 4 dp.
- **Length:** 140.2 km simplified (147.8 km raw); old sketch 127.0 km. Kind line → line; decay 16.45 → 15.31 km.
- **Sanity (original anchors → new geometry, km):** [0.38, 0.56, 0.04, 0.12, 7.82] — max **7.82 km** at 46.7261,-120.6911.
- **Old sketch's worst miss:** 20.7 km (real course at 46.9894,-121.0951).
- **Notes:** Relation 1728708 (WA SR 410), members inside 46.6–47.3°N, 122.1–120.5°W. Runs from the node nearest Enumclaw, through Greenwater, Mount Rainier NP (Mather Memorial Parkway), Cayuse Pass and Chinook Pass, then down the American and Naches valleys to where SR 410 ends in OSM: its junction with US 12 at 46.7483,-120.7885. **The last old anchor, Naches town (46.7261,-120.6911), is 7.8 km off because SR 410 doesn't reach Naches;** the last ~8 km into town is US 12. I didn't extend it, since that's a different highway and would need one more query; say if you want it. The old sketch's worst miss was 20.7 km (46.99,-121.10): its straight Chinook Pass → Naches segment cut off the road's run down the American and Naches river valleys.

```
[out:json][timeout:300];
rel(1728708);out body;way(r)(46.6,-122.1,47.3,-120.5);out geom;
```

## Mountain Loop Hwy

- **OSM:** [r8328743](https://www.openstreetmap.org/relation/8328743); 70 ways on the final path (71 kept after role/tag filtering).
- **Extent:** 48.0834,-121.9641 → 48.2525,-121.6014 (OSM data as of 2026-09-28T08:43:20Z)
- **Points:** 1757 raw → 21 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.415 km), rounded to 4 dp.
- **Length:** 80.7 km simplified (85.4 km raw); old sketch 71.8 km. Kind line → line; decay 23.21 → 21.85 km.
- **Sanity (original anchors → new geometry, km):** [0.42, 0.21, 1.54, 0.13, 0.44, 0.13] — max **1.54 km** at 48.0539,-121.5196.
- **Old sketch's worst miss:** 3.8 km (real course at 48.1181,-121.9421).
- **Notes:** Relation 8328743 (Mountain Loop Highway, ref NF 20; 71 ways in one chain). Runs from its start in Granite Falls (N Alder Ave) via Verlot, Barlow Pass and the gravel Sauk River section to its end in Darrington. Max anchor 1.54 km at (48.0539,-121.5196), which is ~1.5 km south of the road near Big Four (the anchor sits off the road, not the line). The old sketch's worst miss was 3.8 km (48.12,-121.94) just out of Granite Falls.

```
[out:json][timeout:300];
rel(8328743);out body;way(r);out geom;
```

## Sea-to-Sky Hwy

- **OSM:** [r8746146](https://www.openstreetmap.org/relation/8746146), [r8746147](https://www.openstreetmap.org/relation/8746147); 322 ways on the final path (681 kept after role/tag filtering).
- **Extent:** 49.3713,-123.2700 → 50.3163,-122.8038 (OSM data as of 2026-09-28T08:42:20Z)
- **Points:** 2995 raw → 31 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.489 km), rounded to 4 dp.
- **Length:** 125.6 km simplified (131.8 km raw); old sketch 114.5 km. Kind line → line; decay 17.67 → 16.58 km.
- **Sanity (original anchors → new geometry, km):** [0.59, 0.41, 1.04, 0.47, 0.3, 0.52] — max **1.04 km** at 49.7017,-123.1589.
- **Old sketch's worst miss:** 2.7 km (real course at 49.9410,-123.1678).
- **Notes:** Hwy 99 relations 8746146 + 8746147, OSM's two *directional* relations for BC 99 (tagged "(South)"/"(North)" but each spanning the whole highway); same query as Duffey Lake Rd. On divided stretches the path uses one carriageway. Runs from the node nearest the Horseshoe Bay anchor (0.59 km) past Lions Bay, Britannia Beach, Squamish, Brandywine Falls and Whistler to the node nearest the Pemberton anchor. Max anchor 1.04 km at Squamish town (49.7017,-123.1589), which lies west of the highway. The old sketch's worst miss was 2.7 km, north of Squamish (49.94,-123.17).

```
[out:json][timeout:300];
rel(id:8746146,8746147);out body;way(r)(49.3,-123.4,50.8,-121.8);out geom;
```

## Duffey Lake Rd

- **OSM:** [r8746146](https://www.openstreetmap.org/relation/8746146), [r8746147](https://www.openstreetmap.org/relation/8746147); 54 ways on the final path (681 kept after role/tag filtering).
- **Extent:** 50.3164,-122.7174 → 50.6920,-121.9214 (OSM data as of 2026-09-28T08:42:20Z)
- **Points:** 1565 raw → 25 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.49 km), rounded to 4 dp.
- **Length:** 83.4 km simplified (92.2 km raw); old sketch 71.6 km. Kind line → line; decay 23.24 → 21.46 km.
- **Sanity (original anchors → new geometry, km):** [0.03, 0.5, 1.32, 0.84] — max **1.32 km** at 50.4042,-122.3417.
- **Old sketch's worst miss:** 5.1 km (real course at 50.3021,-122.5741).
- **Notes:** Hwy 99 relations 8746146 + 8746147 (the two directional relations; same query as Sea-to-Sky). Runs from Mount Currie (0.03 km) past Lillooet Lake's north end, over Cayoosh Pass, past Duffey Lake and down Cayoosh Creek to the Fraser. There it crosses the Bridge of the Twenty-Three Camels and ends ~1 km up the east bank, at the Hwy 99 node nearest Lillooet town (0.84 km; Hwy 99 doesn't enter the town). The old sketch's worst miss was 5.1 km (50.30,-122.57), where the road dips south along Lillooet Lake.

```
[out:json][timeout:300];
rel(id:8746146,8746147);out body;way(r)(49.3,-123.4,50.8,-121.8);out geom;
```

## Coquihalla Hwy

- **OSM:** [r417855](https://www.openstreetmap.org/relation/417855), [r20057078](https://www.openstreetmap.org/relation/20057078); 133 ways on the final path (212 kept after role/tag filtering).
- **Extent:** 49.3617,-121.3627 → 50.6620,-120.3410 (OSM data as of 2026-09-28T08:41:20Z, 2026-09-28T08:50:36Z)
- **Points:** 1940 raw → 42 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.497 km), rounded to 4 dp.
- **Length:** 188.7 km simplified (194.2 km raw); old sketch 166.9 km. Kind line → line; decay 13.38 → 12.1 km.
- **Sanity (original anchors → new geometry, km):** [5.79, 0.02, 2.18, 1.54] — max **5.79 km** at 49.3800,-121.4414.
- **Old sketch's worst miss:** 7.9 km (real course at 50.6510,-120.4847).
- **Notes:** Uses relation 20057078, the northbound-carriageway Coquihalla; the two carriageway relations share no nodes, so one is used. Also relation 417855, BC Hwy 5 north of Kamloops, whose first stretch is the Hwy 1/5/97 concurrency through Kamloops, starting at the exact node where the Coquihalla ends. The line starts at Hwy 5's southern terminus, the Hwy 3 junction east of Hope (49.3617,-121.3627). OSM has no Hwy 5 any closer to Hope: an extra query for every `ref`-5 highway way around Hope found only the Coquihalla itself. It then runs over Coquihalla Summit (Zopkios), past Merritt and down into Kamloops, where the Coquihalla proper ends at the Hwy 1 interchange (50.6662,-120.4417). From there it follows Hwy 5 ~7 km along the concurrency to the node nearest downtown (50.6620,-120.3410, 1.54 km from the anchor), matching the brief's "Hwy 5, Hope → Kamloops". Trim at 50.6662,-120.4417 if you want the named Coquihalla only. **The first anchor (Hope town, 49.3800,-121.4414) is 5.8 km off because Hwy 5 starts ~6 km east of town;** the road into Hope is Hwy 3 only, so the anchor sits beyond the highway, not on it. The old sketch's worst miss was 7.9 km (50.65,-120.48), on the descent into Kamloops.

```
[out:json][timeout:300];
rel(id:20056841,20057078);out body;way(r);out geom;
[out:json][timeout:300];
rel(417855);out body;way(r)(49.30,-121.50,50.75,-120.20);out geom;
// check only, no ways used (confirms no ref-5 highway west of the Hwy 3 junction):
[out:json][timeout:300];
way["highway"~"^(motorway|trunk|primary|motorway_link|trunk_link)$"]["ref"~"(^|;) *(BC )?5 *(;|$)"](49.33,-121.47,49.40,-121.33);out geom;
```

## Icefields Parkway

- **OSM:** [r15588](https://www.openstreetmap.org/relation/15588), [r8725770](https://www.openstreetmap.org/relation/8725770); 150 ways on the final path (201 kept after role/tag filtering).
- **Extent:** 51.4256,-116.1735 → 52.8665,-118.0934 (OSM data as of 2026-09-28T08:41:20Z)
- **Points:** 3114 raw → 45 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.505 km), rounded to 4 dp.
- **Length:** 224.6 km simplified (230.0 km raw); old sketch 209.5 km. Kind line → line; decay 11.08 → 10.43 km.
- **Sanity (original anchors → new geometry, km):** [0.23, 0.41, 0.14, 0.06, 2.58, 0.51, 0.22, 1.05] — max **2.58 km** at 52.1986,-117.2436.
- **Old sketch's worst miss:** 6.3 km (real course at 52.4333,-117.4100).
- **Gaps bridged:** 0.01 km 52.6178,-117.8470→52.6177,-117.8469; 0.03 km 52.4498,-117.4429→52.4500,-117.4431
- **Notes:** Relations 15588 (Icefields Parkway) + 8725770 (Alberta Hwy 93; its members in the box also include the TCH concurrency at Lake Louise). I bridged two 10–30 m gaps where ways touch but share no node (52.4500,-117.4431 and 52.6178,-117.8469). Runs from the node nearest the Lake Louise anchor (on TCH/93 by the village, 0.23 km) over Bow Summit, past the Columbia Icefield and down the Sunwapta and Athabasca valleys to the Parkway's north end at Hwy 16 south of Jasper (52.8665,-118.0934). Raw length 230 km, close to the official 232 km. Max anchor 2.58 km at (52.1986,-117.2436): that point is on the Athabasca Glacier, not the road, so the anchor is off. The old sketch's worst miss was 6.3 km (52.43,-117.41), in the Sunwapta valley.

```
[out:json][timeout:300];
rel(id:15588,8725770);out body;way(r)(51.3,-118.2,53.0,-116.0);out geom;
```

## Historic Columbia River Highway

- **OSM:** [r1661228](https://www.openstreetmap.org/relation/1661228), [r12219633](https://www.openstreetmap.org/relation/12219633), [r19609957](https://www.openstreetmap.org/relation/19609957); 229 ways on the final path (264 kept after role/tag filtering).
- **Extent:** 45.5382,-122.3774 → 45.6277,-121.2146 (OSM data as of 2026-09-28T08:38:21Z)
- **Points:** 3919 raw → 30 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.488 km), rounded to 4 dp.
- **Length:** 106.6 km simplified (117.9 km raw); old sketch 100.3 km. Kind line → line; decay 19.25 → 18.52 km.
- **Sanity (original anchors → new geometry, km):** [0.78, 0.02, 0.44, 0.83, 0.05, 0.02, 0.19, 3.71] — max **3.71 km** at 45.6017,-121.1847.
- **Old sketch's worst miss:** 4.5 km (real course at 45.6623,-121.2205).
- **Gaps bridged:** 0.02 km 45.6900,-121.7736→45.6899,-121.7734; 6.57 km 45.7102,-121.5554→45.6993,-121.6386
- **Notes:** The union of three OSM relations: 12219633 (the ODOT legislative "Historic Columbia River Highway", No. 100), 19609957 (the scenic byway) and 1661228 (the HCRH State Trail bike route, which covers the car-free trail segments). The line runs the drivable old road Troutdale → Corbett → Crown Point → Multnomah Falls → Ainsworth, then the State Trail segments via Cascade Locks to Wyeth and Viento. **Between Viento and Hood River no HCRH exists** (I-84 obliterated it and the trail isn't built), so a straight 6.57 km bridge (penalised in the routing, used only because nothing else connects) spans 45.6993,-121.6386 → 45.7102,-121.5554 along the shore. After that it follows the Twin Tunnels trail to Mosier and the Rowena Loops road to where the routes end, on West 6th St (US 30) at the west edge of The Dalles (45.6277,-121.2146). I also closed one 20 m node gap near Wyeth. Max anchor 3.71 km at downtown The Dalles (45.6017,-121.1847), which is ~3.7 km past the end of the OSM route; the line is right and the anchor is a little beyond it. The old sketch's worst miss was 4.5 km (45.66,-121.22), east of Rowena.

```
[out:json][timeout:300];
rel(id:12219633,19609957,1661228);out body;way(r);out geom;
```

## Lake Chelan

- **OSM:** [r446718](https://www.openstreetmap.org/relation/446718).
- **Extent:** 47.8350,-120.0141 → 48.3198,-120.6776 (OSM data as of 2026-09-28T08:38:21Z)
- **Points:** 608 raw → 17 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.478 km), rounded to 4 dp.
- **Length:** 80.9 km simplified (83.3 km raw); old sketch 72.6 km. Kind line → line; decay 23.08 → 21.82 km.
- **Sanity (original anchors → new geometry, km):** [0.26, 0.82, 0.7, 0.84] — max **0.84 km** at 48.3094,-120.6553.
- **Old sketch's worst miss:** 5.1 km (real course at 47.9866,-120.2161).
- **Notes:** OSM lake relation 446718 (`natural=water`, `water=reservoir`; 54 outer and 6 inner ways; islands ignored). The centreline is a discrete medial axis: the shoreline was pre-simplified at 50 m, densified every 200 m, and the Voronoi edges lying inside the lake kept. It is the shortest path along those edges between the lake's SE-most shore point (47.8349,-120.0120, Chelan/dam end) and NW-most (48.3223,-120.6802, head of the lake at Stehekin). 608 medial vertices → 17 points (DP 0.5 km), 80.9 km, matching the lake's ~81 km (50.5 mi) length. All 17 vertices are in the lake, and 99% of the line's length is over water (~0.7 km in total clips shore corners at bends). The line follows the bend at Manson/Wapato Point. It is still an open line, so it stays a line feature. All four old anchors are within 0.84 km. The old sketch's worst miss was 5.1 km (47.99,-120.22), where it cut straight from Manson to Lucerne across the lake's curve.

```
[out:json][timeout:300];
(rel["natural"="water"]["name"="Lake Chelan"](47.7,-120.8,48.4,-119.9);way["natural"="water"]["name"="Lake Chelan"](47.7,-120.8,48.4,-119.9););out geom;
```

## Whidbey Island

- **OSM:** [r3954595](https://www.openstreetmap.org/relation/3954595).
- **Extent:** 48.0870,-122.5200 → 48.0870,-122.5200 (OSM data as of 2026-09-28T08:37:16Z)
- **Points:** 4871 raw → 74 after Douglas–Peucker at 0.5 km (max deviation from raw OSM 0.495 km), rounded to 4 dp.
- **Length:** 215.4 km simplified (248.4 km raw); old sketch 63.5 km. Kind line → area; decay 24.61 → 17.04 km.
- **Sanity (original anchors → new geometry, km):** [0.28, 0.09, 0.0, 0.0, 0.38] — max **0.38 km** at 47.9739,-122.3469.
- **Notes:** OSM island relation 3954595 (`place=island` multipolygon; 108 outer coastline ways). Built one polygon with `polygonize` (4,871 vertices). Simplified with Douglas–Peucker at 0.5 km, run as two open halves so the 0.5 km bound holds (max deviation 0.495 km), and checked it is still a simple ring. Result: 74 points, first == last, 215 km perimeter, including Penn Cove, Holmes Harbor and Useless Bay. It becomes an **area** (category `island`, closed ring): taps inside score 100. Old spine points: 2 of 5 are inside; the other three sit on the shore just outside the simplified outline (Deception Pass 0.28 km, Oak Harbor side 0.09 km, Clinton ferry 0.38 km).

```
[out:json][timeout:300];
(rel["place"="island"]["name"="Whidbey Island"](47.8,-122.9,48.5,-122.2);way["place"="island"]["name"="Whidbey Island"](47.8,-122.9,48.5,-122.2););out geom;
```

