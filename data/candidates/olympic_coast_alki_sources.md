# Hole-in-the-Wall, Rialto Beach, Second Beach, Alki Beach — sources (added 2026-09-29)

Researched, then independently fact-checked. Beach lengths are measured from the OSM beach outlines (no published figures);
areas were dropped (tide-dependent / not a beach-only figure). Second Beach is named "(Olympic coast)" to tell it apart from
Vancouver's Second Beach without naming La Push.

## Identification notes (olympic-coast)

Hole-in-the-Wall: the natural sea arch at the north end of Rialto Beach on the Olympic National Park wilderness coast (Clallam County, WA). Identified by GNIS 1510467, Wikidata Q105425593 ('natural arch on the Olympic Coast in Clallam County, Washington', coords 47.94167,-124.65139) and OSM node 267280215 (47.94173,-124.65088, tagged gnis:feature_id 1510467 and wikidata Q105425593). NPS describes it as 'a sea-carved arch about 1.5 mile north of Rialto Beach'. On Esri imagery at z18-19 both points sit on the rocky headland mass at the north tip of the Rialto sand. The row uses 47.9418,-124.6511, the middle of that rock and within about 20 m of both the GNIS and OSM points. Other features share the name, so the clue type 'sea arch' is what tells them apart.

Rialto Beach: OSM relation 3326596, natural=beach, name 'Rialto Beach', GNIS 1507790, wikidata Q2035275, wikipedia en:Rialto Beach, website pointing at the NPS Rialto page (relation v8, edited 2026-03-13). Its outline runs from the Quillayute River mouth spit (47.916) north past the Mora/Rialto parking area (about 47.920) and Ellen Creek to the headland at Hole-in-the-Wall (47.942). This is what the task asked for: the NPS beach north of the Quillayute River mouth, running up to about Hole-in-the-Wall.

Second Beach: OSM relation 20320038, natural=beach, name 'Second Beach', wikidata Q105394233, wikipedia en:Second Beach (Olympic National Park), which redirects to La Push Beach (relation v3, edited 2026-03-16). It is the sandy crescent south of La Push between Quateata Head (north, 47.893) and Teahwhit Head (south, 47.876). You reach it by the 0.7-mile NPS Second Beach Trail from the trailhead on the Quileute Reservation. This is not Second Beach in Vancouver's Stanley Park.

Naming: I named the row 'Second Beach (La Push)', not plain 'Second Beach'. Stanley Park is already a row in the game, and Vancouver's Second Beach inside it is well known and also inside the game region, so the bare name would be ambiguous. The existing names follow the same pattern: 'Castle Rock (Leavenworth)', 'Red Mountain (Snoqualmie)', 'Microsoft Campus (Redmond)'. If you'd rather not name the town, a less revealing option is 'Second Beach (Olympic coast)'. Plain 'Second Beach' would still parse and is unique in the CSV. 'Hole-in-the-Wall' and 'Rialto Beach' are kept as asked, and all three names are unique against the current locations.csv.

Geometry choices: both beaches are well mapped in OSM as named natural=beach multipolygons. On Esri World Imagery (the game's basemap) the outlines closely follow the visible sand, so both are closed rings rather than shoreline lines.
- Rialto: raw 156 points, 0.106 km². Douglas-Peucker at 15 m gives 25 points (Hausdorff 13.8 m); the tighter tolerance keeps the shape because the strip is only about 35 m wide.
- Second Beach: raw 253 points, 0.474 km², including the low-tide sand and one attached sea-stack islet that OSM maps as part of the outline. Douglas-Peucker at 20 m gives 44 points (Hausdorff 20.8 m).
- For both: 4-decimal rounding, first point == last point, and each is a valid simple polygon (shapely is_valid and is_simple).


Fact caveats:
- length_km and area_km2 for both beaches are measured from the OSM outlines. I found no published length or area for either beach.
- Length is along the landward edge between the two ends. Rialto: 3.10-3.15 km raw, 3.08 km on the simplified ring, so 3.1. That fits NPS putting Hole-in-the-Wall 1.5 mi (2.4 km) north of the parking area, plus about 0.6 km of spit south of the parking area. Second Beach: 3.08 km raw, 2.93-2.98 km simplified, so 3.0; the straight-line distance between its ends is 2.5 km.
- Second Beach's area includes low-tide sand as mapped, so it depends on tide. Drop the area_km2 values if only published figures are wanted.
- I found no reliable source for Hole-in-the-Wall's height, so height_m is left out.
- The NPS Rialto page says 'Distance: 1 mile to Hole-in-the-Wall camp area', while the NPS Mora/Rialto page says 1.5 mi to the arch. The blurb uses 1.5 mi, which matches the arch, OSM measurement and the NPS Tidepooling and Mora/Rialto pages.
- The NPS Rialto page currently says Mora Road is closed for construction through Oct 15, 2026. None of the text depends on road access.

Difficulty: all three are medium, comparable to Cannon Beach and Colchuck Lake. Seattle hikers know the outer Olympic coast, but on a bare map you have to find the right few kilometres of it west of Forks. 'La Push' in the Second Beach name makes it slightly easier; the plain 'Hole-in-the-Wall' is a single point target, which makes it slightly harder.

### Fact-check changes

- Identity confirmed for all three. Hole-in-the-Wall matches Wikidata Q105425593 (natural arch, GNIS 1510467) and OSM node 267280215. Rialto Beach matches OSM relation 3326596 (GNIS 1507790, Q2035275). Second Beach matches OSM relation 20320038 (Q105394233), the La Push beach between Quateata and Teahwhit Head.
- Second Beach geometry: replaced the full OSM ring with the same outline clipped at OSM's natural=coastline (mean high water). The raw outline extends 150-250 m seaward over what the game's Esri basemap shows as open water, including a big bulge around the north sea stacks. Rialto's own OSM relation stops at the coastline, so the clip also makes the two beaches consistent. The clip was rejoined with a 12 m closing across a pinch at the trail stairs and simplified with Douglas-Peucker at 12 m to 42 points. It is valid and simple, and I checked it visually on the imagery.
- Second Beach area_km2: 0.474 -> 0.166 (the beach above high water, 41 acres). The unclipped figure was also slightly off: 0.4776 km2 on the ellipsoid, not 0.474.
- Second Beach length_km: 3.0 -> 2.9. The two long edges of the clipped outline measure 2.93 and 2.91 km, smoothed about 2.8 km, straight 2.55 km.
- Rialto Beach area_km2: 0.106 -> 0.107. The equal-area measurement on the WGS84 ellipsoid gives 0.1069 km2; the researcher's local projection read about 0.8% low. length_km 3.1 confirmed (edges 3.12 and 3.16 km).
- Rialto blurb: 'Whole trees tossed up by winter storms pile along...' -> 'Storms heave whole tree trunks onto...'. Sources say storm-deposited trunks but do not say winter.
- Second Beach blurb rewritten. Dropped 'famous for its sunsets' (only an NPS photo caption supports it) and 'broad'. Now uses the NPS 'impassable even at the lowest tide' headlands and the 'steep stairs' from the Olympic Peninsula tourism site. 157 chars.
- Hole-in-the-Wall: point kept; it lies inside the arch's headland rock on Esri z19. Corrected the distance claim: it is about 18 m from the OSM node and 26 m from the GNIS/Wikidata point, not about 20 m from both. The blurb's 'walk through at low tide' is now sourced to the WTA Rialto Beach and Hole-in-the-Wall hike page. The 2011 magazine PDF only says the tides pass through the arch.
- Dropped the Mora Road closure note from Rialto (temporary, and not about the data). Kept the note that the NPS pages disagree on the distance (1 mile vs 1.5 miles).
- Names are unique against the current CSV, and there are no existing La Push, Forks or Olympic-coast rows. Clue facts (sea arch / driftwood beach / sea-stack beach, lengths, areas) don't give away the location. Difficulty medium for all three is kept.
- Alki Beach, the user's fourth request, was not in this batch; it is being researched separately.

## Identification notes (alki)

Alki Beach is the beach along Alki Ave SW on the north shore of West Seattle's Alki peninsula, facing Elliott Bay and downtown. It lies inside Seattle Parks' Alki Beach Park: OSM leisure=park relation 3195464 (Wikidata Q4727699, en:Alki Beach Park), which runs from about 64th Pl SW east to Duwamish Head. OSM also has a natural=beach multipolygon named "Alki Beach" (relation 20035106, GNIS 1502992, Wikidata Q49320012, surface=sand). It covers only the sandy core between about 53rd and 61st Ave SW, which is roughly 0.9 km long and 2.8 ha. The name is unique among existing rows, so there is no ambiguity.

### Fact-check changes

- Blurb: changed 'the skyline' to 'the downtown skyline' for clarity (now 158 characters). Checked that 'stormy' is accurate: Seattle Parks says 'cold, stormy day', and HistoryLink quotes a passenger saying it rained hard and the wind blew.
- area_km2: added a primary source, the City of Seattle Parks boundary GIS record (PMA 445). It gives PARKSBND_AREA as 5,919,768 sq ft, which is 135.90 acres or 0.54996 km², so 0.5500 is confirmed. The record also confirms the researcher's guess that the official acreage includes tidelands: the city parcel covers 0.55 km², against 7.5 ha for OSM's dry-land polygon.
- founded: 1910 confirmed by three sources: Seattle Parks, Friends of Seattle's Olmsted Parks, and the acquisition date in the Seattle GIS record.
- Added sources for the blurb: HistoryLink 5392 (landing at Alki Point, marked by a pylon at Alki Beach), HistoryLink 21323 (the weather), and Wikipedia West Seattle (skyline, Puget Sound and Olympics views).
- Geometry re-derived independently from OSM relation 3195464 and kept unchanged. The joined coastline is 81 nodes and 3.34 km, the simplified line 3.30 km. Every point is within 5.1 m of the coastline and the maximum deviation is 14.6 m. Also confirmed that OSM relation 20035106, the natural=beach 'Alki Beach', covers 0.92 km and 2.8 ha.
- The name 'Alki Beach' is unique among the existing 233 rows. Difficulty stays easy.

## Hole-in-the-Wall

Geometry: A single point inside the headland rock that holds the arch, where the Rialto Beach sand ends, checked on Esri World Imagery at z19. It is about 18 m from OSM node 267280215, which sits on the rock's south edge, and about 26 m from the GNIS/Wikidata point on its southwest edge. The OSM beach relation for Rialto Beach ends at the same rock.

Notes: No published height was found, so height_m is left out. OSM tags the node natural=cliff, but it carries the GNIS and Wikidata ids of the natural arch. Other features share the name; the clue type 'sea arch' plus the Olympic-coast context tells them apart.

- type: sea arch; identification ('a sea-carved arch about 1.5 mile north of Rialto Beach, within the Olympic wilderness') — https://www.nps.gov/olym/planyourvisit/visiting-mora-and-rialto.htm
- identification: Wikidata instance of natural arch, GNIS 1510467, coords 47.94167,-124.65139 — https://www.wikidata.org/wiki/Q105425593
- geometry: OSM node for Hole-in-the-Wall (47.94173,-124.65088), tagged gnis:feature_id 1510467 and wikidata Q105425593 — https://www.openstreetmap.org/node/267280215
- blurb: at low tide you can scramble through the rocky arch to the adjacent tide pools — https://www.wta.org/go-hiking/hikes/rialto-beach-hole-in-the-wall
- blurb: Hole in the Wall on Rialto Beach is an NPS tidepooling destination; tide pools hold sea stars and anemones — https://www.nps.gov/thingstodo/tidepooling-on-the-olympic-coast.htm
- blurb: rock arch near Rialto Beach, formed by sea erosion — https://en.wikipedia.org/wiki/Rialto_Beach

## Rialto Beach

Geometry: A closed ring from OSM multipolygon relation 3326596 (natural=beach, 'Rialto Beach'). It runs from the Quillayute River mouth spit (47.916) past the Mora/Rialto parking area to the headland at Hole-in-the-Wall (47.942). Simplified with Douglas-Peucker at 15 m, from 156 to 25 points (Hausdorff 13.8 m from the raw outline), rounded to 4 decimals, first == last, valid simple polygon. I kept the OSM outline over a shoreline line because on Esri World Imagery it follows the visible sand and driftwood strip (about 35 m wide) along its whole length. Its seaward edge is OSM's coastline (mean high water).

Notes: length_km and area_km2 are measured from OSM; I found no published figure for either. The length fits NPS's 1.5 mi from the parking area to the arch plus about 0.5 km of spit south of it. The NPS Rialto page gives '1 mile to Hole-in-the-Wall camp area', which disagrees with its own Mora/Rialto page (1.5 mi to the arch); the OSM measurement supports 1.5 mi.

- geometry, length_km 3.1, area_km2 0.107 (measured from the OSM natural=beach outline) — https://www.openstreetmap.org/relation/3326596
- type: driftwood beach ('giant drift logs', seastacks); Hole-in-the-Wall 'about 1.5 mile north of Rialto Beach'; Quillayute River separates Rialto from First, Second and Third Beaches — https://www.nps.gov/olym/planyourvisit/visiting-mora-and-rialto.htm
- north of the Quillayute River, with La Push Beach to the south; tree graveyard of storm-deposited trunks — https://en.wikipedia.org/wiki/Rialto_Beach
- cobbled beach (blurb) — https://olympicpeninsula.org/things-to-do/beaches/rialto-beach/
- consistency check on length: Ellen Creek at half a mile, then another mile to Hole-in-the-Wall; WTA hike page gives 3.3 mi roundtrip — https://www.wta.org/go-hiking/hikes/rialto-beach-hole-in-the-wall

## Second Beach (La Push)

Geometry: A closed ring from OSM multipolygon relation 20320038 (natural=beach, 'Second Beach'), clipped to the land side of OSM's natural=coastline (mean high water). The raw OSM outline runs 150-250 m past the coastline, onto low-tide flats and around the north sea stacks. On Esri World Imagery (the game's basemap) that area shows as open water, and the Rialto Beach relation stops at the coastline. The clipped ring keeps OSM's landward edge exactly and matches the visible sand. The high-water line touches the landward edge at a rock near the foot of the trail stairs, so the clip came out in pieces; a 12 m morphological closing rejoined them. Then Douglas-Peucker at 12 m (42 points, Hausdorff 14 m to the unsimplified shape; 15 m cut into the forest edge on this 60-90 m wide strip), 4-decimal rounding, first == last, valid simple polygon. The ring runs from the foot of Quateata at the north to Teahwhit Head at the south, including OSM's small pocket cove behind the sea stack there.

Notes: Named 'Second Beach (La Push)' because Vancouver's Second Beach, inside Stanley Park (already a game row), is also in the game region; the parenthetical follows 'Castle Rock (Leavenworth)'. length_km and area_km2 are measured from OSM (no published figures found). The area counts only sand above OSM's high-water line; the full OSM outline including low-tide flats is 0.478 km2. The NPS gives the trail as 0.7 mile; Wikipedia says about 1 mile.

- geometry, length_km 2.9, area_km2 0.166 (measured from the OSM natural=beach outline clipped at OSM's coastline) — https://www.openstreetmap.org/relation/20320038
- trail 0.7 mile; Teahwhit Head and Quateata Head 'impassible, even at the lowest tide'; sea stacks; parking on Quileute Tribal Lands — https://www.nps.gov/olym/planyourvisit/second-beach-trail.htm
- reached via a short hike and steep stairs; coastline dotted with sea stacks (blurb) — https://olympicpeninsula.org/things-to-do/beaches/second-beach/
- identification: beach near La Push; longest and flattest of the three La Push beaches — https://en.wikipedia.org/wiki/La_Push_Beach
- consistency check on length: Teahwhit Head about a mile south of where the trail reaches the beach, arch to the north — https://www.wta.org/go-hiking/hikes/second-beach

## Alki Beach

Geometry: An open line along the shoreline, not a ring. The OSM natural=coastline ways that form the seaward edge of the Alki Beach Park multipolygon (relation 3195464) were joined into one line: 81 nodes, 3.34 km, from the park's west end near 64th Pl SW, past the sandy core and the seawall promenade, to the east side of Duwamish Head. Douglas-Peucker at 15 m reduced it to 10 points, about 3.30 km long, rounded to 4 decimals. Independent check: every point lies within 5.1 m of the OSM coastline, and no coastline node is more than 14.6 m from the simplified line. This matches Seattle Parks' own description of the beach as a strip from 64th Place SW to Duwamish Head, and the 2.5-mile length on the card. The OSM natural=beach 'Alki Beach' ring (relation 20035106) was not used. It is well drawn but covers only the ~0.9 km, 2.8 ha sand core. That would conflict with the card's length and area, and would leave out much of the stretch people call Alki Beach. The park outline was not used as a ring either: OSM's version is a thin dry-land strip, and the city's parcel runs out over the tidelands. All points pass the region mask, bounding box and facts validation.

Notes: The length is Seattle Parks' round figure of 2.5 miles from Alki Point to Duwamish Head. The mapped public shoreline from 64th Pl SW is about 3.3 km; the difference is roughly the private shore around Alki Point itself. The area is the official park acreage, 135.9 ac, from the city's park boundary record. That parcel includes tidelands, which at minus tides are exposed beach. OSM's dry-land park polygon is only about 7.5 ha. Founded is 1910, the year the city acquired the beach, from Seattle Parks, Friends of Seattle's Olmsted Parks and the city's GIS acquisition date. The Wikipedia infobox's 1907 is not used. Difficulty is easy: the NW tip of the West Seattle peninsula, across Elliott Bay from downtown, is easy to find on satellite imagery.

- length_km: 4.02 (2.5 mi) — https://www.seattle.gov/parks/allparks/alki-beach-park
- area_km2: 0.5500 (135.9 acres) — https://services.arcgis.com/ZOyb2t4B0UYuYNYH/arcgis/rest/services/Park_Boundaries/FeatureServer/0/query?where=PMA%3D445&outFields=NAME,PARKSBND_AREA&f=json
- area_km2 (135.9 acres, second source) — https://en.wikipedia.org/wiki/Alki_Beach_Park
- area_km2 (135.9 acres) and founded: 1910 — https://seattleolmsted.org/parks/alki-beach-park/
- founded: 1910; tagline — https://www.seattle.gov/parks/allparks/alki-beach-park
- tagline (second source) — https://en.wikipedia.org/wiki/Alki_Beach_Park
- blurb: Denny Party landing, November 1851 — https://en.wikipedia.org/wiki/Denny_Party
- blurb: landing marked at Alki Beach — https://www.historylink.org/file/5392
- blurb: stormy day — https://www.historylink.org/File/21323
- blurb: summer beach, views of the Olympics; type: urban beach — https://www.seattle.gov/parks/allparks/alki-beach-park
- blurb: downtown skyline view — https://en.wikipedia.org/wiki/West_Seattle
- geometry: seaward (coastline) edge of the Alki Beach Park polygon — https://www.openstreetmap.org/relation/3195464
- identification: OSM natural=beach 'Alki Beach' (sand core, not used for geometry) — https://www.openstreetmap.org/relation/20035106
