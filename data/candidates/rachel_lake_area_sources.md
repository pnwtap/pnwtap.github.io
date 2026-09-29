# Rachel Lake / Box Ridge area — sources (added 2026-09-28)

Six rows requested by the user: Box Ridge, Hibox Mountain, Alta Mountain, Rachel Lake, Lila Lake, Rampart Lakes.
Each was researched, then independently fact-checked. Lake areas are WDFW acreage converted to km²
(Rachel 25.10 ac, Lila 2.80 ac); the card shows them in acres. Rachel Lake is medium, the rest hard.

## Identification notes (peaks)

"The box mountain ridge" is almost certainly BOX RIDGE, the official USGS GNIS name (feature 1516904). I'm highly confident. It is the ridge whose summits carry the "box" names: Hibox Mountain (named as its high point), "Lobox Mountain" (Pt 6032, an unofficial name) and "Nobox". Evidence:
(a) The GNIS record for Hibox (1529153) says: "At the NW end of Box Ridge ... 8 km (5 mi) ENE of Snoqualmie Pass".
(b) Wikipedia's Hibox article says the name comes from its position as the high point of Box Ridge.
(c) Peakbagger's Lobox page (pid 2152, read via search snippet because the site is behind Cloudflare) names three notable points on Box Ridge: Lobox, Hibox and Nobox.
(d) willhiteweb calls Hibox the highest point on Box Ridge, with Lobox (6,032 ft) on the same ridge.
(e) OSM has a natural=ridge way named Box Ridge (way 1249966395, gnis 1516904). It maps only the southern, forested half, from 47.4085,-121.2665 down to about 47.3675,-121.2475 near Kachess Lake.
(f) The GNIS "true shape" polygon for Box Ridge, pulled from the GNIS GraphQL API, is a thin band from the Kachess Lake shore (47.3625,-121.2465) NW through Lobox and Hibox. It ends at the junction with the Alta Pass / Alta Mountain ridges (tips at 47.4445,-121.3145 and 47.4399,-121.3237). GNIS gives the ridge an elevation of 1991 m, which is Hibox's height.

So the ridge is the NE wall of Box Canyon, splitting Box Canyon Creek (Rachel Lake side, to the SW) from the Mineral Creek / Park Lakes side (NE). Both drain to Kachess Lake. I found no peak or ridge named "Box Mountain" anywhere nearby. The phrasing "the ridge itself, hibox as a separate entry" also fits, since Hibox is Box Ridge's high point.

Alternatives, all less likely:
1. Rampart Ridge (GNIS 1524859; OSM way 980376732). This is the crest the Rachel Lake trail tops out on, the west wall above Rachel and Rampart Lakes, but it has no "box" in the name. If the user meant it, here is the OSM crest simplified to 15 points (about 4.3 km): 47.4299,-121.3285; 47.4271,-121.3319; 47.4241,-121.3345; 47.4207,-121.3351; 47.4208,-121.3410; 47.4206,-121.3422; 47.4199,-121.3425; 47.4194,-121.3437; 47.4188,-121.3443; 47.4153,-121.3449; 47.4121,-121.3448; 47.4081,-121.3427; 47.4055,-121.3421; 47.4036,-121.3477; 47.4007,-121.3501.
2. Only the rocky Hibox–Lobox section.
3. A "Box Canyon" horseshoe (Rampart Ridge – Alta – Hibox). No source names this.

Proposed row name: "Box Ridge". Hibox Mountain and Alta Mountain are separate rows. No name collisions in locations.csv, curated.csv or the candidates CSVs.

Summit positions (two or more sources each):
- Hibox: Wikipedia/peakbagger 47.431772,-121.300756; OSM (GNIS-sourced) 47.4317799,-121.30065; PeakVisor 47.431575,-121.30088; USGS 3DEP 1 m lidar highest pixel 47.43175,-121.30085. Row uses 47.4318,-121.3008.
- Alta: Wikipedia 47.441131,-121.331964; OSM 47.4410071,-121.331956; PeakVisor 47.440908,-121.331935; lidar 47.44106,-121.33196. Row uses 47.4411,-121.3320.
- Relative to the lakes (OSM centres): Rachel Lake 47.4199,-121.3311, Lila Lake 47.4314,-121.3254, Rampart Lakes 47.4176,-121.3396. Alta is about 2.4 km north of Rachel Lake; Hibox is about 2.5 km NE of it.

Context: the WTA Rachel Lake page says the trail closed 7.30.26 because of the Three Queens Fire. None of the blurbs depend on this.


### Fact-check changes

- Box Ridge geometry, NW end: extended the line about 0.7 km west, from the Box Canyon / Mineral / Gold creek triple junction (47.4400,-121.3148) along the crest to the saddle below Alta's east ridge (47.4398,-121.3236). Three reasons: GNIS's true-shape polygon includes this arm; Box Canyon Creek heads directly beneath it; and peakbagger places a third Box Ridge point, 'Nobox', between Hibox and Alta. The ridge line now reaches toward Alta, which fits how the user grouped the features. Alta itself stays out of the line.
- Box Ridge geometry, south of Lobox: fixed a corner cut. The segment 47.4154,-121.2734 -> 47.4085,-121.2667 ran up to about 200 m down the SW flank and bypassed a 1716 m knob on the Box Canyon / Mineral Creek divide. I replaced it with 47.4158,-121.2721; 47.4168,-121.2711; 47.4127,-121.2707. I also moved 47.3727,-121.2488 to 47.3740,-121.2508, because the old point sat about 100 m east of the divide.
- Box Ridge geometry, other edits: added 47.4314,-121.2995 where the crest leaves Hibox eastward. Changed the Lobox vertex to 47.4241,-121.2832 to match the lidar high point at 47.42405. Dropped 47.4245,-121.2867 and 47.3751,-121.2503, which were redundant at a 40-50 m tolerance. Net result: 22 points / 10.7 km became 25 points / 11.7 km. The line is simple and 100% inside the GNIS polygon. Its distance to the independently computed drainage divide improved from median 17 / p90 69 / max 205 m to median 14 / p90 39 / max 112 m.
- Hibox facts: removed 'classic: Hibox climbers' path, Class 3'. FACTS_SPEC limits classic to crags, formations and big peaks, and asks for a signature route. This is an unnamed boot path, and the sources can't agree on the ridge (east vs southeast). Comparable Snoqualmie-area rows (Granite Mountain, Snoqualmie Mountain, Red Mountain, Mount Si, Mt Daniel) have no classic. The route now appears only in the blurb.
- Alta facts: removed 'classic: South Ridge, Class 2' for the same reason; a Class 2 boot path is not a signature climb. The route is kept in the blurb.
- Hibox blurb rewritten. 'Up loose rock' rested on one peakery trip-report remark; the havetent, mountainflamingo and willhiteweb route descriptions don't say it. 'Relentlessly steep' overstated the sources. 'Named as the high point' read awkwardly. The new text uses what the sources support: a steep, rooty path (havetent) and a Class 3 finish on the east ridge (mountainflamingo, havetent). It is also shorter: 154 -> 148 chars. Existing blurbs have a median of 110 and a max of 153.
- Alta blurb rewritten. 'From the Lila Lake junction' was ambiguous: WTA describes two junctions, and the Alta path leaves the Lila Lake trail at a cairn 0.3 mi past the Rampart/Lila fork. It now says 'off the Lila Lake trail'. I added the narrow (WTA: knife-edge) south ridge and shortened it from 153 to 137 chars.
- Sources: added an independent check for each row. I re-queried GNIS names, polygons and descriptions via GraphQL, fetched my own 3DEP lidar summits (Hibox 1995.85 m at 47.43177,-121.30084; Alta 1912.31 m at 47.44100,-121.33196), and cited the OSM Alta Mountain Trail and Hibox climbers' trail ways, the OSM Box Canyon Creek and Mineral Creek ways, and the onehikeaweek Lobox page and WTA route text.

## Identification notes (lakes)

Scope: I handled only my three rows (Rachel Lake, Lila Lake, Rampart Lakes). The ridge, Hibox and Alta belong to other agents. One thing that may help them: OSM has "Rampart Ridge" as a natural=ridge way, w980376732 (GNIS 1524859). Its crest runs from 47.4299,-121.3285 (just SW of Lila Lake) south past the west side of Rachel Lake, turns west along about 47.4208, then runs south along about -121.3445 to 47.4007,-121.3501. OSM also has Hibox Mountain as n356547169 (47.4318,-121.3007, GNIS 1529153), Alta Mountain as n356544086 (47.4410,-121.3320, GNIS 1515838) and Lobox Mountain as n13825672125. There is also a separate OSM "Box Ridge" way (w1249966395, GNIS 1516904) at about 47.388,-121.257, south of this area.

1) Rachel Lake is the single lake GNIS 1524794 (feature class Lake), OSM relation r16215472 and WDFW High Lakes "Rachel" (centre 47.420569,-121.330965). It sits on the east side of Rampart Ridge at the top of the steep climb out of Box Canyon. Don't confuse it with Box Canyon Lake (GNIS 1516900, about 1.6 ac, 47.4126,-121.3246), which is a different, smaller lake further down-valley. The OSM outline was traced from USGS elevation data. It shows a larger northern basin and a small southern lobe joined by a neck about 20 m wide at 47.4185. The simplified ring keeps this shape and is still a valid polygon.

2) Lila Lake vs "Lila Lakes": the official and most-used name is "Lila Lake" (singular). GNIS 1522076, WDFW ("Lila", 2.80 ac), WTA ("Lila Lake" hike), Wikipedia and OSM r7746070 all use it. "Lila Lakes" is informal. Backpacker, 10adventures and NWHikers use it for Lila Lake plus the small tarns around it on the bench under Alta Mountain. WTA mentions one such tarn on the approach, and OSM has about half a dozen unnamed ponds of 0.1–0.9 ac within 100–700 m. The row points at the named lake. OSM puts it about 150 m SE of those two ponds, at 47.4315,-121.3254, and it is the largest water body there (about 2.9 ac, roughly 185 x 90 m). WTA notes its long, narrow island. The island is an inner member in OSM, and following the project's convention I ignored inner members, so the island counts as inside the ring.

3) Rampart Lakes is GNIS 1524856 (Lake), whose GNIS/Wikipedia point sits on the largest, southern lake. OSM r6520842 is a multipolygon of 5 lakes: about 6.9, 4.6, 1.5, 0.8 and 0.6 ac, 14.4 ac in total. More tiny ponds sit east of them. WDFW names only the two big ones: "Rampart 1" (6.30 ac, 5,083 ft, 47.4157,-121.3404) and "Rampart 2" (3.80 ac, 5,082 ft, 47.4193,-121.3394). WTA calls them "a pretty collection of pothole lakes". They sit in the crook where the Rampart Ridge crest hooks around their north and west sides.

Point vs ring for Rampart Lakes: I used a POINT, the centre of the OSM multipolygon's bounding box, 47.4176,-121.3396. It is 9 m from Rampart 2's shore, and the farthest member lake edge is about 350 m away. Reasons: (a) Scoring can't tell the difference. SCORE_NEAR_KM is 10, so a tap anywhere in the basin (0.35 km or less) scores 100 either way. (b) A hull or ring would draw the land, heather and trails between the tarns as lake on the reveal, which is misleading. (c) It matches the Joffre Lakes precedent.

Caveats:
- WTA shows the Rachel Lake trail and trailhead as closed because of the Three Queens Fire (July 2026 notices). The blurbs describe the route and make no claims about current access.
- Wikipedia's Rampart Lakes elevation reference wrongly cites GNIS for Lila Lake. I queried GNIS 1524856 directly (1549 m).
- Wikipedia's "south slope of Alta Mountain" wording for Rampart Lakes is boilerplate and wrong (the lakes are about 2.8 km south of Alta), so I didn't use it.


### Fact-check changes

- Rachel Lake: removed 'area_km2: 0.102'. The figure itself is right (WDFW 25.10 ac = 0.1016 km2; NHD 0.1059; OSM 0.109), but the game's formatter shows it on the card as '0.1 km² (0 sq mi)'. FACTS_SPEC wants the imperial display to round-trip, and a 25-acre lake shown as 0 sq mi doesn't. This is the same reasoning the researcher used to drop Lila's area. The clue line becomes 'alpine lake · elev. 1,422 m · 671 m gain'.
- Rachel Lake blurb rewritten. 'Old-growth miles up Box Canyon' overstated the forest: WTA says sections of old growth alternating with brushy avalanche meadows. The new text also names the creek (Box Canyon Creek, per USFS and Wikipedia). New: 'Old growth and avalanche brush line Box Canyon Creek before a rooty, relentless final mile to this lake beneath Rampart Ridge, springboard for Lila and Rampart Lakes.'
- Lila Lake blurb rewritten for originality. 'long, skinny island' was a one-word swap of WTA's 'long, narrow island', and 'Parkland lake' echoed WTA's 'surrounded by parkland'. I checked every claim in the new sentence: island 52 x 15 m in OSM; Alta summit 1.17 km NNW; Rampart Ridge's north end 300 m SW; Hibox 1.86 km E, about 420 m above the lake, with only a 1,364 m valley between (EPQS transect). New: 'A slim island floats in this small parkland tarn high on Alta Mountain's south flank, where Rampart Ridge ends and Hibox Mountain fills the view to the east.'
- Rampart Lakes blurb rewritten. 'laced together by a confusing web of boot paths' followed WTA's own sentence ('social trails lacing them together') too closely. 'Cupped in a crook of Rampart Ridge' overstated the terrain: USGS EPQS shows a real crest only to the west (1,733 m, about 185 m above the lakes) and just a 19 m rise to the north. New: 'A scatter of tarns on a bench beneath the crest of Rampart Ridge, perched above Rachel Lake, with huckleberries and a tangle of boot paths between them.'
- Verified with no change: identities (GNIS 1524794 / 1522076 / 1524856, confirmed in USGS NHD Waterbody as well as OSM); both rings (valid, closed, 4 decimals, IoU about 0.90 against both OSM and NHD, Hausdorff 21-25 m and 8 m); the Rampart point (bbox centre recomputed exactly, 9 m from water); elevations 1422/1584/1549 queried directly from the GNIS gazetteer; gain conversions 2,200 ft -> 670.6 and 2,800 ft -> 853.4 (they display as 2,200 ft and 2,800 ft); facts keys and format. The appended check copy at passes sheet.parse_locations (230 rows). Names are unique across locations.csv, curated.csv, the candidates and schedule_lock. Difficulty hard for all three, consistent with Lake Serene.

## Box Ridge

Geometry: Open crest line, 25 points, about 11.7 km. It starts at the saddle below Alta's east ridge (the tip of GNIS's west arm), runs east to the triple divide of Box Canyon, Mineral and Gold creeks, then SE over Nobox (Pt 6242), Hibox and Lobox, and down the forested crest to the ridge toe above Kachess Lake (the south tip of the GNIS polygon).
I built it on my own 3DEP DEM download (0.0001-degree grid) with a least-cost crest path through these waypoints: west tip 47.4398,-121.3237; junction 47.4400,-121.3148; Hibox lidar summit 47.43177,-121.30084; Lobox lidar summit 47.42405,-121.28321; a 1716 m knob at 47.41675,-121.27105; Pt 1546 at 47.40852,-121.26653; and the Kachess end 47.3628,-121.2463. I simplified it with Douglas-Peucker at 40 m in local metres and rounded to 4 dp. Then I dropped three vertices that were redundant at a 50 m tolerance, and moved the west tip about 10 m so it sits inside the GNIS polygon.
The Hibox vertex equals the Hibox row point.
Independent check: I ran a watershed segmentation of the DEM seeded on the OSM streams to get the Box Canyon Creek / Mineral Creek drainage divide. Divide pixels lie a median 14 m from the line (p90 39 m, max 112 m).
The line is simple, lies 100% inside the GNIS Box Ridge polygon, and is within 0-72 m of every vertex of the OSM Box Ridge way.

Notes: The ridge uses category peak with type: ridge, following Shuksan Arm, and scores as a line ('Anywhere along it counts').
The line extends past GNIS's text ('Hibox at the NW end') to match the GNIS polygon and peakbagger's Nobox. To use only the section from Hibox SE, drop the first 7 points.
elevation_m is left out, as on Shuksan Arm. The high point is Hibox (1996.4 m); GNIS gives 1991 m for the ridge feature.
Difficulty hard: the name is obscure. The long line makes it a little easier to hit.

- Official name 'Box Ridge' (GNIS 1516904). Its true-shape polygon runs from the Kachess Lake shore (47.3625 N) NW past Lobox and Hibox. At the NW end it forks into a west arm reaching 47.4399,-121.3237 (the saddle below Alta's east ridge) and a north arm toward Alta Pass (47.4445,-121.3145). GNIS elevation is 1991 m. — https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/1516904 (Re-queried independently via the app's public GraphQL endpoint (https://edits.nationalmap.gov/apps/gaz-domestic/graphql, activeEditForGazRecord), which returned officialGazNameSnapshot 'Box Ridge'.)
- Hibox Mountain is 'At the NW end of Box Ridge' — https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/1529153
- Hibox's name is a portmanteau from its position as the high point of Box Ridge; Cascade Range; the peak's runoff drains to Box Canyon Creek and Mineral Creek, both of which reach Kachess Lake — https://en.wikipedia.org/wiki/Hibox_Mountain
- OSM natural=ridge way 'Box Ridge' (gnis 1516904) maps the southern crest from Pt 1546 (47.4085,-121.2665) to 47.3675,-121.2475. Every vertex lies within 0-72 m of the final line. — https://www.openstreetmap.org/way/1249966395
- The ridge separates Box Canyon Creek (OSM way 297840484, which heads at 47.4376,-121.3242 directly under the line's west end) from Mineral Creek (OSM way 32505502) — https://www.openstreetmap.org/way/297840484
- Box Ridge has three notable points: 'Lobox' (Pk 6032), Hibox (6,547 ft) and 'Nobox' (Pt 6242). Nobox is the northerly one, between Hibox and Alta, so the named ridge runs NW past Hibox. — https://www.peakbagger.com/peak.aspx?pid=2152 (Behind Cloudflare, so read from search-result snippets only.)
- Hibox is the highest point on Box Ridge; Lobox (6,032 ft) is on the same ridge — http://www.willhiteweb.com/alpine_lakes_wilderness/hibox_mountain/rachel_lake_trail_339.htm
- Lobox shares the extensive Box Ridge with Hibox and rises above Box Canyon — https://onehikeaweek.com/2021/08/23/lobox-mountain/
- Crest traced and checked on USGS 3DEP elevation data (0.0001-degree grid plus about 1 m lidar at the summits) — https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer

## Hibox Mountain

Geometry: Single summit point, 4 dp. It is 3 m from the 3DEP 1 m lidar high point I fetched myself (47.43177,-121.30084), 11 m from the OSM/USGS node, about 5 m from Wikipedia/peakbagger, about 25 m from PeakVisor, and inside the GNIS summit polygon.

Notes: Elevation follows the project's convention of using the Wikipedia infobox figure (listsofjohn 6,550 ft = 1996.44 m, so 1996.4). Peakbagger gives 6,547 ft, WTA 6,560 ft and lidar 6,548 ft.
Prominence uses listsofjohn (1,052 ft = 320.65 m, so 320.6). Peakbagger gives 1,027 ft, PeakVisor 316 m.
The clue line shows only the elevation.
First ascent is omitted because no reliable source gives one.

- Elevation 6,550 ft = 1996.4 m (listsofjohn); prominence 1,052 ft = 320.6 m (listsofjohn); parent Chikamin Peak; coordinates 47.431772,-121.300756 (peakbagger); Cascade Range; name from being Box Ridge's high point — https://en.wikipedia.org/wiki/Hibox_Mountain
- Summit node 47.4317799,-121.30065, ele 1996 (source USGS, gnis 1529153). This is 11 m from the row point. — https://www.openstreetmap.org/node/356547169
- GNIS summit polygon centroid 47.4319,-121.3003, which contains the row point; GNIS elevation 1988 m — https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/1529153
- Independent check: the about 1 m 3DEP lidar high point is 1995.85 m (6,548 ft) at 47.43177,-121.30084, 3 m from the row point. This supports roughly 6,550 ft. — https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer
- Cross-check: 1,996 m (6,550 ft); prominence 316 m; coordinates 47.431575,-121.30088 — https://peakvisor.com/peak/hibox-mountain.html
- Peakbagger's alternative figures: 6,547 ft, prominence 1,027 ft; top route 'Rachel Lake Trail to Hibox Climbers Path' — https://peakery.com/hibox-mountain-washington/
- Boot path leaves the Rachel Lake Trail about 2 mi in and goes steeply straight up (Class 2), with a bit of Class 3 rock at the end — http://www.willhiteweb.com/alpine_lakes_wilderness/hibox_mountain/rachel_lake_trail_339.htm
- Spur leaves after the second big meadow (about 2.3 mi) and is steep and full of roots; the route gains the ridge east of the peak for a Class 3 scramble with a 15 ft chimney — https://havetent.com/2015/06/08/hibox-mountain/
- Way trail leaves the Rachel Lake Trail at 2.2 mi and is much steeper; Class 3 scrambling on the east ridge of the peak — https://mountainflamingo.com/2019-06-30-hibox-mountain/
- Rated hard; needs route-finding and comfort with scrambling; 3,900 ft gain; WTA's high point figure is 6,560 ft — https://www.wta.org/go-hiking/hikes/hibox-mountain
- OSM path 'Hibox Mountain climber's trail' runs from the Rachel Lake Trail (47.4195,-121.3101) to the summit — https://www.openstreetmap.org/way/541829638

## Alta Mountain

Geometry: Single summit point, 4 dp. It is 11 m from the 3DEP 1 m lidar high point I fetched myself (47.44100,-121.33196), 11 m from the OSM/USGS node, 4 m from Wikipedia, about 25 m from PeakVisor, and inside the GNIS summit polygon.

Notes: Elevation sources disagree: listsofjohn/Wikipedia/PeakVisor give 6,275 ft, peakbagger 6,240 ft, GNIS 1904 m and WTA 6,151 ft. The 1 m lidar reads 6,274 ft, so 1912.6 m is kept.
Prominence is about 175 m from the lidar summit minus the roughly 1737 m DEM saddle toward Hibox, which is consistent with listsofjohn's 585 ft.
First ascent is omitted because there is no source.
Difficulty hard: the peak is popular, but placing it on bare imagery needs knowledge of the Kachess / Rachel Lake area.

- Elevation 6,275 ft = 1912.6 m (listsofjohn); prominence 585 ft = 178.3 m (listsofjohn); parent Hibox Mountain; coordinates 47.441131,-121.331964; Cascade Range; easiest route 'Scrambling (class 2) South Ridge' — https://en.wikipedia.org/wiki/Alta_Mountain
- Summit node 47.4410071,-121.331956, ele 1902 (source USGS, gnis 1515838). This is 11 m from the row point. — https://www.openstreetmap.org/node/356544086
- OSM 'Alta Mountain Trail' (way 297840980) branches from the Lila Lake Trail (way 297840979) at 47.4279,-121.3317 and runs due north along the south ridge to the summit — https://www.openstreetmap.org/way/297840980
- Independent check: the about 1 m 3DEP lidar high point is 1912.31 m (6,274 ft) at 47.44100,-121.33196. This confirms 6,275 ft over peakbagger's 6,240 ft and GNIS's 1904 m. — https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer
- GNIS summit polygon (centroid 47.4404,-121.3318) contains the row point; GNIS elevation 1904 m — https://edits.nationalmap.gov/apps/gaz-domestic/public/gaz-record/1515838
- Cross-check: 6,275 ft; prominence 169 m; parent Hibox; coordinates 47.440908,-121.331935 — https://peakvisor.com/peak/alta-mountain.html
- The climbers' path leaves the Lila Lake trail at a cairned junction 0.3 mi past the Rampart/Lila fork on the ridge. It is steep and loose at first, then follows a knife-edge ridge to a rocky summit. Photo caption: 'The lower portion of the ridge up Alta Mountain with Rachel Lake and the Rampart Lakes in the background'. 12 mi round trip, 3,300 ft gain. — https://www.wta.org/go-hiking/hikes/alta-mountain
- Peakbagger's alternative figures: 6,240 ft and prominence 520 ft — https://peakery.com/alta-mountain-washington/

## Rachel Lake

Geometry: Researcher's ring, verified independently. It is the OSM r16215472 outer ring (4 ways polygonized, 265 vertices), simplified with Douglas-Peucker at 20 m in a local metre projection on two open halves, rounded to 4 decimals and closed: 18 points (17 unique). My check against a fresh OSM API fetch: closed, valid simple polygon, area 100.1% of the raw outline, Hausdorff 21 m, IoU 0.91. Against USGS NHD: IoU 0.90, Hausdorff 25 m. It includes the small southern lobe joined by a narrow neck near 47.4185, which NHD also shows.

Notes: Clue line: alpine lake · elev. 1,422 m · 671 m gain. Card: 1,422 m (4,665 ft), 671 m (2,200 ft). area_km2 removed; see changes. Other checks: USGS EPQS lidar reads 1415 m at the lake surface, 7 m under GNIS, and I kept the published GNIS value. Box Canyon Lake (GNIS 1516900, 0.006 km2, 47.4126,-121.3245) is a separate lake down-valley and is not what the ring traces. Difficulty hard, like Lake Serene. Blurb 166 chars.

- geometry (outline) and identity — https://www.openstreetmap.org/relation/16215472 (OSM natural=water multipolygon 'Rachel Lake', gnis:feature_id 1524794, 4 outer ways, raw area 109,308 m2, re-fetched from api.openstreetmap.org 2026-09-28. Independent check against USGS NHD Waterbody (hydro.nationalmap.gov/arcgis/rest/services/nhd/MapServer/12): GNIS_NAME 'Rachel Lake', GNIS_ID 01524794, AREASQKM 0.1059, centroid 47.42055,-121.33099. The proposed ring has IoU 0.90 and Hausdorff 25 m against the NHD polygon)
- elevation_m 1422 — https://edits.nationalmap.gov/apps/gaz-domestic/public/summary/1524794 (USGS GNIS 1524794: elevation 1422 m (queried the gazetteer GraphQL directly). Wikipedia infobox 4,665 ft (1,422 m) cites GNIS. WDFW gives 4,664 ft. 1422 m displays as 4,665 ft)
- gain_m 670.6 (2,200 ft x 0.3048 = 670.56) — https://www.wta.org/go-hiking/hikes/rachel-lake (WTA: 7.0 mi roundtrip, 2,200 ft gain, high point 4,600 ft. 'sections of old-growth, primarily Douglas fir and hemlock' alternating with brushy avalanche meadows. After 2.75 mi the trail climbs 1,200 ft in about a mile over roots, rocks and big step-ups. From the lake, 600 ft up to Rampart Ridge, then left 1 mi to Rampart Lakes or right 0.75 mi to Lila Lake. Notice 7.30.26: trail closed due to the Three Queens Fire)
- type alpine lake; acreage cross-check — https://wdfw.wa.gov/fishing/locations/high-lakes/rachel (WDFW High Lakes 'Rachel': 25.10 ac, 4,664 ft, 47.420569,-121.330965, Kittitas County)
- blurb: gentle valley along Box Canyon Creek, then a steep final mile — https://www.fs.usda.gov/r06/okanogan-wenatchee/recreation/trails/rachel-lake-trail (USFS Trail #1313: 'a fairly gentle grade for the first 3 miles' on the north side of Box Canyon Creek, then 'a steep 1-mile climb to Rachel Lake', then about another mile to the Rampart Lakes basin)
- blurb: beneath Rampart Ridge — https://en.wikipedia.org/wiki/Rachel_Lake ('located on the eastern side of Rampart Ridge'. The trail follows Box Canyon Creek. Cross-checked with OSM Rampart Ridge w980376732, which passes 300 m west of the lake)

## Lila Lake

Geometry: Researcher's ring, verified independently. It is the OSM r7746070 outer way only (108 vertices), simplified with Douglas-Peucker at 8 m (stepped down from 20 m for a tiny lake to keep at least 8 points, per the repo's osm_areas convention), rounded to 4 decimals and closed: 12 points (11 unique). My check: valid simple polygon, area 100.5% of raw OSM, Hausdorff 8.5 m, IoU 0.92 vs OSM and 0.91 vs the USGS NHD polygon (Hausdorff 7.8 m).

Notes: Clue line: alpine lake · elev. 1,584 m · 853 m gain. area_km2 is still omitted, as the researcher decided: 0.0113 km2 would display as '0 km² (0 sq mi)'. EPQS lidar at the lake reads 1579 m against GNIS 1584; I kept GNIS. Difficulty hard. Blurb 157 chars.

- name 'Lila Lake' (singular) and identity — https://edits.nationalmap.gov/apps/gaz-domestic/public/summary/1522076 (USGS GNIS 1522076 'Lila Lake'. USGS NHD Waterbody GNIS_NAME 'Lila Lake', GNIS_ID 01522076, AREASQKM 0.0101, centroid 47.43151,-121.32535. WDFW 'Lila', WTA 'Lila Lake' and Wikipedia 'Lila Lake' agree. 'Lila Lakes' is informal)
- geometry (outline) — https://www.openstreetmap.org/relation/7746070 (OSM natural=water multipolygon, gnis:feature_id 1522076. Outer way 297840486 (raw area 11,696 m2 = 2.89 ac). Inner way 541831072 is the island (336 m2, about 52 x 15 m, aligned with the lake's long axis), which is ignored per repo convention)
- elevation_m 1584 — https://edits.nationalmap.gov/apps/gaz-domestic/public/summary/1522076 (GNIS elevation 1584 m, queried directly. Wikipedia 5,197 ft (1,584 m) cites GNIS. WDFW gives 5,196 ft. 1584 m displays as 5,197 ft)
- gain_m 853.4 (2,800 ft x 0.3048 = 853.44) — https://www.wta.org/go-hiking/hikes/lila-lake (WTA 'Lila Lake': 11.0 mi roundtrip, 2,800 ft gain, high point 5,400 ft. Mentions the lake's 'long, narrow island' and 'parkland'. Route: Rachel Lake, then switchbacks to the ridge junction, then right to Lila)
- type alpine lake; acreage cross-check — https://wdfw.wa.gov/fishing/locations/high-lakes/lila (WDFW High Lakes 'Lila': 2.80 ac, 5,196 ft, 47.431699,-121.324946)
- blurb: Alta Mountain's south flank, end of Rampart Ridge, Hibox to the east — https://en.wikipedia.org/wiki/Lila_Lake ('on the south slope of Alta Mountain'. Photo caption: Lila Lake on Rampart Ridge with Hibox Mountain in the background. OSM: Alta n356544086 is 1.17 km NNW. The north end of Rampart Ridge w980376732 is 300 m SW. Hibox n356547169 (ele 1996) is 1.86 km E. An EPQS transect shows the ground dropping to about 1,364 m between the lake and Hibox, so Hibox rises about 420 m above the lake with nothing in between)

## Rampart Lakes

Geometry: Point at the group centre: the centre of the bounding box of the 5 OSM r6520842 member lakes (47.41755,-121.33961, rounded to 47.4176,-121.3396). I recomputed it from a fresh OSM API fetch: 9 m from the nearest lake (Rampart 2 area), 348 m from the farthest member-lake vertex. Scoring can't tell a point from a ring here: a tap 0.35 km away scores 100 under the repo formula (NEAR 10 km). The repo's single-ring format can't represent 5 separate lakes without painting the land between them as water. This follows the Joffre Lakes precedent.

Notes: Clue line: pothole lakes · elev. 1,549 m. gain_m omitted: WTA's 2,200 ft for Rampart equals its figure for Rachel Lake, even though the route climbs about 600 ft more, so it's inconsistent. area_km2 omitted: ambiguous for a group (WDFW 2 lakes 10.1 ac vs OSM 5 lakes 14.4 ac), and it would display as 0.1 km²/0 sq mi. Difficulty hard. Blurb 152 chars.

- identity / group extent — https://www.openstreetmap.org/relation/6520842 (OSM natural=water multipolygon 'Rampart Lakes', gnis:feature_id 1524856, 5 outer lakes of 6.89, 4.59, 1.53, 0.83 and 0.60 ac (14.44 ac total), spanning 47.4145-47.4206 N, 121.3376-121.3416 W. In USGS NHD the GNIS name 'Rampart Lakes' (01524856, 0.0275 km2) is on the largest, southern lake only)
- elevation_m 1549 — https://edits.nationalmap.gov/apps/gaz-domestic/public/summary/1524856 (GNIS elevation 1549 m, queried directly (displays as 5,082 ft). Wikipedia 5,082 ft cites GNIS. WDFW Rampart 1 is 5,083 ft and Rampart 2 is 5,082 ft. EPQS lidar on Rampart 1 reads 1546.6 m)
- type pothole lakes; blurb: boot paths, berries — https://www.wta.org/go-hiking/hikes/rampart-ridge-1 (WTA 'Rampart Ridge - Rampart Lakes': a collection of pothole lakes with many social trails between them, 'lots of berries'. The WTA Rachel Lake page says Rampart Ridge 'is in the huckleberry zone')
- the two WDFW-named lakes — https://wdfw.wa.gov/fishing/locations/high-lakes/rampart-1 (WDFW 'Rampart 1': 6.30 ac, 5,083 ft, 47.415703,-121.340449. 'Rampart 2' (https://wdfw.wa.gov/fishing/locations/high-lakes/rampart-2): 3.80 ac, 5,082 ft)
- blurb: bench beneath the crest of Rampart Ridge, above Rachel Lake — https://epqs.nationalmap.gov/v1/json (USGS EPQS W-E transect at 47.4176: ridge crest 1,733 m at -121.3445 (matches OSM Rampart Ridge w980376732), lakes about 1,547 m, dropping east to Rachel Lake at 1,415 m. The lakes sit on a bench about 185 m below the crest and about 130 m above Rachel Lake. USFS Trail #1313 page: about a mile of climbing beyond Rachel Lake to the Rampart Lakes basin)
