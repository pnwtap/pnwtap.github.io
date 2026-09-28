# facts_water_roads.csv sources

Group `water_roads`: 37 rows (15 lakes, 7 rivers, 3 islands, 12 roads). All pages were read on
2026-09-28. Wikipedia pages were read as wikitext through the MediaWiki API.

**Conversions.** Where the source gives feet, miles, square miles or acres, the metric value is
computed from that figure. Feet convert to metres at 1 ft = 0.3048 m, rounded to 1 decimal. Miles
convert to km at 1 mi = 1.609344 km, and square miles to km² at 2.589988, both rounded to 2
decimals. Acres convert to km² at 0.0040468564, rounded to 2 decimals. Two lakes are smaller than
1 km² (Colchuck, Serene), so their areas keep 3 decimals to preserve the acre figure. Metric sources
(Canadian lakes, rivers and roads) are copied as plain numbers.

**Abbreviations.** WP = English Wikipedia, CE = The Canadian Encyclopedia, PC = Parks Canada,
WTA = Washington Trails Association, GNIS = USGS Geographic Names Information System,
EPQS = USGS Elevation Point Query Service (3DEP 1 m lidar DEM, https://epqs.nationalmap.gov/v1/json),
NRCan CDEM/CDSM = Natural Resources Canada elevation service (geogratis.gc.ca/services/elevation).
The DEMs were used only as tie-breakers where published figures disagree.

**Taglines.** There are 5 (Crater Lake, Lake Chelan, Columbia, Fraser, Historic Columbia River
Highway), about 1 row in 7.4. That is slightly above the "1 in 8" guide, so drop Lake Chelan's first
if the total needs trimming. Other genuine superlatives that are sourced but left out:
- Kluane Lake: "largest lake contained entirely within Yukon"
- Skeena River: "second-longest river entirely within British Columbia"
- Yukon River: "longest river in Alaska and Yukon"
- Whidbey Island: "largest island in Washington state"

---

## Lakes

### Colchuck Lake
- type `alpine lake`: this natural lake was raised by a small 1930s irrigation dam. WP's lead calls it a
  "freshwater reservoir lake", and Chelan County's report on it is titled *Alpine Lake Optimization
  and Automation* (2015).
  The report is at https://iciclenetwork.com/sites/default/files/2017-11/Appraisal%20-%20Alpine%20Lakes%20Optimization%20and%20Automation%20%283-20-15%29_0.pdf
  and WP cites it at https://en.wikipedia.org/wiki/Colchuck_Lake.
- elevation_m `1697.7` (5,570 ft): Chelan County report p. 27, via WP Hydrology: "maximum surface
  elevation of 5,570 feet". GNIS (WP infobox) gives 1,695 m and WTA gives a 5,580 ft high point
  (https://www.wta.org/go-hiking/hikes/colchuck-lake).
- area_km2 `0.355` (87.8 acres): Chelan County report p. 27, via WP.

### Crater Lake
- tagline, type, length, area, elevation, depth: https://en.wikipedia.org/wiki/Crater_Lake
  - tagline: lead, "the lake is the deepest in the United States".
  - type `caldera lake`: the lake partly fills the caldera left when Mount Mazama collapsed.
  - depth_m `594.1` (1,949 ft): USGS, https://www.usgs.gov/volcanoes/crater-lake/bathymetry-and-floor-crater-lake,
    and Bacon et al. 2002 (GSA Bulletin), both cited by WP.
  - area_km2 `53.35` (20.6 sq mi), elevation_m `1883.1` (6,178 ft), length_km `9.66` (6 mi): WP
    infobox; the body says the lake is "5 by 6 mi" across.

### Diablo Lake
- type `reservoir`, length_km `7.24` (4.5 mi), depth_m `118.9` (390 ft), elevation_m `366.1` (1,201 ft):
  WP infobox, which cites GNIS; https://en.wikipedia.org/wiki/Diablo_Lake. The lake is impounded by
  Diablo Dam, part of Seattle City Light's Skagit project.
- Area omitted because sources disagree: WP Diablo Dam says 990 acres and a FERC document says
  770 acres.

### Garibaldi Lake
- type `lava-dammed lake`: WP Geology section. Lava from Mount Price and Clinker Peak dams the lake
  behind The Barrier (https://en.wikipedia.org/wiki/Garibaldi_Lake).
- area_km2 `9.94`, depth_m `258.7`: WP infobox. Hike in Whistler agrees ("almost 10 square
  kilometres", "at its deepest, 258 metres";
  https://hikeinwhistler.com/index.php/whistler-hiking-trails/garibaldi-lake).
- Elevation omitted because sources disagree: WP Garibaldi Lake 1,484 m, WP The Barrier 1,470 m,
  and NRCan CDEM about 1,468 m across the lake.

### Joffre Lakes
- type `glacier-fed lakes`, gain_m `400`: BC Parks, https://bcparks.ca/joffre-lakes-park/. It says
  "The glacier-fed lakes in this park…" and "Elevation gain from the parking lot to Upper Joffre
  Lake is approximately 400 m".
- The park's area (14.87 km², WP) is not used because it measures the park, not the lakes.

### Kluane Lake
- length_km `81`, area_km2 `408` (c.), depth_m `91` (max), elevation_m `781`: WP infobox and lead
  (https://en.wikipedia.org/wiki/Kluane_Lake). These cite Barker, Millar & Foos (2014), a Yukon Fish
  & Wildlife report, p. 1.
- WP also calls it "the largest lake contained entirely within Yukon". This is not used as a
  tagline (see above).
- No type: no source gives one.

### Lake Chelan
- https://en.wikipedia.org/wiki/Lake_Chelan
  - tagline: "Lake Chelan is the third deepest lake in the United States behind Crater Lake … and
    Lake Tahoe".
  - type: infobox "Glacially overdeepened lake"; the lead says "overdeepened … resembles a fjord".
  - length_km `81.27` (50.5 mi), area_km2 `134.94` (52.1 sq mi), depth_m `452.9` (1,486 ft): infobox.
  - elevation_m `335.3` (1,100 ft): "present maximum-capacity elevation", set after the 1927 dam.

### Lake Crescent
- area_km2 `20.75` (5,127 acres), depth_m `190.2` (official 624 ft), elevation_m `176.8` (580 ft): WP
  infobox and lead (https://en.wikipedia.org/wiki/Lake_Crescent). A 2013–14 bathymetric survey
  measured 596 ft; the official 624 ft is used here.
- type `glacially carved lake`: NPS says "this deep, glacially carved lake"
  (https://www.nps.gov/olym/planyourvisit/visiting-lake-crescent.htm).
- Length omitted. WP's infobox says "12 m", a unit error. Web claims of "12 miles" do not fit the
  lake's roughly 13 km straight-line extent.

### Lake Louise
- type `glacial lake`, area_km2 `0.8`: WP lead, https://en.wikipedia.org/wiki/Lake_Louise_(Alberta).
- elevation_m `1731`: CE says "Lake Louise, 2.4 km long, elevation 1731 m"
  (https://www.thecanadianencyclopedia.ca/en/article/lake-louise). WP's unreferenced infobox says
  1,750 m. NRCan CDSM reads a flat 1,732 m across the lake, which supports CE.
- Length omitted because sources disagree: WP 2.0 km, CE 2.4 km.
- Depth omitted because sources disagree: WP 70 m, other guides 90 m.

### Lake O'Hara
- type `alpine lake`, elevation_m `2020`: WP says "a lake at an elevation of 2020 m in the alpine
  area of Yoho National Park" (https://en.wikipedia.org/wiki/Lake_O%27Hara). NRCan CDEM reads
  2,019–2,020 m.

### Lake Serene
- type `alpine lake`: WP lead (https://en.wikipedia.org/wiki/Lake_Serene).
- area_km2 `0.214` (53 acres), elevation_m `769.9` (2,526 ft): WP infobox citing GNIS. WTA's high
  point is 2,521 ft.

### Maligne Lake
- length_km `22.5`, area_km2 `19.71`, depth_m `97`, elevation_m `1670`: WP infobox and lead
  (https://en.wikipedia.org/wiki/Maligne_Lake). NRCan CDSM reads about 1,671 m.
- No type: WP only says "oligotrophic".
- The blurb's claim "Largest natural lake in the Canadian Rockies" is not stated in these sources.

### Moraine Lake
- type `glacier-fed lake`, elevation_m `1884`, area_km2 `0.5` (50 ha): WP lead says "a snow and
  glacially fed alpine lake … elevation of approximately 1884 m … surface area of 50 ha"
  (https://en.wikipedia.org/wiki/Moraine_Lake). Other sources say 1,885 m.
- Depth omitted: WP's infobox gives 14 m with no reference, and nothing else confirms it.

### Okanagan Lake
- type `fjord lake`, length_km `135`, area_km2 `348`, depth_m `232`, elevation_m `342`: WP infobox and
  lead (https://en.wikipedia.org/wiki/Okanagan_Lake). These cite BCGNIS and the 1974 Okanagan Basin
  limnology report.
- CE instead gives 120 km and 351 km² (https://www.thecanadianencyclopedia.ca/en/article/okanagan-lake).
  The primary report's 135 km is kept; it also matches the blurb.

### Skyline Lake
- elevation_m `1554.5` (5,100 ft), gain_m `320.0` (1,050 ft): WTA, https://www.wta.org/go-hiking/hikes/skyline-lake.
  WTA gives a "Highest Point 5,100 feet" (the lake) and "Elevation Gain 1,050 feet" from Stevens Pass.
  EPQS reads 5,098.5 ft at the row pin, which matches.
- There is no WP page. No type is given because no source describes the lake.

## Rivers

### Columbia River
- https://en.wikipedia.org/wiki/Columbia_River
  - tagline: lead, "the largest river in the Pacific Northwest region of North America".
  - length_km `2000.41` (1,243 mi): lead and infobox. Note: 1,243 × 1.609344 = 2,000.41; the
    coordinator's example said 2000.43.
  - source `Columbia Lake, BC`: infobox, source elevation 2,690 ft.
  - mouth `Pacific Ocean`: infobox.

### Deschutes River
- length_km `405.55` (252 mi), source `Little Lava Lake`, mouth `Columbia River`: WP
  (https://en.wikipedia.org/wiki/Deschutes_River_(Oregon)). The headwaters are "at Little Lava Lake,
  a natural lake in the Cascade Range".

### Fraser River
- https://en.wikipedia.org/wiki/Fraser_River
  - tagline: lead, "the longest river within British Columbia".
  - length_km `1375`, source `Fraser Pass`, mouth `Strait of Georgia`: lead, "rising at Fraser Pass
    near Blackrock Mountain in the Rocky Mountains and flowing for 1,375 km, into the Strait of
    Georgia".

### Skagit River
- https://en.wikipedia.org/wiki/Skagit_River
  - length_km `241.40` (about 150 mi): lead.
  - source: "rises at Allison Pass in the Canadian Cascades of British Columbia", in E. C. Manning
    Provincial Park.
  - mouth: "These two forks both empty into Skagit Bay, a branch of Puget Sound".

### Skeena River
- length_km `570`, source `Spatsizi Plateau`, mouth `Chatham Sound`: WP
  (https://en.wikipedia.org/wiki/Skeena_River). The river "flows for 570 km before it empties into
  Chatham Sound … all part of the Pacific Ocean".

### Skykomish River
- length_km `46.67` (29 mi, main stem): WP lead and Course section
  (https://en.wikipedia.org/wiki/Skykomish_River).
  - The river begins where the North and South Forks meet, about 1 mi west of Index. It ends where
    it meets the Snoqualmie River to form the Snohomish at Monroe.
  - Counting the longest headwater tributaries (South Fork + Tye River), WP gives 62.4 mi
    (100.42 km). The row's line starts on the South Fork, so the owner may prefer that figure.

### Yukon River
- https://en.wikipedia.org/wiki/Yukon_River
  - length_km `3190`, mouth `Bering Sea`: lead.
  - source: "According to the United States Geographic Survey, the generally accepted source …
    is the Llewellyn Glacier at the southern end of Atlin Lake".

## Islands

### Haida Gwaii
- type `archipelago` (about 150 islands), area_km2 `10180`, high_point_m `1164`: WP infobox
  (https://en.wikipedia.org/wiki/Haida_Gwaii).
  - The high point is Mount Moresby at 1,164 m (WP Mount Moresby, citing bivouac.com).
  - CE rounds the area to "10,000 km²" (https://www.thecanadianencyclopedia.ca/en/article/haida-gwaii).
- population `4,526 (2021)`: WP infobox, citing BC Stats Population Estimates
  (bcstats.shinyapps.io/popApp). **This is a BC Stats estimate for 2021, not a census count.**
  Haida Gwaii is not a single census unit. WP's body text, citing the 2011 census, says "around
  4,500".

### San Juan Island
- area_km2 `142.59` (55.053 sq mi land area), population `8,632 (2020)`: WP lead
  (https://en.wikipedia.org/wiki/San_Juan_Island). The population is the 2020 census count for the
  county subdivision (Census TIGERweb). WP's infobox still shows the 2010 figure (6,894).
- high_point_m `329.2` (Mount Dallas, 1,080 ft): WP infobox. Other published figures range from
  1,073 to 1,083 ft.

### Whidbey Island
- https://en.wikipedia.org/wiki/Whidbey_Island
  - area_km2 `436.85` (168.67 sq mi): infobox.
  - length_km `59.55` (37 mi): "approximately 37 mi from north to south". This is the island's long
    axis, which is its claim to fame.
  - population `69,501 (2020)`: 2020 census, the sum of the North, Central and South Whidbey county
    subdivisions (CCDs).
- high_point_m `147.5` (484 ft, Goose Rock): WP infobox. WP Deception Pass State Park, citing the
  Everett Herald (2022), says "Goose Hill, which at 484 ft is the highest point on Whidbey Island".
  The Deception Pass Park Foundation page on the Goose Rock interpretive signs makes the same claim.

## Roads

### Chinook Pass Hwy (SR-410)
- length_km `147.19` (91.46 mi): from WP's SR 410 junction list (https://en.wikipedia.org/wiki/Washington_State_Route_410),
  which follows the WSDOT route log.
  - The Chinook Scenic Byway begins in Enumclaw at MP 15.98 ("Begin Chinook Scenic Byway") and
    ends at US 12 in Naches at MP 107.44.
  - Tourism sources round it to "92 miles" (visitrainier.com).
- high_point_m `1655.1` (Chinook Pass, 5,430 ft): https://en.wikipedia.org/wiki/Chinook_Pass.
- built `completed 1931`: "The highway across Chinook Pass was completed in 1931 and named the
  Mather Memorial Highway … on July 2, 1932" (WP SR 410).
- season `closed ~Nov–May`: "Chinook Pass is usually closed in November … It usually opens in
  mid-May" (WP Chinook Pass).
- type `scenic byway`: Chinook Scenic Byway, an All-American Road.

### Coquihalla Hwy
- https://en.wikipedia.org/wiki/British_Columbia_Highway_5
  - type `freeway`, length_km `186`: "Between Hope and Kamloops … It is a 186 km freeway"; the
    infobox gives 185.55 km.
  - high_point_m `1244`: "the 1244 m Coquihalla Pass".
  - built `opened 1986–87`: Phase 1 (Hope–Merritt) opened May 16, 1986; Phase 2 (Merritt–Kamloops)
    opened in September 1987.

### Duffey Lake Rd
- https://en.wikipedia.org/wiki/British_Columbia_Highway_99
  - length_km `91.8`: from the Highway 99 junction list (BC MoTI km). It runs from Mount Currie
    (km 210.50) to the Highway 12 junction at Lillooet (km 302.31, the "Duffey Lake Road north
    end"). That is the extent in the blurb. Measured from Pemberton instead, the road is "almost
    99 km" (WP).
  - high_point_m `1275`: "Cayoosh Pass, the highest point on the highway at 1,275 m".
  - built `paved 1990–91`: "Paving of Duffey Lake Road began in 1990 and was mostly completed by the
    end of the following year". It was a logging road in the 1960s, opened in 1972 and became part
    of Highway 99 in 1992.
  - type `mountain highway`: WP says the road winds "in very steep mountains" with 20 km/h
    advisory curves.

### Historic Columbia River Highway
- https://en.wikipedia.org/wiki/Historic_Columbia_River_Highway
  - tagline: "As the first planned scenic roadway in the United States…".
  - type `scenic highway`: lead.
  - length_km `119.25` (74.1 mi, Troutdale–The Dalles, "measured by historic mileposts"): infobox.
  - built `1913–22`: "built … between 1913 and 1922".
- High point omitted: not sourced.

### I-90 Exit 32 (Mt Si/Little Si) · I-90 Exit 38 (Deception Crags/Olallie) · I-90 Exit 47 (Denny Creek/Asahel Curtis)
- type `freeway exit`, road `I-90`: WP I-90 exit list (https://en.wikipedia.org/wiki/Interstate_90_in_Washington).
  - Exit 32: 436th Avenue Southeast, MP 30.95.
  - Exit 38: a split exit to Olallie State Park and the Fire Training Academy. The eastbound exit is
    at MP 36.14 and the westbound exit at MP 37.96.
  - Exit 47: "Denny Creek, Asahel Curtis", MP 46.09.
- elevation_m `151` / `368` / `566`: EPQS at each row's pin, which sits on the interchange.
  - The readings were 150.8, 367.6 and 565.6 m.
  - Readings at the OpenStreetMap exit points (the `motorway_junction` nodes) were:
    - Exit 32: 148 and 154 m.
    - Exit 38: 353 m (eastbound) and 407 m (westbound). Exit 38's ramps are about 3 km apart, so its
      figure is the freeway level between them.
    - Exit 47: 557 and 579 m.
- Note for the owner: the Exit 47 blurb calls it the "Tinkham Rd exit". WP's list signs
  **Exit 42** as "Tinkham Road" and Exit 47 as "Denny Creek, Asahel Curtis". Tinkham Road (FR 55)
  runs between the two exits.

### Icefields Parkway
- type `scenic mountain roadway`, length_km `232`, high_point_m `2070`: PC,
  https://parks.canada.ca/pn-np/ab/jasper/activ/itineraires-itineraries/promenadedesglaciers-icefieldsparkway.
  It says "The Icefields Parkway (93N) is a scenic mountain roadway … The 232 km route" and "From
  the highest point on the Icefields Parkway (2070 m)" (Bow Summit). WP Bow Pass also gives 2,070 m.
- built `1931–40; rebuilt 1961`: WP Alberta Highway 93 (https://en.wikipedia.org/wiki/Alberta_Highway_93).
  It was begun in 1931 as a Depression relief project and completed in 1940. "In 1961, a
  reconstructed paved and modern highway was opened".

### Mountain Loop Hwy
- https://en.wikipedia.org/wiki/Mountain_Loop_Highway
  - type `partly gravel scenic byway`: "a scenic byway". It is paved for 34 mi to Barlow Pass, then
    unpaved for about 13–14 mi.
  - length_km `86.90` (54 mi, Granite Falls–Darrington): infobox.
  - built `1936–41`: construction began March 23, 1936 and the highway opened in December 1941.
- high_point_m `719.9` (Barlow Pass, 2,362 ft): https://en.wikipedia.org/wiki/Barlow_Pass_(Washington).
  The highway article's body says 2,349 ft.
- season `closed ~Nov–May`: a Snohomish County Public Works release (May 2022) says "The annual
  winter closure is normally early November until end of May". The gated section runs from Deer
  Creek over Barlow Pass to Bedal (https://www.snohomishcountywa.gov/m/newsflash/Archive/Item/2332?arcId=3672).

### North Cascades Hwy (SR-20)
- length_km `225.31` (140 mi): Scenic Washington says "The 140-mile scenic byway stretches from
  Sedro-Woolley to Twisp"
  (https://www.scenicwa.com/story/the-road-worth-waiting-for-north-cascades-highway-reopens-to-washingtons-most-spectacular-scenery).
  - This matches WSDOT mileposts in WP's SR 20 junction list: Sedro-Woolley MP 64.37 to the SR 153
    junction near Twisp at MP 203.48, which is 139.1 mi.
  - The row's line ends at Winthrop, about 10 mi short of Twisp.
- https://en.wikipedia.org/wiki/Washington_State_Route_20
  - high_point_m `1669.4` (Washington Pass, 5,477 ft): Rainy Pass is 4,875 ft.
  - built `opened 1972`: "officially opened on September 2, 1972".
  - season `closed ~Nov–Apr`: "the median first open date was April 21. The median final closure
    date was November 24" (as of November 2021).
  - type `scenic byway`: a Washington State Scenic Byway and National Forest Scenic Byway.

### Sea-to-Sky Hwy
- https://en.wikipedia.org/wiki/British_Columbia_Highway_99
  - type `scenic highway`, length_km `134`: "the 134 km long section of Highway 99 from Horseshoe
    Bay to Pemberton, a province-designated scenic highway".
  - built `1958–66`:
    - Horseshoe Bay–Squamish opened August 7, 1958.
    - An unpaved extension to Pemberton opened in 1965.
    - The Alta Lake (Whistler) section was completed in January 1966.
    - The highway was rebuilt for the 2010 Olympics.
- High point omitted: not sourced.

### US-2 (Stevens Pass Hwy)
- https://en.wikipedia.org/wiki/U.S._Route_2_in_Washington
  - length_km `161.50` (100.35 mi): from the WSDOT mileposts in WP's junction list. US 2 starts at
    MP 0.00 in Everett, and the Leavenworth junction (Chumstick Highway) is at MP 100.35. This is
    the extent in the blurb.
  - high_point_m `1237.8` (Stevens Pass, 4,061 ft): also https://en.wikipedia.org/wiki/Stevens_Pass.
  - built `opened 1925`: "The Stevens Pass Highway was opened on July 11, 1925". The Tumwater Canyon
    section opened in 1929.
  - type `scenic byway`: the Stevens Pass Greenway National Scenic Byway, from Monroe to Cashmere.
