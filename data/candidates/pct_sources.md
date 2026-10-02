# Pacific Crest Trail rows — sources (added 2026-10-01)

Each row was researched and then independently re-derived and fact-checked.

## PCT Northern Terminus (poi, point)

Pin 49.0003,-120.8021: Single point, re-derived independently with a generic browser User-Agent. (1) OSM API: node 1040294835 'Pacific Crest Trail Northern Terminus' (historic=monument, v6) is at 49.0002693,-120.8021271. Node 1738808391 'Monument 78' (historic=boundary_stone, operator International Boundary Commission, ref MON 78) is at 49.0002692,-120.8021219, about 0.4 m away. Both round to 49.0003,-120.8021. (2) Monument 78 is a vertex of the admin_level=2 border way 75112566. The terminus node is the last node of PCT way 350466146, which runs 339 nodes north from 48.9571,-120.7810 and is in relation 1322978 'PCT - Washington Section L'. It is also the first node of way 89763502, which carries on north into Canada and is in relation 18377216 'Pacific Crest Trail - Int'. So this node is the end of the US trail. (3) Authoritative cross-check: the official IBC US-Canada boundary shapefile (v1.3, NAD83, downloa

Border rule (time-sensitive): Canada's CBSA discontinued the PCT entry permit in January 2025; as of late Sep 2026 crossing on the
trail is still prohibited and finishers turn back (nearest road: Harts Pass, about 30 mi south). Re-check each season.

Sources:
- Pin: OSM node 1040294835 'Pacific Crest Trail Northern Terminus' at 49.0002693,-120.8021271; end node of US PCT way 350466146 (Section L) and start of way 89763502 (PCT-Int into Canada) — https://www.openstreetmap.org/node/1040294835
- Pin cross-check: OSM node 1738808391 'Monument 78' (IBC boundary stone) at 49.0002692,-120.8021219, a vertex of US/Canada border way 75112566 — https://www.openstreetmap.org/node/1738808391
- Pin cross-check: official IBC US-Canada boundary dataset (v1.3, NAD83) has a boundary vertex at 49.00027006,-120.80212053, within about 0.1 m of OSM Monument 78 — https://www.internationalboundarycommission.org/en/maps-coordinates/coordinates.php
- Terminus monument is about three feet south of the border, a wood pillar monument just south of the metal obelisk Monument 78; Harts Pass is about 30 miles south; crossing the border on the PCT is illegal (Wayback capture 2026-08-31 of the PCTA page, which blocks non-browser clients) — https://web.archive.org/web/20260831070538/https://www.pcta.org/discover-the-trail/backcountry-basics/pct-transportation/directions-northern-terminus-pct/
- built: monument is five 12x12 Douglas fir posts, 4 to 10 ft long; it replicates the monument first installed in 1988 for the PCT's 20th year as a National Scenic Trail; PCTA put the replacement in the old footprint in summer 2018 (article dated Jan 9, 2019; Wayback capture 2022-01-21) — https://web.archive.org/web/20220121144652/https://www.pcta.org/2019/pacific-crest-trails-northern-terminus-monument-63137/
- Second source: current monument installed July 2018 — https://www.longtrailswiki.net/wiki/Northern_Terminus_Monument_(Pacific_Crest_Trail)
- elevation_m 1288: USGS 3DEP (10 m) point query gives 1287.9 m at the rounded pin and 1289.0 m at the OSM node. NRCan CDSM, a surface model, gives 1296 m. No official published terminus elevation was found — https://epqs.nationalmap.gov/v1/json?x=-120.8021&y=49.0003&units=Meters&wkid=4326&includeDate=false
- Trail length: 'We say that the Pacific Crest Trail is 2,650 miles long' (PCTA FAQ, Wayback capture 2026-07-24); the same FAQ says the terminus is about three feet south of Monument 78 — https://web.archive.org/web/20260724022249/https://www.pcta.org/discover-the-trail/faq/
- CBSA news release dated January 27, 2025: stops issuing permits to enter Canada on the PCT without reporting to a port of entry, effective immediately. Hikers must first enter Canada at a port of entry (Osoyoos or Abbotsford are closest). Trail is about 4,265 km from Mexico to Canada — https://www.canada.ca/en/border-services-agency/news/2025/01/the-cbsa-is-discontinuing-the-issuance-of-pacific-crest-trail-permits.html
- PCTA permit page: 'As of January 31, 2025' the CBSA has discontinued the PCT permit program and crossing the border on the PCT is prohibited (Wayback capture 2025-06-22) — https://web.archive.org/web/20250622120513/https://www.pcta.org/discover-the-trail/permits/canada-pct-entry-permit/
- Newest dated statement, Sep 9, 2026: crossing on the PCT is still prohibited, Canadian citizens included; hikers at the terminus must turn around and hike about 30 miles south to Harts Pass. Harts Pass to the border reopened that day after the Ptarmigan Fire closure — https://thetrek.co/pacific-crest-trail/pct-hikers-can-once-again-reach-the-northern-terminus/
- Wikipedia: it is not currently possible to cross the border legally in either direction on the trail; the Canada PCT entry permit was discontinued as of January 31, 2025 — https://en.wikipedia.org/wiki/Pacific_Crest_Trail
- Context, not in the blurb: Ptarmigan Fire closed the last 43 miles of the PCT in Washington on July 29, 2026 (article dated Aug 14, 2026) — https://www.kuow.org/climate/2026-08-14/new-monument-marks-northern-end-of-fire-blocked-pacific-crest-trail

## Pacific Crest Trail (hike, line, in-map part)

620 points, south to north from where the trail enters the map stencil (41.10 N, between Burney Falls and Castle
Crags) to Monument 78. Facts describe the full 2,650-mile trail, as the Dempster Highway row does for its road.

I rebuilt the geometry from scratch on 2026-10-01 using the OSM API (relation/{id}/full, generic browser User-Agent). Source is superroute relation 1225378 ("Pacific Crest Trail", ref PCT, operator PCTA) and its section relations: CA O 1253065, P 1253310, Q 1255154, R 1255155; OR B–G 1258061, 1260310, 1260388, 1260401, 1268073, 1268116; WA H–L 1285294, 1285818, 1296807, 1304995, 1322978. OSM has no "Oregon A"; CA R carries the trail over the state line. Graph check: I joined all 418 member ways into one node graph. It is a single connected component with 116,336 nodes. Every node has degree 2 except two ends, Burney Falls (41.0108,-121.6531) and Manning Park (49.0632,-120.7875). So there are no branches, alternates or side trails, and walking it gives one ordered path. It is the official line: past Crater Lake it stays west of the rim (around -122.20), not on the Rim alternate. It also includes the official Seiad Valley and Stehekin road walks. Clipping: - South: the path enters the region mask once (index 1416, 41.1008,-121.7890) and crosses 41.5 N once. The main row starts there, at an interpolated point 41.5000,-123.1112, because config.BBOX min_lat = 41.5 and build.py rejects any point further south (see notes). - North: it ends at OSM node 1040294835, "Pacific Crest Trail Northern Terminus" (49.00027,-120.80213), which is 0.4 m from node 1738808391 "Monument 78". The unoff

Southern extension: config.BBOX's south edge was lowered from 41.5 to 41.0 N to match the stencil, so the 107-point stretch from
41.10 N to 41.5 N (verified against the same OSM path) could be included.

Sources:
- length_km 4264.76: 'The Pacific Crest Trail spans 2,650 miles (4,265 kilometers) from Mexico to Canada' (checked on the Aug 2026 Wayback copy; pcta.org returns 403 to scripts). 2,650 mi x 1.609344 = 4264.76; the card shows 4,265 km (2,650 mi) — https://www.pcta.org/discover-the-trail/
- gain_m 149047.2: NPS Crater Lake 'Reflections' guide, Summer-Fall 2022, trail table: Pacific Crest 2,650 mi (4,265 km) one-way, elevation gain 489,000 feet (149,000 m), time 5 months. The original nps.gov PDF now returns 404; this is the archived copy I opened. 489,000 ft x 0.3048 = 149047.2; the card shows 149,047 m (489,000 ft) — https://web.archive.org/web/20260201123432/https://www.nps.gov/crla/learn/news/upload/Crater_Lake_Reflections_Summer-Fall_2022_for_Website-2.pdf
- gain_m (corroboration): Wikipedia's infobox and lead give overall elevation gain of about 489,000 ft, citing the same NPS guide — https://en.wikipedia.org/wiki/Pacific_Crest_Trail
- days 135–170: PCTA Thru-hiker FAQ says a thru-hike takes 'about 5 months', and average hikers are out '4.5 months or 5.5' (about 137–167 days, rounded outward to 5). NPS also lists 5 months — https://www.pcta.org/discover-the-trail/thru-hiking-long-distance-hiking/thruhiker-faq/
- high_point_m 4009.0: Forester Pass, 13,153 ft (USGS GNIS 260262), the highest point on the PCT. 13,153 x 0.3048 = 4009.03; the card shows 4,009 m (13,153 ft) — https://en.wikipedia.org/wiki/Forester_Pass
- season 'late Apr–late Sep (thru-hike)': Wikipedia infobox lists months 'Late April to Late September'. The PCTA FAQ says most northbound thru-hikers start mid-April through early May — https://en.wikipedia.org/wiki/Pacific_Crest_Trail
- built 'designated 1968, completed 1993': Wikipedia says it was designated a National Scenic Trail in 1968 (National Trails System Act) and officially completed in 1993, citing USFS history — https://en.wikipedia.org/wiki/Pacific_Crest_Trail
- Blurb, 'along the Sierra Nevada and Cascades': Wikipedia says the trail is 'closely aligned with the highest portion of the Cascade and Sierra Nevada' ranges — https://en.wikipedia.org/wiki/Pacific_Crest_Trail
- Length comparison (2019 state mileages): California 1,691.7 mi, Oregon 455.2 mi, Washington 505.7 mi (archived copy July 2026) — https://www.pcta.org/discover-the-trail/geography/
- Blurb, 'to Monument 78': the PCTA Washington region page says the trail ends at 'the northern terminus of the PCT which stands next to Monument 78 on the Canadian border (elev. 4,240′)'. Lakeview Ridge, 7,126 ft, is Washington's highest point on the trail — https://explore.pcta.org/regions/washington/
- Oregon region page (context for the in-map alternative): 457 miles, and Oregon's highest point on the trail is an unnamed saddle at 7,560 ft north of Mount Thielsen — https://explore.pcta.org/regions/oregon/
- Geometry: OSM superroute 1225378 and section relations 1253065, 1253310, 1255154, 1255155, 1258061, 1260310, 1260388, 1260401, 1268073, 1268116, 1285294, 1285818, 1296807, 1304995, 1322978 (OSM API, fetched 2026-10-01) — https://www.openstreetmap.org/relation/1225378
- Northern end: OSM node 1040294835 'Pacific Crest Trail Northern Terminus', 0.4 m from node 1738808391 'Monument 78' (International Boundary Commission, 1905) — https://www.openstreetmap.org/node/1738808391

## PCT Section J (hike, line)

80 points from OSM route relation 1296807 (PCT - Washington Section J), Snoqualmie Pass (I-90) to Stevens
Pass (US-2); one continuous path, max deviation about 150 m. Endpoints match Section I's end and Section K's start nodes.

Length is WTA's 74.7 mi (120.22 km); the OSM path measures 72.2 mi (116.18 km), matching current PCTA milepost spacing.
High point 5,988 ft (WTA), on the shoulder between Huckleberry Mountain and Chikamin Peak.

Time-sensitive, not in the blurb: in Sep 2026 the King and Three Queens fires closed part of Section J (WTA, 24 Sep 2026: Ridge Lake
to the Lake Vicente junction; PCTA order through Oct 31, 2026).

Sources:
- geometry: PCT Washington Section J route relation (from Interstate 90 to Hwy 2), 25 member ways chained into one 116.18 km path — https://www.openstreetmap.org/relation/1296807
- start endpoint: Section I (to Interstate 90) ends on the same node, 47.4271,-121.4153 — https://www.openstreetmap.org/relation/1285818
- end endpoint: Section K (from Hwy 2) starts on the same node, 47.7461,-121.0886 — https://www.openstreetmap.org/relation/1304995
- length_km 120.22 (74.7 miles one-way), gain_m 4876.8 (about 16,000 ft), high_point_m 1825.1 (5,988 ft), days 6–7 (six or seven days of food), not crossing a road, Kendall Katwalk on day 1, some places impassable until well into August. Closure note dated 9.24.26 — https://www.wta.org/go-hiking/hikes/pacific-crest-trail-section-j-snoqualmie-pass-to-stevens-pass-east
- season: Washington snow usually melts by mid to late July or August, and the mountains are typically snow-covered from October through June. Direct fetch returned 403, so this is verified from the page's search-indexed text — https://www.pcta.org/discover-the-trail/backcountry-basics/when-to-hike-pct/
- high point check, USGS 3DEP sampled every 100 m along the OSM path: 5,983 ft (1823.6 m) at 47.4788,-121.3210, 18.5 km from the start. The runner-up is Pieper Pass at 5,923 ft — https://epqs.nationalmap.gov/v1/docs
- high point location: Chikamin Peak summit 0.85 km ESE of the high point — https://www.openstreetmap.org/node/3012987620
- high point location: Huckleberry Mountain summit 1.1 km WSW of the high point — https://www.openstreetmap.org/node/288650064
- blurb: Kendall Katwalk viewpoint node lies on the trail (0 m) — https://www.openstreetmap.org/node/1013218078
- blurb: Spectacle Lake shore is 0.21 km from the trail — https://www.openstreetmap.org/relation/14308756
- blurb: Waptus Lake shore is 0.17 km from the trail — https://www.openstreetmap.org/relation/16190245
- blurb: Deep Lake shore is 0.15 km from the trail — https://www.openstreetmap.org/relation/16193988
- blurb: Cathedral Pass node lies on the trail (0 m) — https://www.openstreetmap.org/node/1013212545
- section identity, length (116.31 km) and endpoints, linked to OSM relation 1296807 — https://www.wikidata.org/wiki/Q133272510
