# facts_towns.csv sources

Group `towns`: 45 rows (12 WA, 7 OR, 7 AB, 17 BC, 2 YT). Everything was read on 2026-09-28. Wikipedia (WP) pages were read as wikitext through the MediaWiki API (action=query&prop=revisions), with infobox and body text checked against each other.

**Population.** US rows use the 2020 Census count (P.L. 94-171 POP100) for the incorporated place or CDP, taken from the Census Bureau's TIGERweb Census 2020 service (https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census2020/MapServer, layers 26 incorporated places and 28 CDPs). The api.census.gov endpoint now requires a key. Every US figure matches its WP infobox. None of these places had a 2020 Count Question Resolution change (errata: https://www2.census.gov/programs-surveys/decennial/2020/program-management/cqr/errata-notes/). Canadian rows use the 2021 Census: CSDs from table 98-10-0002-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810000201), designated places (DPL) from 98-10-0012-01 (https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810001201). All were checked against StatCan's 2021 amendments list (https://www12.statcan.gc.ca/census-recensement/2021/ref/amendments-modifications-eng.cfm). Only Whitehorse and Waterton Park were amended, and the revised counts are used for both. Unincorporated places are labelled `(2020, CDP)` or `(2021, DPL)`.

**Elevation.** US towns: the WP infobox feet figure (GNIS-derived), converted at 1 ft = 0.3048 m and written to 1 decimal so the imperial display round-trips. Each was cross-checked against the USGS EPQS 3DEP DEM (https://epqs.nationalmap.gov/v1/json) at the GNIS coordinate from the USGS DomesticNames files. Canadian towns use whole metres from the WP infobox, except where WP has only a range, an airport or aerodrome figure, or nothing. Those gaps use BC Building Code 2018 Div. B Appendix C Table C-2, which reproduces the NBC 2015 location elevations (https://free.bcpublications.ca/civix/document/id/public/bcbc2018/bcbc_2018dbac), or the official town/tourism figure. NRCan CDEM (geogratis.gc.ca/services/elevation/cdem) at the WP or CGNDB coordinate served only as a tie-breaker. Nelson's only WP figure is in feet (1,755 ft), so it is also written to 1 decimal.

**Founded.** This is the first incorporation year unless the row says FOUNDING year. The founding year is used only for Astoria (1811, its claim to fame), Dawson City (1897, gold rush), and the national-park townsites Banff (1885) and Jasper (1911), which were federally administered and only incorporated in 1990 and 2001. Incorporation years were cross-checked against official lists: the Oregon Blue Book city pages (https://sos.oregon.gov/blue-book/government/pages/<city>.aspx), MRSC Washington City & Town Profiles (https://mrsc.org/research-tools/washington-city-and-town-profiles), and the BC ministry incorporation list as tabulated in https://en.wikipedia.org/wiki/List_of_municipalities_in_British_Columbia. Three WP infoboxes were overridden by these lists and article bodies: Cannon Beach (1957, not 1956), Yakima (1886, not 1883), and Jasper (townsite 1911, not the 1813 fur post).

**Type.** Official municipal status: WP infobox, confirmed by the Census LSAD code (25 city, 43 town, 57 CDP), MRSC class, StatCan CSD type, or the BC list status. Capitals are typed plain `city` so the clue does not give them away.

**Taglines.** There are 5 (Astoria, Bend, Edmonton, Spokane, Whitehorse), about 1 row in 9. Each quotes a WP lead. None names a nearby place. Capital-city claims were avoided because they give the location away. Sourced superlatives left out: Vancouver "highest population density in Canada"; Bellingham "northernmost city with a population of more than 90,000 people in the contiguous United States"; Kamloops "Canada's largest municipal bike park"; Whitehorse's river as the "highest point on earth that can be reached by watercraft navigating from the sea".

**Region.** A named region taken from the WP lead or infobox. It is not a clue, so it may name the valley or park.

---

## Astoria

- Page: https://en.wikipedia.org/wiki/Astoria,_Oregon
- **tagline** `First permanent US settlement west of the Rockies`: WP lead: "the first permanent American settlement west of the Rocky Mountains" (also "oldest city in the state").
- **type** `city`: WP infobox (City); Census LSAD 25 = city.
- **population** `10,181 (2020)`: Census 2020 P.L. 94-171 via TIGERweb, GEOID 4103150 (Astoria city), POP100 10,181; matches WP.
- **elevation_m** `36.0`: WP infobox 118 ft, cited to GNIS 2409744 (City of Astoria civil point); USGS EPQS at that point 118 ft. Oregon Blue Book lists 23 ft (downtown waterfront).
- **founded** `1811`: FOUNDING year: WP lead "Founded in 1811" (Fort Astoria), the town's claim to fame. Incorporated 1876 per WP (Oregon Blue Book says 1/18/1856).
- **region** `Oregon Coast`: WP: "Populated coastal places in Oregon"; Clatsop County; press coverage of "the Northwest Oregon coast".

## Banff

- Page: https://en.wikipedia.org/wiki/Banff,_Alberta
- **type** `town`: WP infobox (Town); StatCan CSD type T (Town).
- **population** `8,305 (2021)`: StatCan 2021 Census, table 98-10-0002-01, CSD Banff (DGUID 2021A00054815035), 8,305; not amended.
- **elevation_m** `1400`: WP infobox 1,400 m, cited to Alberta Safety Codes Council design-data handbook; NRCan CDEM at WP coordinate 1,400 m.
- **founded** `1885`: FOUNDING year: WP infobox "Founded 1885"; WP body: "In 1885, Canada established a federal reserve ... around the Cave and Basin hot springs". Incorporated only on Jan 1, 1990 (first municipality incorporated inside a Canadian national park), so 1990 would misstate the town's age.
- **region** `Bow Valley, AB`: WP: "first established in the 1880s after the transcontinental railway was built through the Bow Valley".
- Notes: No 'highest town in Canada' tagline: WP does not make that claim; WP's list of communities by elevation puts Lake Louise (hamlet, 1,600 m) above Banff (1,400 m).

## Bella Coola

- Page: https://en.wikipedia.org/wiki/Bella_Coola,_British_Columbia
- **type** `unincorporated community`: WP infobox/lead: "an unincorporated community".
- **population** `162 (2021, DPL)`: StatCan 2021, table 98-10-0012-01, designated place Bella Coola (DGUID 2021A0006590225), 162; not amended. CAUTION: this DPL is only part of the townsite. The adjacent Nuxalk reserve Bella Coola 1 (CSD 2021A00055945802) has 937, and WP's figure for the whole Bella Coola Valley is 2,163 (2021).
- **region** `Central Coast, BC`: WP: head offices of the Central Coast Regional District are here; infobox regional district "Central Coast".
- Notes: elevation omitted: WP gives none. NBC/BCBC Table C-2 lists 40 m, but NRCan CDEM at the CGNDB point is 11 m on the tidewater townsite, so 40 m was not trusted. founded omitted: WP gives no townsite founding year.

## Bellingham

- Page: https://en.wikipedia.org/wiki/Bellingham,_Washington
- **type** `city`: WP infobox (City); Census LSAD 25; MRSC class: first-class city.
- **population** `91,482 (2020)`: Census 2020 via TIGERweb, GEOID 5305280, POP100 91,482; matches WP.
- **elevation_m** `20.1`: WP infobox 66 ft (GNIS 2409823); EPQS at GNIS point 65 ft.
- **founded** `1903`: Incorporated: WP "officially incorporated on December 28, 1903" (consolidation of four towns); MRSC 1903.
- **region** `Whatcom County, WA`: WP lead: "county seat of Whatcom County".

## Bend

- Page: https://en.wikipedia.org/wiki/Bend,_Oregon
- **tagline** `Home of the last Blockbuster video store`: WP lead lists "the last Blockbuster video-rental store" among Bend's attractions (revision read 2026-09-28).
- **type** `city`: WP infobox (City); Census LSAD 25.
- **population** `99,178 (2020)`: Census 2020 via TIGERweb, GEOID 4105800, POP100 99,178; matches WP lead.
- **elevation_m** `1110.1`: WP infobox 3,642 ft (GNIS 2409832); EPQS at GNIS point 3,641 ft. Oregon Blue Book: 3,628 ft.
- **founded** `1905`: Incorporated: WP lead "incorporated as a city in 1905"; infobox Jan 4, 1905; Oregon Blue Book 1/19/1905. (Platted 1904.)
- **region** `Central Oregon`: WP lead: "Bend is a city in Central Oregon".

## Calgary

- Page: https://en.wikipedia.org/wiki/Calgary
- **type** `city`: WP infobox (City); StatCan CSD type CY.
- **population** `1,306,784 (2021)`: StatCan 2021, 98-10-0002-01, CSD Calgary (2021A00054806016), 1,306,784; not amended.
- **elevation_m** `1045`: WP infobox 1,045 m ("downtown elevation" ref); NRCan CDEM at WP coordinate 1,048 m.
- **founded** `1884`: Incorporated as a town: WP body "On November 27, 1884, Lieutenant Governor Dewdney proclaimed the incorporation of The Town of Calgary" (infobox gives Nov 7, 1884). Fort Calgary founded 1875; city status 1894.
- **region** `Calgary–Edmonton Corridor, AB`: WP lead: "The city anchors the south end of the Statistics Canada-defined urban area, the Calgary–Edmonton Corridor".

## Canmore

- Page: https://en.wikipedia.org/wiki/Canmore,_Alberta
- **type** `town`: WP infobox (Town); StatCan CSD type T.
- **population** `15,990 (2021)`: StatCan 2021, 98-10-0002-01, CSD Canmore (2021A00054815023), 15,990; not amended.
- **elevation_m** `1309`: Explore Canmore (official destination site): "Elevation: 1,309 m (4,296 ft) at town centre" - https://www.explorecanmore.ca/plan-your-trip/about-canmore/ ; the Town of Canmore's own social channels give the same figure. NRCan CDEM at the CGNDB point 1,312 m. WP infobox gives only a 1,375-1,480 m range (Safety Codes handbook), which sits above the valley-floor townsite, so it was not used.
- **founded** `1965`: Incorporated: WP body "In 1965 ... Canmore was incorporated as a town" (infobox: village Jan 1, 1965; town Jun 1, 1966). Founded 1884.
- **region** `Bow Valley, AB`: WP lead: "located in the Bow Valley within Alberta's Rocky Mountains".

## Cannon Beach

- Page: https://en.wikipedia.org/wiki/Cannon_Beach,_Oregon
- **type** `city`: WP infobox (City); Census LSAD 25.
- **population** `1,489 (2020)`: Census 2020 via TIGERweb, GEOID 4110850, POP100 1,489; matches WP.
- **elevation_m** `14.0`: WP infobox 46 ft (GNIS 2409975); EPQS at GNIS point 45 ft. Oregon Blue Book: 30 ft.
- **founded** `1957`: Incorporated: Oregon Blue Book (Secretary of State) 3/5/1957 - https://sos.oregon.gov/blue-book/government/pages/cannon-beach.aspx . WP infobox says 1956 (unsourced); the official state figure is used.
- **region** `Oregon Coast`: WP: "a popular coastal Oregon tourist destination"; Category:Oregon Coast.

## Darrington

- Page: https://en.wikipedia.org/wiki/Darrington,_Washington
- **type** `town`: WP infobox (Town); Census LSAD 43 = town; MRSC class: town.
- **population** `1,462 (2020)`: Census 2020 via TIGERweb, GEOID 5316690, POP100 1,462; matches WP.
- **elevation_m** `170.1`: WP infobox 558 ft (GNIS 2412405); EPQS at GNIS point 557 ft. (WP lead separately says "554" ft for "the Darrington area"; infobox/GNIS used.)
- **founded** `1945`: Incorporated: WP "incorporated as a town in 1945" (infobox Oct 15, 1945); MRSC 1945. Settled 1891.
- **region** `North Cascades, WA`: WP lead: "located in a North Cascades mountain valley formed by the Sauk and North Fork Stillaguamish rivers".

## Dawson City

- Page: https://en.wikipedia.org/wiki/Dawson_City
- **type** `town`: WP lead: "Dawson City is a town" (legally the Town of the City of Dawson); StatCan CSD type T.
- **population** `1,577 (2021)`: StatCan 2021, 98-10-0002-01, CSD Dawson (2021A00056001029), 1,577; not amended. WP lead: "1,577 as of the 2021 census".
- **elevation_m** `320`: Klondike Visitors Association (dawsoncity.ca): "The community is at an elevation of 320 m (1,050 ft)" - https://dawsoncity.ca/discover-dawson/weather/ ; NRCan CDEM at the CGNDB point 320 m. WP's 370 m is cited to the Dawson City water aerodrome, so it is not the townsite.
- **founded** `1897`: FOUNDING year: WP body "The current settlement was founded by Joseph Ladue in January 1897" (Klondike Gold Rush boomtown, its claim to fame). WP infobox gives "Settled 1896"; incorporated as a city 1902, as a town 1980.
- **region** `Klondike, YT`: WP "Klondike, Yukon": a region "around the Klondike River, a small river that enters the Yukon River from the east at Dawson City".

## Drumheller

- Page: https://en.wikipedia.org/wiki/Drumheller
- **type** `town`: WP infobox (Town); StatCan CSD type T.
- **population** `7,909 (2021)`: StatCan 2021, 98-10-0002-01, CSD Drumheller (2021A00054805026), 7,909; not amended.
- **elevation_m** `670`: WP infobox 670 m (Alberta Safety Codes Council handbook); NRCan CDEM at WP coordinate 686 m.
- **founded** `1913`: Incorporated: WP "incorporated as a village on 15 May 1913, a town on 2 March 1916, and a city on 3 April 1930" (town again after 1998 amalgamation). Townsite founded 1911.
- **region** `Red Deer River valley, AB`: WP lead: "a town on the Red Deer River in the badlands"; "The Drumheller portion of the Red Deer River valley, often referred to as Dinosaur Valley".

## Edmonton

- Page: https://en.wikipedia.org/wiki/Edmonton
- **tagline** `Northernmost million-plus city in North America`: WP lead: "It is the northernmost city and metropolitan area in North America to have a population of over one million."
- **type** `city`: WP infobox (City and provincial capital); StatCan CSD type CY. "city" used so the clue does not reveal capital status.
- **population** `1,010,899 (2021)`: StatCan 2021, 98-10-0002-01, CSD Edmonton (2021A00054811061), 1,010,899; not amended.
- **elevation_m** `645`: WP infobox 645 m (Alberta Safety Codes Council handbook); NRCan CDEM at WP coordinate 617 m (river-valley edge).
- **founded** `1892`: Incorporated as a town: WP "In 1892, Edmonton was incorporated as a town" (city 1904). Fort Edmonton era dates to 1795.
- **region** `Calgary–Edmonton Corridor, AB`: WP lead: "the city anchors the northern end of what Statistics Canada defines as the Calgary–Edmonton Corridor".

## Eugene

- Page: https://en.wikipedia.org/wiki/Eugene,_Oregon
- **type** `city`: WP infobox (City); Census LSAD 25.
- **population** `176,654 (2020)`: Census 2020 via TIGERweb, GEOID 4123850, POP100 176,654; matches WP.
- **elevation_m** `125.9`: WP infobox 413 ft (GNIS 2410460); EPQS at GNIS point 414 ft. Oregon Blue Book: 430 ft.
- **founded** `1862`: Incorporated: WP "Formally incorporated as a city in 1862" (infobox Oct 17, 1862); Oregon Blue Book "10/17/1862 or 10/22/1864". Founded 1846.
- **region** `Willamette Valley, OR`: WP lead: "located at the southern end of the Willamette Valley".

## Fall City

- Page: https://en.wikipedia.org/wiki/Fall_City,_Washington
- **type** `unincorporated community`: WP lead: "an unincorporated community and census-designated place (CDP)".
- **population** `2,032 (2020, CDP)`: Census 2020 via TIGERweb CDP layer, GEOID 5323200 (Fall City CDP), POP100 2,032; matches WP.
- **elevation_m** `36.0`: WP infobox 118 ft (GNIS 2408111); EPQS at GNIS point 117 ft.
- **region** `Snoqualmie Valley, WA`: WP history: Fall City sits in the Snoqualmie Valley (first mill "in the Snoqualmie Valley" just upstream of Fall City; winds "down the Snoqualmie Valley").
- Notes: founded omitted: WP infobox says "Established 1856", but the body says that year refers to two military forts built during the Puget Sound War; the trading post dates to 1869 and the post office to 1872. No clear founding year.

## Fernie

- Page: https://en.wikipedia.org/wiki/Fernie,_British_Columbia
- **type** `city`: WP infobox (City); StatCan CSD type CY.
- **population** `6,320 (2021)`: StatCan 2021, 98-10-0002-01, CSD Fernie (2021A00055901012), 6,320; not amended. (WP infobox still shows 2016's 5,249.)
- **elevation_m** `1010`: WP infobox 1,010 m; BC Building Code 2018 Table C-2 (NBC data) also 1,010 m; NRCan CDEM 1,008 m.
- **founded** `1904`: Incorporated: WP lead "Founded in 1898 and incorporated as the City of Fernie in July 1904"; BC ministry list (via WP List of municipalities in BC) Jul 28, 1904.
- **region** `Elk Valley, BC`: WP lead: "a city in the Elk Valley area of the East Kootenay region".

## Gold Bar

- Page: https://en.wikipedia.org/wiki/Gold_Bar,_Washington
- **type** `city`: WP infobox (City); Census LSAD 25; MRSC class: code city.
- **population** `2,403 (2020)`: Census 2020 via TIGERweb, GEOID 5327365, POP100 2,403; matches WP.
- **elevation_m** `63.1`: WP infobox 207 ft / 63 m (GNIS 1520077); EPQS at GNIS point 197 ft.
- **founded** `1910`: Incorporated: WP "officially incorporated on September 16, 1910"; MRSC 1910.
- **region** `Skykomish Valley, WA`: WP: Gold Bar is in the "upper Skykomish Valley" (history section).

## Golden

- Page: https://en.wikipedia.org/wiki/Golden,_British_Columbia
- **type** `town`: WP infobox (Town); StatCan CSD type T; BC list status Town.
- **population** `3,986 (2021)`: StatCan 2021, 98-10-0002-01, CSD Golden (2021A00055939007), 3,986; not amended.
- **elevation_m** `800`: WP infobox 800 m; BCBC 2018 Table C-2: 790 m; NRCan CDEM 790 m.
- **founded** `1957`: Incorporated: WP infobox 1957; BC ministry list (via WP list) Jun 26, 1957.
- **region** `Columbia Valley, BC`: WP infobox region: "Columbia Valley".

## Index

- Page: https://en.wikipedia.org/wiki/Index,_Washington
- **type** `town`: WP infobox (Town); Census LSAD 43; MRSC class: town.
- **population** `155 (2020)`: Census 2020 via TIGERweb, GEOID 5333175, POP100 155; matches WP.
- **elevation_m** `164.9`: WP lead/infobox 541 ft (GNIS 1521157); EPQS at GNIS point 540 ft.
- **founded** `1907`: Incorporated: WP "incorporated as a municipality on October 11, 1907"; MRSC 1907. Established 1889.
- **region** `Skykomish Valley, WA`: WP: "every Skykomish Valley settlement" including Index (history section); on the North Fork Skykomish River.

## Jasper

- Page: https://en.wikipedia.org/wiki/Jasper,_Alberta
- **type** `specialized municipality`: WP infobox (Specialized municipality); StatCan CSD type SM (Specialized municipality).
- **population** `4,738 (2021)`: StatCan 2021, 98-10-0002-01, CSD Jasper (2021A00054815033), 4,738; not amended. (Pre-2024-wildfire count.)
- **elevation_m** `1060`: WP infobox 1,060 m (Alberta Safety Codes Council handbook); NRCan CDEM at WP coordinate 1,054 m.
- **founded** `1911`: FOUNDING year of the townsite: WP body "The railway divisional point at the location of the future townsite was established by the Grand Trunk Pacific Railway in 1911 and originally named Fitzhugh". WP infobox's "Founded 1813" is Jasper House, a fur-trade post (not the townsite); the first step to incorporation came in 1995 and specialized-municipality status in 2001.
- **region** `Athabasca River valley, AB`: WP lead: "The townsite is in the Athabasca River valley".

## Kamloops

- Page: https://en.wikipedia.org/wiki/Kamloops
- **type** `city`: WP infobox (City); StatCan CSD type CY.
- **population** `97,902 (2021)`: StatCan 2021, 98-10-0002-01, CSD Kamloops (2021A00055933042), 97,902; not amended. (WP infobox shows a 2025 estimate.)
- **elevation_m** `355`: BC Building Code 2018, Div. B Appendix C, Table C-2 (NBC 2015 climatic data): Kamloops 355 m - https://free.bcpublications.ca/civix/document/id/public/bcbc2018/bcbc_2018dbac ; NRCan CDEM at the CGNDB point 358 m. WP's 345 m is explicitly "Elevation at the airport", so the town-referenced figure is used.
- **founded** `1893`: Incorporated: WP lead "The city was incorporated in 1893". (BC ministry list gives Oct 17, 1967, which is the post-amalgamation re-incorporation.)
- **region** `Thompson Country, BC`: WP lead: "largest city within Thompson Country, a region of the British Columbia Interior".

## Kelowna

- Page: https://en.wikipedia.org/wiki/Kelowna
- **type** `city`: WP infobox (City); BC list status City.
- **population** `144,576 (2021)`: StatCan 2021, 98-10-0002-01, CSD Kelowna (2021A00055935010), 144,576; not amended. (WP infobox shows a 2025 city figure.)
- **elevation_m** `344`: WP infobox 344 m; BCBC 2018 Table C-2: 350 m; NRCan CDEM 342 m.
- **founded** `1905`: Incorporated: WP infobox May 5, 1905; BC ministry list May 4, 1905.
- **region** `Okanagan, BC`: WP lead: "a city on Okanagan Lake in the Okanagan Valley".

## Leavenworth

- Page: https://en.wikipedia.org/wiki/Leavenworth,_Washington
- **type** `city`: WP infobox (City); Census LSAD 25; MRSC class: code city.
- **population** `2,263 (2020)`: Census 2020 via TIGERweb, GEOID 5338845, POP100 2,263; matches WP.
- **elevation_m** `356.0`: WP infobox 1,168 ft (GNIS); EPQS at GNIS populated-place point 1,171 ft.
- **founded** `1906`: Incorporated: WP "officially incorporated as a city on September 5, 1906"; MRSC 1906.
- **region** `Chelan County, WA`: WP lead: "a city in Chelan County, Washington".

## Marblemount

- Page: https://en.wikipedia.org/wiki/Marblemount,_Washington
- **type** `unincorporated community`: WP: census-designated place (unincorporated; no municipal government).
- **population** `286 (2020, CDP)`: Census 2020 via TIGERweb CDP layer, GEOID 5343325 (Marblemount CDP), POP100 286; matches WP.
- **elevation_m** `109.1`: WP infobox 358 ft (GNIS 2408175); EPQS at GNIS point 357 ft.
- **region** `Skagit County, WA`: WP lead: "a census-designated place in Skagit County".
- Notes: founded omitted: WP gives no founding year.

## Mazama

- Page: https://en.wikipedia.org/wiki/Mazama,_Washington
- **type** `unincorporated community`: WP infobox/lead: "an unincorporated community".
- **elevation_m** `641.9`: WP lead/infobox 2,106 ft (GNIS 1522828); EPQS at GNIS point 2,111 ft.
- **region** `Methow Valley, WA`: WP lead: "located in the Methow Valley of Washington".
- Notes: population omitted: there is no Mazama CDP in the 2020 Census (checked TIGERweb incorporated-place and CDP layers for WA); WP's "(population 158)" is unsourced. founded omitted: WP says only "around the beginning of the twentieth century".

## Nanaimo

- Page: https://en.wikipedia.org/wiki/Nanaimo
- **type** `city`: WP infobox (City); BC list status City.
- **population** `99,863 (2021)`: StatCan 2021, 98-10-0002-01, CSD Nanaimo city (2021A00055921007), 99,863; not amended.
- **elevation_m** `28`: WP infobox 28 m; BCBC 2018 Table C-2: 15 m; NRCan CDEM 17 m.
- **founded** `1874`: Incorporated: WP infobox 1874; BC ministry list Dec 24, 1874.
- **region** `Vancouver Island, BC`: WP lead: "a city on the east coast of Vancouver Island".

## Nelson

- Page: https://en.wikipedia.org/wiki/Nelson,_British_Columbia
- **type** `city`: WP infobox (City); StatCan CSD type CY.
- **population** `11,106 (2021)`: StatCan 2021, 98-10-0002-01, CSD Nelson (2021A00055903015), 11,106; not amended. (WP infobox's 11,198 is the population-centre figure, not the municipality.)
- **elevation_m** `534.9`: WP infobox gives only feet: 1,755 ft, so this is written to 1 decimal. NRCan CDEM at the CGNDB point 546 m. BCBC 2018 Table C-2 lists 600 m.
- **founded** `1897`: Incorporated: WP infobox 1897; BC ministry list Mar 18, 1897.
- **region** `West Kootenay, BC`: WP lead: "one of three cities forming the commercial and population centers of the West Kootenay region".

## North Bend

- Page: https://en.wikipedia.org/wiki/North_Bend,_Washington
- **type** `city`: WP infobox (City); Census LSAD 25; MRSC class: code city.
- **population** `7,461 (2020)`: Census 2020 via TIGERweb, GEOID 5349485, POP100 7,461; matches WP.
- **elevation_m** `139.0`: WP infobox 456 ft (GNIS 2411270); EPQS at GNIS point 457 ft.
- **founded** `1909`: Incorporated: WP "officially incorporated on March 12, 1909"; MRSC 1909.
- **region** `Snoqualmie Valley, WA`: WP: "upper Snoqualmie Valley" (history section).

## Pemberton

- Page: https://en.wikipedia.org/wiki/Pemberton,_British_Columbia
- **type** `village`: WP infobox (Village); StatCan CSD type VL.
- **population** `3,407 (2021)`: StatCan 2021, 98-10-0002-01, CSD Pemberton (2021A00055931012), 3,407; not amended.
- **elevation_m** `210`: WP infobox 210 m (Pemberton is not in BCBC Table C-2).
- **founded** `1956`: Incorporated: WP "The village was incorporated in 1956"; BC ministry list Jul 20, 1956.
- **region** `Sea-to-Sky, BC`: WP infobox region: "Pemberton Valley (Sea to Sky Country/Lillooet Country)".

## Penticton

- Page: https://en.wikipedia.org/wiki/Penticton
- **type** `city`: WP infobox (City); BC list status City.
- **population** `36,885 (2021)`: StatCan 2021, 98-10-0002-01, CSD Penticton (2021A00055907041), 36,885; not amended.
- **elevation_m** `350`: BCBC 2018 Table C-2 (NBC data): Penticton 350 m; NRCan CDEM at the CGNDB point 345 m. WP's 344 m cites the Canada Flight Supplement (airport), so the town-referenced figure is used.
- **founded** `1908`: Incorporated (as a district municipality): WP "incorporated as a district municipality on December 31, 1908" (city 1948). BC ministry list gives Jan 1, 1909.
- **region** `Okanagan, BC`: WP lead: "a city in the Okanagan Valley".

## Port Hardy

- Page: https://en.wikipedia.org/wiki/Port_Hardy
- **type** `district municipality`: WP infobox (District municipality); StatCan CSD type DM.
- **population** `3,902 (2021)`: StatCan 2021, 98-10-0002-01, CSD Port Hardy (2021A00055943023), 3,902; not amended.
- **elevation_m** `23`: WP infobox 23 m; BCBC 2018 Table C-2: 5 m; NRCan CDEM 26 m.
- **founded** `1966`: Incorporated: WP infobox Apr 5, 1966 (BC Geographical Names ref); BC ministry list May 5, 1966.
- **region** `Vancouver Island, BC`: WP lead: "located on the north-east tip of Vancouver Island".

## Portland

- Page: https://en.wikipedia.org/wiki/Portland,_Oregon
- **type** `city`: WP infobox (City); Census LSAD 25.
- **population** `652,503 (2020)`: Census 2020 via TIGERweb, GEOID 4159000, POP100 652,503; matches WP.
- **elevation_m** `49.1`: WP infobox 161 ft, cited to GNIS 2411471 ("City of Portland" civil feature point, NE Portland); EPQS there 162 ft. Caveat: downtown is lower (Oregon Blue Book lists 77 ft).
- **founded** `1851`: Incorporated: WP "its incorporation on February 8, 1851"; Oregon Blue Book 1/23/1851. Founded 1845.
- **region** `Willamette Valley, OR`: WP: "at the northern end of Oregon's most populated region, the Willamette Valley".

## Prince George

- Page: https://en.wikipedia.org/wiki/Prince_George,_British_Columbia
- **type** `city`: WP infobox (City); BC list status City.
- **population** `76,708 (2021)`: StatCan 2021, 98-10-0002-01, CSD Prince George (2021A00055953023), 76,708; not amended.
- **elevation_m** `575`: WP infobox 575 m; BCBC 2018 Table C-2: 580 m; NRCan CDEM 570 m.
- **founded** `1915`: Incorporated: WP infobox Mar 6, 1915; BC ministry list Mar 6, 1915. (Fort George established 1807.)
- **region** `Northern BC`: WP lead: "often called the province's 'northern capital'"; home of the University of Northern British Columbia.

## Revelstoke

- Page: https://en.wikipedia.org/wiki/Revelstoke,_British_Columbia
- **type** `city`: Official name "City of Revelstoke" (WP); StatCan CSD type CY.
- **population** `8,275 (2021)`: StatCan 2021, 98-10-0002-01, CSD Revelstoke (2021A00055939019), 8,275; not amended.
- **elevation_m** `480`: WP infobox 480 m (unreferenced); NRCan CDEM at the CGNDB point 458 m; BCBC 2018 Table C-2 440 m.
- **founded** `1899`: Incorporated: WP infobox 1899; BC ministry list Mar 1, 1899. Founded 1880.
- **region** `Columbia-Shuswap, BC`: WP infobox: Columbia-Shuswap Regional District.

## Salem

- Page: https://en.wikipedia.org/wiki/Salem,_Oregon
- **type** `city`: WP infobox (Capital city); Census LSAD 25 = city. "city" used so the clue does not reveal capital status.
- **population** `175,535 (2020)`: Census 2020 via TIGERweb, GEOID 4164900, POP100 175,535; matches WP.
- **elevation_m** `53.9`: WP infobox 177 ft / 54 m, cited to GNIS 2411764; EPQS at GNIS point 178 ft. Oregon Blue Book: 154 ft.
- **founded** `1857`: Incorporated: WP "incorporated in 1857"; Oregon Blue Book 1/13/1857. Founded 1842.
- **region** `Willamette Valley, OR`: WP lead: "located in the center of the Willamette Valley".

## Sisters

- Page: https://en.wikipedia.org/wiki/Sisters,_Oregon
- **type** `city`: WP infobox (City); Census LSAD 25.
- **population** `3,064 (2020)`: Census 2020 via TIGERweb, GEOID 4167950, POP100 3,064; matches WP.
- **elevation_m** `972.0`: WP infobox 3,189 ft (GNIS 2411907); EPQS at GNIS point 3,189 ft. Oregon Blue Book: 3,182 ft.
- **founded** `1946`: Incorporated: WP "incorporated in 1946"; Oregon Blue Book 4/9/1946.
- **region** `Central Oregon`: Sisters is in Deschutes County (WP); WP "Central Oregon": region "traditionally considered to be made up of Deschutes, Jefferson, and Crook counties".

## Spokane

- Page: https://en.wikipedia.org/wiki/Spokane,_Washington
- **tagline** `Birthplace of Father's Day`: WP lead: "It is known as the birthplace of Father's Day".
- **type** `city`: WP infobox (City); Census LSAD 25; MRSC class: first-class city.
- **population** `228,989 (2020)`: Census 2020 via TIGERweb, GEOID 5367000, POP100 228,989; matches WP.
- **elevation_m** `561.7`: WP infobox 1,843 ft / 562 m (long-standing GNIS figure). EPQS at the GNIS civil-feature point is 1,901 ft (point is north of downtown).
- **founded** `1881`: Incorporated: WP "officially incorporated ... on November 29, 1881" (as Spokane Falls; reincorporated as Spokane 1891); MRSC 1881.
- **region** `Inland Northwest, WA`: WP lead: "the economic and cultural center of the Inland Northwest".

## Squamish

- Page: https://en.wikipedia.org/wiki/Squamish,_British_Columbia
- **type** `district municipality`: WP infobox (District municipality); StatCan CSD type DM.
- **population** `23,819 (2021)`: StatCan 2021, 98-10-0002-01, CSD Squamish (2021A00055931006), 23,819; not amended.
- **elevation_m** `5`: WP infobox 5 m; BCBC 2018 Table C-2 also 5 m; NRCan CDEM 2 m.
- **founded** `1948`: Incorporated (as a village): District of Squamish history page, "until 1948 for actual incorporation as the Village of Squamish" - https://squamish.ca/rec/arts-culture-and-heritage/history/ ; BC ministry list (via WP list) May 18, 1948. Re-incorporated as a district municipality on Dec 15, 1964. The WP town article gives no date.
- **region** `Sea-to-Sky, BC`: WP infobox region: "Howe Sound/Sea to Sky Country"; lead: "on the Sea to Sky Highway".

## Tofino

- Page: https://en.wikipedia.org/wiki/Tofino
- **type** `district municipality`: WP infobox (District municipality; "District of Tofino"); StatCan CSD type DM. (Resort Municipality status in 2008 is a designation, not a change of municipal type.)
- **population** `2,516 (2021)`: StatCan 2021, 98-10-0002-01, CSD Tofino (2021A00055923025), 2,516; not amended.
- **elevation_m** `10`: WP infobox 10 m; BCBC 2018 Table C-2 also 10 m; NRCan CDEM 22 m.
- **founded** `1932`: Incorporated: WP "Tofino was incorporated as a municipality in 1932 and as a district in 1982"; BC ministry list Feb 5, 1932.
- **region** `Clayoquot Sound, BC`: WP lead: "on the tip of the Esowista Peninsula at the southern edge of Clayoquot Sound".

## Vancouver

- Page: https://en.wikipedia.org/wiki/Vancouver
- **type** `city`: WP infobox (City); BC list status City.
- **population** `662,248 (2021)`: StatCan 2021, 98-10-0002-01, CSD Vancouver (2021A00055915022), 662,248; not amended.
- **elevation_m** `40`: BCBC 2018 Table C-2 (NBC data): "Vancouver (City Hall)" 40 m; NRCan CDEM at the CGNDB point (City Hall) 42 m. WP infobox gives only a range (0-152 m).
- **founded** `1886`: Incorporated: WP infobox Apr 6, 1886; BC ministry list Apr 6, 1886. (Granville established 1870.)
- **region** `Lower Mainland, BC`: WP lead: "located in the Lower Mainland region of British Columbia".

## Victoria

- Page: https://en.wikipedia.org/wiki/Victoria,_British_Columbia
- **type** `city`: WP infobox (City and provincial capital); BC list status City. "city" used so the clue does not reveal capital status.
- **population** `91,867 (2021)`: StatCan 2021, 98-10-0002-01, CSD Victoria (2021A00055917034), 91,867; not amended.
- **elevation_m** `23`: WP infobox 23 m; BCBC 2018 Table C-2: 10 m; NRCan CDEM 18 m.
- **founded** `1862`: Incorporated: WP infobox Aug 2, 1862; BC ministry list Aug 2, 1862. (Fort Victoria / British settlement from 1843.)
- **region** `Vancouver Island, BC`: WP lead: "located on the southern tip of Vancouver Island".

## Waterton

- Page: https://en.wikipedia.org/wiki/Waterton_Park
- **type** `hamlet`: WP lead: "Waterton Park, commonly referred to as Waterton, is a hamlet"; StatCan: designated place (UNP).
- **population** `132 (2021, DPL)`: StatCan 2021 designated place Waterton Park (DGUID 2021A0006480249). Release table 98-10-0012-01 shows 158, but StatCan's 2021 amendments page (revised 2023-12-01) corrects it to 132: https://www12.statcan.gc.ca/census-recensement/2021/ref/amendments-modifications-eng.cfm . WP also uses 132.
- **elevation_m** `1280`: WP lead/infobox: "It has an elevation of 1280 m"; NRCan CDEM at WP coordinate 1,291 m.
- **region** `Waterton Lakes NP, AB`: WP lead: "within Improvement District No. 4 Waterton (Waterton Lakes National Park)".
- Notes: founded omitted: WP gives no founding year for the townsite.

## Whistler

- Page: https://en.wikipedia.org/wiki/Whistler,_British_Columbia
- **type** `resort municipality`: WP infobox/lead: "a resort municipality" (official name Resort Municipality of Whistler; BC list status Resort municipality). StatCan files it under CSD type DM because StatCan has no resort-municipality type.
- **population** `13,982 (2021)`: StatCan 2021, 98-10-0002-01, CSD Whistler (2021A00055931020), 13,982; not amended.
- **elevation_m** `670`: WP infobox 670 m; BCBC 2018 Table C-2: 665 m; NRCan CDEM 674 m.
- **founded** `1975`: Incorporated: WP infobox 1975 ("Incorporated as a resort municipality"); BC ministry list Sep 6, 1975. Settled 1914.
- **region** `Sea-to-Sky, BC`: WP infobox subregion: "Sea-to-Sky Corridor".

## Whitehorse

- Page: https://en.wikipedia.org/wiki/Whitehorse
- **tagline** `Largest city in Northern Canada`: WP lead: "Whitehorse is the capital of Yukon, and the largest city in Northern Canada."
- **type** `city`: WP infobox (City and territorial capital); StatCan CSD type CY. "city" used so the clue does not reveal capital status.
- **population** `28,408 (2021)`: StatCan 2021, CSD Whitehorse (2021A00056001009). The release tables and WP show 28,201, but StatCan's 2021 amendments page (revised 2023-12-01) corrects the count to 28,408: https://www12.statcan.gc.ca/census-recensement/2021/ref/amendments-modifications-eng.cfm . Use 28,201 if release-table figures are preferred.
- **elevation_m** `640`: WP body: "At 640 m above sea level, the river at Whitehorse is the highest point on earth that can be reached by watercraft navigating from the sea"; downtown sits on the river flats. NRCan CDEM at the CGNDB (downtown) point 640 m. WP infobox gives only a municipal range (670-1,702 m).
- **founded** `1950`: Incorporated: WP lead "It was incorporated in 1950". Established 1898 (gold rush).
- **region** `Southern Yukon`: WP lead: "on the Alaska Highway in southern Yukon".

## Winthrop

- Page: https://en.wikipedia.org/wiki/Winthrop,_Washington
- **type** `town`: WP infobox (Town); Census LSAD 43; MRSC class: town.
- **population** `504 (2020)`: Census 2020 via TIGERweb, GEOID 5379380, POP100 504; matches WP.
- **elevation_m** `531.9`: WP infobox 1,745 ft (GNIS); EPQS at GNIS points 1,754-1,761 ft.
- **founded** `1924`: Incorporated: WP "The town was incorporated in 1924" (infobox Mar 12, 1924); MRSC 1924. Founded 1890.
- **region** `Methow Valley, WA`: WP lead: founded after "the Methow Valley ... was opened to white settlement"; at the Methow-Chewuch confluence.

## Yakima

- Page: https://en.wikipedia.org/wiki/Yakima,_Washington
- **type** `city`: WP infobox (City); Census LSAD 25; MRSC class: first-class city.
- **population** `96,968 (2020)`: Census 2020 via TIGERweb, GEOID 5380010, POP100 96,968; matches WP.
- **elevation_m** `367.9`: WP infobox 1,207 ft (GNIS 2412314); EPQS at GNIS point 1,208 ft.
- **founded** `1886`: Incorporated: WP body "dubbed North Yakima and was officially incorporated ... on January 27, 1886"; MRSC 1886. NOTE: WP infobox says Dec 10, 1883, which is Yakima City, today's Union Gap (WP Union Gap: incorporated Nov 23, 1883).
- **region** `Yakima Valley, WA`: WP lead: "situated in the Yakima Valley".
