# facts_landmarks sources

All pages accessed 2026-09-28. Wikipedia was read through the MediaWiki API (full wikitext).

**Conversions.** Feet to metres uses x 0.3048, rounded to 1 decimal. Miles to km uses x 1.609344, rounded to 2 decimals. Acres to km² uses x 0.0040468564, rounded to 3 decimals so the value converts back to the source's acre figure. Square miles to km² uses x 2.589988, rounded to 2 decimals. Figures that are metric in the source (BC/AB/YT) are left unconverted.

**Ski areas.** `elevation_m` is the top elevation. That means the top of the highest lift unless a row says otherwise. `vertical_m` is lift-served vertical. `lifts` is the resort's own count where it gives one, and the notes say what it includes.

**Taglines.** 5 of 34 rows have one: Grand Coulee, Multnomah, Mt Baker, Crystal and Cape Flattery. The "Candidates not used" section lists the rest.

---

## Deception Pass
- type `tidal strait`: https://en.wikipedia.org/wiki/Deception_Pass (infobox type "Strait").
- height_m `54.9`: this is the **bridge deck's** height above the water. The row's blurb gives the same 180 ft figure. https://en.wikipedia.org/wiki/Deception_Pass_Bridge says "Height from water to roadway: about 180 ft, depending on the tide". 180 ft = 54.864 m.
- built `bridge opened 1935`: the same article says construction began August 1934 and the bridge was dedicated July 31, 1935.

## Fremont Troll
- https://en.wikipedia.org/wiki/Fremont_Troll: a "public sculpture" 18 ft high, made of steel rebar, wire and concrete. Infobox year 1990. 18 ft = 5.486 m.

## Grand Coulee Dam
- tagline: https://en.wikipedia.org/wiki/Grand_Coulee_Dam says "the largest power station in the United States by nameplate capacity at 6,809 MW". The Bureau of Reclamation says "largest hydropower generating complex in the United States" (https://www.usbr.gov/pn/grandcoulee/about/index.html).
- type `concrete gravity dam`: from the Wikipedia infobox. USBR lists the dam type as concrete.
- height_m `167.6`: USBR gives a structural height of 550.0 ft (https://www.usbr.gov/projects/index.php?id=155). 550 ft = 167.64 m.
- built `1933–42`: Wikipedia gives a construction start of July 16, 1933 and an opening of June 1, 1942. *USBR's project page and FAQ give "1933–1941" for the main dam and Left Powerhouse (https://www.usbr.gov/pn/grandcoulee/about/faq.html). Change the value to `1933–41` if you prefer USBR.*

## Hurricane Ridge
- type `mountain ridge`: https://en.wikipedia.org/wiki/Hurricane_Ridge.
- elevation_m `1597.8`: NPS says "At an elevation of 5,242 feet, Hurricane Ridge is Olympic's alpine destination in winter" (https://www.nps.gov/olym/planyourvisit/hurricane-ridge-in-winter.htm). This is the elevation of the visitor area, where this row's point is. The ridge's high point is Elk Mountain at 6,772 ft, and that figure is not used. 5,242 ft = 1597.76 m.

## Husky Stadium
- https://en.wikipedia.org/wiki/Husky_Stadium: an outdoor football stadium. It opened November 27, 1920 and reopened August 31, 2013 after a $280M renovation.

## Microsoft Campus (Redmond)
- type and built: https://en.wikipedia.org/wiki/Microsoft_campus is about the corporate headquarters. Microsoft moved onto the campus on February 26, 1986.
- area_km2 `2.023`: The Seattle Times (2015) says the campus has "about 80 buildings on roughly 500 acres" (https://www.seattletimes.com/business/microsoft/microsoft-is-said-to-weigh-multibillion-campus-revamp/). Wikipedia's infobox gives 502 acres and cites this same article. 500 acres = 2.0234 km². *This is an approximate figure.*

## Multnomah Falls
- tagline `Tallest waterfall in Oregon`: Wikipedia says "the tallest waterfall in the state of Oregon at 620 ft" (citing Roza 2010). Travel Oregon says "Oregon's tallest waterfall" (https://traveloregon.com/things-to-do/destinations/waterfalls/multnomah-falls/).
- type `tiered waterfall`: the Wikipedia infobox gives type "Tiered", with 2 drops of 542 ft and 69 ft.
- height_m `189.0`: USFS says "the unique 620-foot falls" (https://www.fs.usda.gov/r06/columbiarivergorge/recreation/multnomah-falls). 620 ft = 188.98 m.

## Paradise
- type `subalpine meadows`: NPS describes the "wildflower meadows of Paradise" (https://www.nps.gov/mora/planyourvisit/paradise.htm). See also https://en.wikipedia.org/wiki/Paradise,_Washington.
- elevation_m `1645.9`: NPS says "Paradise is located at an elevation of 5,400 feet" (same page). 5,400 ft = 1645.92 m.
- *No tagline.* NPS says Paradise "**once held** the world record for measured snowfall in single year in 1971-1972: 1,122 inches" and held it "from 1972 until 1998" (https://www.nps.gov/mora/planyourvisit/annual-snowfall-totals.htm, https://www.nps.gov/mora/faqs.htm). Mt Baker's 1998–99 season beat it, so "holds the world record" would be false.

## Pike Place Market
- type `public market` and built `opened 1907`: Wikipedia says "It opened on August 17, 1907" (https://en.wikipedia.org/wiki/Pike_Place_Market). The official site says "Founded in 1907, the Market is one of the oldest and largest continuously operating public markets in the United States" (https://www.pikeplacemarket.org/about-pike-place-market/).

## Snoqualmie Falls
- height_m `81.7`: 268 ft, from https://en.wikipedia.org/wiki/Snoqualmie_Falls and the City of Snoqualmie (https://www.snoqualmiewa.gov/378/Snoqualmie-Falls). 268 ft = 81.69 m.
- type `plunge waterfall`: the World Waterfall Database lists Total Height 268 ft and Form "Plunge" (https://www.worldwaterfalldatabase.com/waterfall/Snoqualmie-Falls-4668). The Wikipedia infobox says "Curtain", which describes the falls at high water. WWD adds that lidar suggests the fall itself is 10–12 ft shorter than the official 268 ft.

## Space Needle
- The official site says "At 605 feet tall" and "grand opening on April 21, 1962" (https://www.spaceneedle.com/about). Wikipedia's infobox gives 184.404 m and the type "Observation tower". 605 ft = 184.40 m.

## Stanley Park
- https://en.wikipedia.org/wiki/Stanley_Park describes a 405-hectare (1,001-acre) public park. The infobox gives type "Urban park", area 404.9 ha and created 1888, and the article says it was "officially opened" on September 27, 1888. 404.9 ha = 4.05 km². *vancouver.ca blocked automated access (Cloudflare), so the city's own page was not checked.*

## Alpental
- vertical_m `698.0` and lifts `6`: the official Alpental page lists "2,290 VERTICAL FEET" and "1 SURFACE LIFT 1 QUAD CHAIR 3 TRIPLE CHAIRS 1 DOUBLE CHAIRS" (https://www.summitatsnoqualmie.com/alpental). Wikipedia gives 2,280 ft. 2,290 ft = 697.99 m.
- elevation_m `1652.0`: this is the top elevation, 5,420 ft (Alpental), from the infobox of https://en.wikipedia.org/wiki/The_Summit_at_Snoqualmie. 5,420 ft = 1652.02 m.
- built `opened 1967`: the Alpental section of the same article says the area "opened for the 1967–68 season".

## Artist Point
- *Note:* the en.wikipedia "Artist Point" article is about a Yellowstone viewpoint, not this one.
- type `viewpoint & trailhead`: USFS says "Artist Point is a scenic vista, parking lot, and trailhead at the end of the Mt. Baker Scenic Byway" (https://www.fs.usda.gov/r06/mbs/recreation).
- elevation_m `1572.8`: USFS gives "Artist Point Trailhead (elevation 5160')" (https://www.fs.usda.gov/r06/mbs/recreation/trails/chain-lakes-trail-682). 5,160 ft = 1572.77 m. Wikipedia's SR 542 article says 5,210 ft but cites Google Maps, so that figure is not used.

## Camp Muir
- elevation_m `3105.3`: NPS says the camp "is located just below the Cowlitz Cleaver at 10,188 feet" (https://www.nps.gov/mora/learn/historyculture/historic-camp-muir-area.htm). An NPS news release also gives "Camp Muir (elevation 10,188 feet)". 10,188 ft = 3105.30 m.
- built `first hut 1916`: the same NPS page lists the Guide Shelter as constructed in 1916 and the Public Shelter in 1921.
- type `climbers' high camp`: Wikipedia calls it a "high-altitude refuge for climbers" and "the most-used high camp" (https://en.wikipedia.org/wiki/Camp_Muir).

## Cape Flattery
- tagline and type: Wikipedia says Cape Flattery "is the northwesternmost point of the contiguous United States" (https://en.wikipedia.org/wiki/Cape_Flattery). *As a clue this effectively gives away the location, so consider dropping it.*

## Crystal Mountain
- Source: the official "Mountain Stats and Facts" page. The live site blocks bots (Imperva), so I read the Wayback copy from 2026-04-27: https://web.archive.org/web/20260427163102/https://www.crystalmountainresort.com/media/mountain-stats-and-facts
  - tagline: "Crystal Mountain is the largest ski resort in Washington State with a total of 2,600 acres".
  - lifts: the page says "Lifts 11". Its lift table lists the gondola and 9 chairs, so the 11th is presumably a magic carpet, as on Wikipedia.
  - built: the page says "first opened in 1962". Wikipedia gives an opening date of December 1962.
  - elevation_m `2131.2`: this is the top of the highest lift, Chair 6, which ends at 6,992 ft. The page also lists Summit (top of the gondola) at 6,872 ft and Silver King (hike-to) at 7,012 ft. 6,992 ft = 2131.16 m.
  - vertical_m `790.0`: this is the lift-served vertical of 2,592 ft. It equals Chair 6's top (6,992 ft) minus the official base (4,400 ft), and matches the Wikipedia infobox's "2,592 ft – lifts". The total vertical including hike-to terrain is 3,100 ft. 2,592 ft = 790.04 m.

## Discovery Park
- area_km2 `2.266`: Seattle Parks calls it "Seattle's largest park, a 560-acre natural area occupying most of the former Fort Lawton site" (https://www.seattle.gov/parks/parks/discovery-park). Wikipedia gives 534 acres. 560 acres = 2.2662 km².
- founded `1973`: the Seattle Parks history page says "1973: U.S. Senator Henry Jackson dedicated Discovery Park" (https://www.seattle.gov/parks/parks/discovery-park/discovery-park-history). Wikipedia agrees.
- type `urban park`: from the Wikipedia infobox.

## Dry Falls
- height_m `121.9` and length_km `5.63`: WA State Parks says "The dry 400-foot-high, 3.5-mile-wide remnants of this ice age waterfall make up one of the largest cataracts on the planet" (https://parks.wa.gov/news/2023/dry-falls-internationally-recognized-scientifically-significant-geologic-site). Wikipedia describes a "3.5-mile-long scalloped precipice" and a "400 ft rock face" (https://en.wikipedia.org/wiki/Dry_Falls). `length_km` is the length of the cliff line. 400 ft = 121.92 m and 3.5 mi = 5.633 km.
- type `dry cataract`: Wikipedia calls it a "cataract complex", and the waterfall has been dry since the ice-age floods ended.

## Hoh Rainforest
- type `temperate rainforest`: NPS calls it "one of the finest remaining examples of temperate rainforest in the United States" (https://www.nps.gov/olym/planyourvisit/visiting-the-hoh.htm).
- *Omitted:* Wikipedia's area (24 sq mi) and elevation range (394–2,493 ft) are both tagged "citation needed". I found no authoritative elevation for the visitor center.

## Mission Ridge
- Source: the infobox and text of https://en.wikipedia.org/wiki/Mission_Ridge_Ski_Area.
  - vertical_m `685.8`: 2,250 ft of vertical. 2,250 ft = 685.80 m.
  - elevation_m `2078.7`: top elevation 6,820 ft. 6,820 ft = 2078.74 m.
  - lifts `6`: "Mission Ridge has six lifts": one high-speed quad, three doubles and two rope tows. The official lift report lists Chairs 1–4, two rope tows and a carpet (https://www.missionridge.com/mountain-report/), so the count would be 7 if carpets are included.
  - built `opened 1966`: the article says it "began operations ... in the fall of 1966". The official expansion site calls it a cornerstone of the valley "since 1966" (https://expansion.missionridge.com/).

## Mt Baker Ski Area
- Source: the official Mountain Stats page (https://www.mtbaker.us/the-mountain/mountain-stats/). It lists "98-99 World Record Snowfall 1,140 inches", "Top of Chair 8 Elevation 5,089 ft", "Ski Area Vertical Rise 1,500 ft", "Quad Chairs 8" and "Handle Tows 2".
  - elevation_m `1551.1`: 5,089 ft = 1551.13 m.
  - vertical_m `457.2`: the official 1,500 ft = 457.2 m. Wikipedia instead gives 1,589 ft, which is 5,089 minus 3,500.
  - lifts `10`: 8 quads plus 2 handle tows.
- tagline: the official snowfall page says the 1,140 inches was "verified by NOAA as the World Record of snowfall during a single winter season" (https://www.mtbaker.us/the-mountain/snowfall-statistics/). Wikipedia says the area is "home to the world's greatest recorded snowfall in one season ... during the 1998–99 season".
- *No `built`.* The official history page is password-protected. Wikipedia's timeline has skiing from the 1920s, a first rope tow in 1937–38 and a first chairlift in 1953, so there is no single clear opening year.

## Palouse Falls
- height_m `61.0`: WA State Parks says the river "drops 200 feet at Palouse Falls" and calls it "the official state waterfall" (https://parks.wa.gov/find-parks/state-parks/palouse-falls-state-park-heritage-site). Wikipedia also gives 200 ft. 200 ft = 60.96 m.
- type `plunge waterfall`: WWD gives Form "Plunge" (https://www.worldwaterfalldatabase.com/waterfall/Palouse-Falls-4757). *WWD's own measured total height is 186 ft (57 m).*

## Summit at Snoqualmie
- type `ski area`.
- built `opened 1934`: this is the opening of today's Summit West. HistoryLink essay 10362 says Seattle's Municipal Ski Park at Snoqualmie Summit had "Gala opening ceremonies ... on January 21, 1934" (https://www.historylink.org/file/10362). Wikipedia says 1933, which is when the USFS permit was issued (December 20, 1933).
- *vertical, lifts and elevation omitted.* The official site treats "Summit" (West, Central and East) and Alpental as separate mountains, and it gives no combined stats for the three Summit areas. Wikipedia's resort-wide figures (2,280 ft vertical, 5,420 ft top, 25 lifts) either belong to Alpental or include it, and Alpental is its own row. Wikipedia's per-area lift lists are out of date: several lifts have been replaced or removed.

## White Pass Ski Area
- lifts `8`: the official Hours & Lifts page lists 5 chairs (Great White Express, Couloir Express, Basin Quad, Far East Triple, 4 The Birds) and 3 carpets, serving 1,402 acres (https://skiwhitepass.com/the-mountain/hours-and-lifts).
- built `opened 1953`: the official site says "Since opening in 1953" (https://skiwhitepass.com/local-ownership). Wikipedia says it "opened in January 1953".
- vertical_m `609.6` and elevation_m `1981.2`: 2,000 ft of vertical and a 6,500 ft top elevation, from the infobox of https://en.wikipedia.org/wiki/White_Pass_Ski_Area. The official site does not give these figures.

## Alvord Desert
- length_km `17.70`: BLM calls it "one of the largest playas in Oregon—six miles wide and 11 miles long" (https://www.blm.gov/visit/alvord-desert). 11 mi = 17.703 km.
- elevation_m `1219.2`: BLM's Alvord Desert WSA page says "The basin ... at 4,000 feet elevation, is the lowest point within the study area" (https://www.blm.gov/programs/national-conservation-lands/oregon-washington/alvord-desert-wsa).
- type: https://en.wikipedia.org/wiki/Alvord_Desert calls it a "dry lake".
- *Area omitted:* the Wikipedia infobox's 84 sq mi has no reference.

## Bongos
- type `Caribbean café`: the official site says "Bongos Café serves authentic Caribbean cuisine". It also quotes The Stranger's description of the building as "a repurposed 76 station" (http://www.bongosseattle.com/restaurant).
- *No `built`.* A search-engine summary says the café opened in July 2013, apparently from Yelp, but I could not confirm this on any accessible primary page.

## Cape Scott
- *Interpretation:* the row's point is the tip of the cape at the lighthouse, which lies inside Cape Scott Provincial Park. Following the task's grouping, the facts describe the park.
- founded `1973`: BC Parks says "Established in 1973 and named after the site of a lighthouse" (https://bcparks.ca/cape-scott-park/).
- area_km2 `223`: the BC Parks API gives a totalArea of 22,300 ha (17,328 ha upland and 4,972 ha marine) and an establishedDate of 1973-05-18 (https://bcparks.api.gov.bc.ca/api/protected-areas?filters[protectedAreaName][$contains]=Cape%20Scott). Wikipedia gives 22,294 ha.

## Carcross Desert
- area_km2 `2.59`: BBC Travel (2018) says it measures "just 1 sq mile (2.59 sq km)" (https://www.bbc.com/travel/article/20180621-the-unlikely-home-of-the-worlds-smallest-desert). Wikipedia gives about 2.6 km² (259 ha).
- type `sand dune field`: Wikipedia says it is "commonly referred to as a desert, but is actually a series of northern sand dunes" (https://en.wikipedia.org/wiki/Carcross_Desert). For that reason "world's smallest desert" is not used as a tagline.

## Lake Agnes Tea House
- elevation_m `2135`: the official site gives an "Altitude of 2135 meters (7005 feet)" (https://www.lakeagnesteahouse.com/).
- built `1901 (rebuilt 1981)`: the official About page says it was "built in 1901 as a refuge for hikers and started serving tea in 1905. The original log building was replaced in 1981" (https://www.lakeagnesteahouse.com/about). Wikipedia adds that the Canadian Pacific Railway built it (https://en.wikipedia.org/wiki/Lake_Agnes_Tea_House).

## Miles Canyon
- type `basalt canyon`: ExploreNorth says "the Yukon River has cut its way down through a flow of basaltic lava" (https://www.explorenorth.com/yukon/miles_canyon.html). Travel Yukon also describes its origin in basaltic lava. There is no Wikipedia article for the canyon.
- *No wall height.* The only figure I found was on a tour listing ("Basaltic 50ft rock walls", Indigenous Yukon). The Yukon Geological Survey paper was blocked. Schwatka Lake (1958) also raised the water level in the canyon by about 10 m.

## Painted Hills
- area_km2 `12.675`: the Painted Hills Unit "covers 3,132 acres" (https://en.wikipedia.org/wiki/John_Day_Fossil_Beds_National_Monument and https://en.wikipedia.org/wiki/Painted_Hills). 3,132 acres = 12.675 km².
- type `banded claystone hills`: Wikipedia says the hills are "primarily made of hard claystone layers". NPS describes them as "distinguished by varied stripes of red, tan, orange, and black" (https://www.nps.gov/joda/planyourvisit/ptd-hills-unit.htm).
- *No `founded`.* The monument was authorized in 1974 and established on October 8, 1975. The unit was a state park before that, so a single year would be misleading.

## Takakkaw Falls
- height_m `373`: Parks Canada says "Standing a whopping 373 m high, Takakkaw Falls" (https://parks.canada.ca/voyage-travel/experiences/sports/randonnee-hiking/chutes-waterfalls). The Wikipedia lead also gives 373 m but notes that sources range from 302 to 373 m. *WWD's laser/GPS measurement is 302 m (992 ft).*
- type `tiered waterfall`: WWD gives Form "Tiered Horsetails" with 4 drops (https://www.worldwaterfalldatabase.com/waterfall/Takakkaw-Falls-2397).

## Tombstone Park
- area_km2 `2200`: the Tr'ondëk Hwëch'in Government says "Covering 2,200 square kilometres" (https://www.trondek.ca/who-we-are/our-territory/tombstone-territorial-park/). mappingtheway.ca also says "The 2,200 square kilometer park". Wikipedia says "over 2100 square kilometres".
- type `territorial park`: see https://en.wikipedia.org/wiki/Tombstone_Territorial_Park.
- *No `founded`.* Sources disagree: Wikipedia says "By 2000 the Park was created", while other sources give 1999. yukon.ca blocked automated access.

---

## Candidates not used
- **Paradise:** "Former world record for single-season snowfall". The claim is true (NPS: record held 1972–1998), but the "holds" version in the brief is false.
- **Palouse Falls:** "Washington's official state waterfall" (WA State Parks). The blurb already says this.
- **Dry Falls:** "One of the first 100 IUGS Geological Heritage Sites" (WA State Parks, 2023 news release).
- **Space Needle:** "once the tallest building west of the Mississippi" (Wikipedia). This is a past claim.
