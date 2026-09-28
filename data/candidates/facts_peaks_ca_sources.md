# facts_peaks_ca.csv sources

Group `peaks_ca`: 36 rows (27 BC/AB/YT peaks and ranges, 4 glaciers, 5 passes). All pages were read on
2026-09-28.

**Conversions.** Where the source figure is in feet or miles, the metric value comes straight from that
figure: 1 ft = 0.3048 m (1 decimal), 1 mi = 1.609344 km (2 decimals), 1 sq mi = 2.589988 km² (2 decimals).
This covers the WA passes, Blue, Easton and Emmons glaciers. Canadian sources (bivouac, CRDB, BC Parks,
Parks Canada, GVP) are metric and are copied as whole metres.

**Abbreviations.**
- WP = English Wikipedia, read through the MediaWiki API (article wikitext and infobox).
- Biv = bivouac.com mountain page (`https://bivouac.com/MtnPg.asp?MtnId=<id>`), which gives height, key
  saddle, prominence and first ascent. Its heights come from BC TRIM mapping.
- CRDB = Canadian Rockies Databases (`https://cdnrockiesdatabases.ca/peaks/<id>`), the source behind WP's
  `{{cite crdb}}`.
- BCGNIS = BC Geographical Names (`https://apps.gov.bc.ca/pub/bcgnws/names/<id>.html`).
- MP = Mountain Project.
- GVP = Smithsonian Global Volcanism Program. Its site returned "temporarily unavailable" (HTTP 403)
  today, so GVP figures are quoted as WP cites them.
- peakbagger.com was behind a Cloudflare block and was not used.

**Rules I followed.**
- **Elevation:** the most widely published figure, usually the one WP cites, which matches the blurb.
  Biv's TRIM height is used where it looks better, and differences are noted below.
- **Prominence:** from Biv or WP. It can be a few metres off the chosen elevation because the two come
  from different surveys.
- **range:** "Major range (subrange)". Canadian Rockies peaks get a subrange only where it is uncontested
  and fits in 40 characters.
- **Omitted:** `first_ascent` where sources disagree, `classic` where no graded signature route could be
  sourced, and `last_eruption` unless it is a dated, established event.

---

## BC / Alberta / Yukon peaks

### Black Tusk
- elevation_m `2319`, prominence_m `569`: Biv 31 (Height 2319 m, prominence 569 m). WP https://en.wikipedia.org/wiki/The_Black_Tusk gives the same (it cites Biv).
- first_ascent `1912, William J. Gray & party`: BCGNIS 5708 ("First ascent, 1912, credited to a party led by William J. Gray"). Biv 31 gives "1912 W. Gray" and WP gives "1912 by William J. Gray and party".
- type `eroded stratovolcano`, rock `andesite`: WP geology section says "remnant of an extinct andesitic stratovolcano" and describes glacial dissection. NRCan, quoted on WP, calls it the hard lava core left after the cinder cone eroded.
- range `Coast Mountains (Garibaldi Ranges)`: WP lead ("Garibaldi Ranges of the Coast Mountains").
- last_eruption omitted: WP says the summit dome formed about 170,000 years ago, but that sentence has no citation.

### Castle Mountain
- elevation_m `2850`, prominence_m `168`: Biv 1536 (Height 2850 m, key saddle 2682 m, prominence 168 m). Biv notes the highest point is on the NW part of the ridge, higher than Eisenhower Tower.
  - **Discrepancy:** WP https://en.wikipedia.org/wiki/Castle_Mountain and CRDB 225 give **2766 m**. I used 2850 m because two elevation models show the massif rises well above 2766 m near Biv's summit point (51.327, -115.967).
  - Copernicus 90 m DEM via api.open-meteo.com: 2816 m.
  - SRTM 30 m via api.opentopodata.org: highest point 2828 m. SRTM normally reads low on summits.
  - WP's prominence of 168 m is Biv's figure paired with the 2850 m height, not with 2766 m.
- first_ascent `1884, Arthur P. Coleman`: CRDB 225 (Ascent Date 1884, Arthur Coleman) and Biv 1536.
- classic `Brewer Buttress, II 5.6, 13 pitches`:
  - MP https://www.mountainproject.com/route/106073047/brewer-buttress ("5.6 PG13", "Trad, Alpine, 13 pitches, Grade II").
  - Biv 1536 ("Brewer's Buttress 5.6, II, 13p, 380m, trad", citing Dougherty's *Selected Alpine Climbs*).
- rock `limestone`: CRDB 225 ("its two major cliffs of limestone being separated by a ledge" of shale).
- range `Canadian Rockies`: WP's infobox says "Sawback Range", but CRDB and the WP text call Castle the easternmost peak of the Main Ranges. Because of that conflict I left out a subrange.

### Golden Hinde
- elevation_m `2195`, prominence_m `2195`: WP https://en.wikipedia.org/wiki/Golden_Hinde_(mountain), citing peaklist.org. It is an island high point, so prominence equals elevation. Biv 1364 gives 2197 m for both.
- range `Vancouver Island Ranges`: WP.
- first_ascent `1913, Einar Anderson & party`: WP lead ("first ascended in 1913"). Biv 1364 gives "1913 Einar Anderson, W.R. Kent, W.W. Urquhart, 1913 or 1914", and the WP infobox also says "1913 or 1914".
- rock `basalt`: WP ("made of basalt which is part of the Karmutsen Formation").
- tagline omitted: "highest on Vancouver Island" would give the location away, and the blurb already says it.

### Grouse Mountain
- elevation_m `1231`, prominence_m `86`: Biv 565 (1231 m; key saddle 1145 m; prominence 86 m). WP https://en.wikipedia.org/wiki/Grouse_Mountain also gives 1231 m.
- type `ski area`, range `Coast Mountains (North Shore Mountains)`: WP lead ("one of the North Shore Mountains of the Pacific Ranges ... the site of an alpine ski area, Grouse Mountain Resort").

### Ha Ling Peak
- elevation_m `2408`: CRDB 593 (2408 m) and Biv 1555 (2408 m). WP https://en.wikipedia.org/wiki/Ha_Ling_Peak still shows an older CRDB value of 2407 m.
- prominence_m `31`: Biv 1555.
- range `Canadian Rockies`: WP. CRDB calls it a named high point on Mount Lawrence Grassi.
- first_ascent omitted: CRDB tells the 1896 Ha Ling bet story from the Medicine Hat News, but it also cites a rival account that credits Lee Poon. It never presents either as a documented first ascent.

### Mount Alberta
- elevation_m `3619`, prominence_m `819`: CRDB 13 (3619 m) and Biv 3 (3619 m, 819 m above Woolley Pass). WP https://en.wikipedia.org/wiki/Mount_Alberta agrees.
- first_ascent `1925, Yuko Maki's Japanese party`:
  - CRDB 13: Ascent Party S. Hashimoto, H. Hatano, T. Hayakawa, Y. Maki, Y. Mita, N. Okabe; Guides Hans Fuhrer, H. Kohler, J. Weber.
  - WP: "headed by Yūkō Maki".
- classic `Japanese Route, V 5.6`:
  - WP route list ("Japanese Route (Normal Route) V 5.6").
  - https://stevensong.com/canadian-rockies/icefield-parkway/mount-alberta/ ("goes at an alpine grade of V, a dozen pitches up to 5.6").
  - MP https://www.mountainproject.com/route/126047112/japanese-route agrees on 5.6 but says Grade IV, from a thin two-vote entry.
- range `Canadian Rockies`: CRDB and WP place it in the Winston Churchill Range. "Canadian Rockies (Winston Churchill Range)" is longer than 40 characters, so I left out the subrange.

### Mount Cayley
- elevation_m `2385`: WP https://en.wikipedia.org/wiki/Mount_Cayley (citing Kelman 2005 PhD thesis) and Biv 36 (2385 m).
- prominence_m `674`: Biv 36.
- type `stratovolcano`: WP ("an eroded but potentially active stratovolcano").
- range `Coast Mountains (Pacific Ranges)`: WP.
- first_ascent `1928, E. C. Brooks & party`: WP infobox ("1928 by E. C. Brooks, W. G. Wheatley, B. Clegg, R. E. Knight and T. Fyles"). Biv 36 gives "1928 E. Brooks; T. Fyles; W. Wheatley".

### Mount Columbia
- elevation_m `3747`: CRDB 296 (3747 m) and WP https://en.wikipedia.org/wiki/Mount_Columbia_(Canada). Biv 1 gives 3741 m.
- prominence_m `2383`: Biv 1 ("2383 m above Crowsnest Pass"), also on WP.
- tagline `Highest point in Alberta`: WP. Biv 1 ranks it "#1 on the Height List for Alberta".
- first_ascent `1902, James Outram & Christian Kaufmann`: CRDB 296 (Ascent Party James Outram, Guide Christian Kaufmann). Biv 1 agrees.
- range `Canadian Rockies`: CRDB and WP give the Winston Churchill Range. I left the subrange out because it is too long (see Mount Alberta).

### Mount Edith Cavell
- elevation_m `3363`: CRDB 415. Biv 8 gives 3361 m.
- prominence_m `2007`: WP https://en.wikipedia.org/wiki/Mount_Edith_Cavell. This equals 3363 minus Biv's 1356 m key saddle at Fortress Pass; Biv's own figure is 2005 m against its 3361 m height.
- first_ascent `1915, A. J. Gilmour & E. W. D. Holway`: CRDB 415 and Biv 8.
- classic `North Face, IV 5.7`:
  - MP https://www.mountainproject.com/route/105941738/north-face-chouinardbeckeydoody ("5.7", "5000 ft (1515 m), 12 pitches, Grade IV", FA Chouinard, Beckey, Doody 1961).
  - Mont Blanc Lines route poster https://www.montblanclines.com/products/mount-edith-cavell-north-face ("North Face Direct: TD 5.7", FA Beckey, Chouinard, Doody, 07/1961).
  - WP's route list gives "North Face, East Summit: IV, 5.8". I kept 5.7 because two sources give it.

### Mount Edziza
- elevation_m `2786`: WP https://en.wikipedia.org/wiki/Mount_Edziza (citing GVP and Souther 1990). Biv 3083 gives 2793 m.
- prominence_m `1763`: Biv 3083 ("above Mess Pass"). It is computed from Biv's 2793 m height.
- type `stratovolcano`: WP Geology section ("the central trachyte stratovolcano of Mount Edziza"). The wider Mount Edziza volcanic complex is described in the blurb.
- range `Tahltan Highland`: WP (citing Dept. of Energy, Mines and Resources 1989).
- last_eruption omitted: WP https://en.wikipedia.org/wiki/Mount_Edziza_volcanic_complex says the latest eruptions "took place in the last 11,000 years but none of them have been precisely dated".

### Mount Meager
- The row is the Mount Meager **massif**, as the blurb says.
- elevation_m `2680`: this is the massif's high point, Plinth Peak. WP https://en.wikipedia.org/wiki/Mount_Meager_massif (citing GVP and GSC) and Biv 952 (Plinth Peak 2677 m). Mount Meager peak itself is 2650 m (Biv 953).
- type `volcanic complex`: WP (infobox "formed_by: Complex volcano"; the lead calls it a group of eroded volcanic edifices).
- last_eruption `c. 2,400 years ago`: WP lead ("About 2,400 years ago, an explosive eruption formed a volcanic crater on its northeastern flank"). The WP infobox, citing GVP, gives 410 BCE ± 200 years.
- range `Coast Mountains (Pacific Ranges)`: WP.
- first_ascent and prominence omitted because both belong to individual summits.

### Mount Price
- elevation_m `2049`: WP https://en.wikipedia.org/wiki/Mount_Price_(British_Columbia) (citing GVP Garibaldi Lake subfeatures). Biv 619 gives 2052 m.
- prominence_m `402`: Biv 619.
- type `stratovolcano`, rock `andesite & dacite`: WP ("a small stratovolcano"; infobox geology "Andesite and dacite").
- first_ascent `1912, BC Mountaineering Club party`: Biv 619 ("1912 BCMC Party"). This is the only source.
- range `Coast Mountains (Garibaldi Ranges)`: WP.
- last_eruption omitted: WP gives only a window ("between 15,000 and 8,000 years ago").

### Mount Sir Douglas
- elevation_m `3406`: CRDB 1259 and WP https://en.wikipedia.org/wiki/Mount_Sir_Douglas. Biv 71 gives 3411 m.
- prominence_m `1141`: Biv 71, current page ("above South Kananaskis Pass"). WP's 1110 m cites an older 2010 reading of the same Biv page.
- first_ascent `1919, J.W.A. Hickson & Edward Feuz Jr.`: CRDB 1259 (Ascent Party J.W.A. Hickson, Guide Edward Feuz jr.) and Biv 71.
- range `Canadian Rockies`: WP's subrange field lists Spray Mountains / Park Ranges together, so I left out a subrange.
- **Blurb issue:** the blurb calls this "Kananaskis's highest summit". WP https://en.wikipedia.org/wiki/Mount_Joffre gives 3450 m for Mount Joffre in Peter Lougheed Provincial Park (Kananaskis Country). WP's Sir Douglas infobox names Joffre as its higher parent.

### Mount Temple
- elevation_m `3544`, prominence_m `1544`: WP https://en.wikipedia.org/wiki/Mount_Temple_(Alberta) (citing Biv); this matches the blurb. The current Biv 1584 gives 3545 / 1545 and CRDB 1376 gives 3543.
- range `Canadian Rockies (Bow Range)`: WP and Biv 1584 ("Park Ranges / Bow Range").
- first_ascent `1894, Wilcox, Allen & Frissell`: CRDB 1376 ("Samuel E.S. Allen, L.F. Frissel, Walter Wilcox") and WP. The third climber is Lewis F. Frissell; CRDB, Biv and WP spell it "Frissel".
- classic `East Ridge, IV 5.7`:
  - WP route list ("East Ridge (IV 5.7)").
  - MP https://www.mountainproject.com/route/106997654/east-ridge ("5.7", Grade IV, FA Wittich & Stegmaier 1931).

### Mt Assiniboine
- elevation_m `3618`: CRDB 57 and WP https://en.wikipedia.org/wiki/Mount_Assiniboine. Biv 1479 gives 3616 m (TRIM).
- prominence_m `2086`: Biv 1479 ("above Howse Pass"), also on WP.
- first_ascent `1901, James Outram, C. Bohren, C. Hasler`: CRDB 57 (Ascent Party James Outram; Guides C. Bohren, Christian Hasler sr.) and Biv 1479.
- classic `North Ridge, II 5.5`:
  - WP (infobox "II/5.5"; text "North Ridge and North Face at YDS 5.5").
  - SummitPost route page https://www.summitpost.org/north-ridge-ii-5-5-via-bc/226304 (title "North Ridge, II, 5.5 (via BC)"). The title was seen in search results; the page itself is behind Cloudflare.
  - MP https://www.mountainproject.com/route/106995815/north-ridge says 5.4, Grade II.
- range `Canadian Rockies`: WP.
- **Blurb note:** the blurb says the summit lies on the BC side. CRDB 57 and WP both place the mountain on the Continental Divide, with Banff to the east and Mount Assiniboine Provincial Park to the west.

### Mt Begbie
- elevation_m `2733`: WP https://en.wikipedia.org/wiki/Mount_Begbie (citing peakbagger) and Biv 2225.
- prominence_m `883`: Biv 2225.
- range `Monashee Mountains`: WP.
- first_ascent `1907, Haggen, Herdman, Robertson, Feuz`: Biv 2225 ("1907 R. Haggen; J. Herdman; J. Robertson; E. Feuz Jr") and WP.

### Mt Garibaldi
- elevation_m `2678`: WP https://en.wikipedia.org/wiki/Mount_Garibaldi (citing GVP). Biv 30 gives 2675 m.
- prominence_m `855`: Biv 30.
- type `stratovolcano`, rock `dacite`: WP ("a dormant stratovolcano"; "mostly dacite").
- last_eruption `c. 10,000 years ago`: WP lead ("The latest period of volcanic activity took place about 10,000 years ago"; the Ring Creek flow from Opal Cone dates to 10,700–9,300 years ago). The WP infobox, citing GVP, gives 8060 BCE ± 500.
- first_ascent `1907, Atwell King & party`: WP. The Aug 11, 1907 party was Warren, A. T. and W. T. Dalton, Pattison, Trorey and Atwell D. King, and the Atwell Peak paragraph says King "led the first ascent". Biv 30 lists the same six names and dates it Aug 12, 1907.
- range `Coast Mountains (Garibaldi Ranges)`: WP.

### Mt Joffre (Joffre Peak, Coast Mountains)
- The pin 50.3411,-122.4456 matches Joffre Peak exactly (Biv 45 location 50.34111,-122.44556). It is not Mount Joffre in the Rockies.
- elevation_m `2721`, prominence_m `331`: Biv 45 and WP https://en.wikipedia.org/wiki/Joffre_Peak.
- range `Coast Mountains (Lillooet Ranges)`: WP and Biv 45 ("Pacific Ranges / Lillooet Ranges / Joffre Group").
- first_ascent `1957, Dick Chambers & Paddy Sherman`: WP ("July 19, 1957 by Dick Chambers and Paddy Sherman") and Biv 45. BCGNIS 34784 names a larger BCMC party of Chambers, Hutton, Scott, Mason and Sherman.
- **Blurb issues:**
  1. WP says Joffre Peak "is the second-highest point of the Joffre Group". Mount Matier, 2783 m, is the highest (https://en.wikipedia.org/wiki/Mount_Matier).
  2. The north-face couloir ski line is out of date. The May 13 and 16, 2019 rock avalanches "destroyed most of the north face and the main north couloir" (Gripped, https://gripped.com/news/major-alpine-climbs-on-north-face-of-joffre-peak-collapse/).

### Mt Logan
- elevation_m `5959`: WP https://en.wikipedia.org/wiki/Mount_Logan (1992 GSC GPS survey) and Biv 14.
- prominence_m `5250`: Biv 14 ("above Mentasta Pass") and WP.
- tagline `Highest peak in Canada`: WP ("the highest mountain in Canada").
- range `Saint Elias Mountains`: WP.
- first_ascent `1925, A. H. MacCarthy & party`: WP (June 23, 1925: MacCarthy as leader, with Lambart, Carpé, Read, Foster and Taylor). Biv 14 agrees.
- classic omitted: the normal route is the King Trench and the famous line is the 1957 East Ridge. Neither has a standard grade in the sources.
- **Blurb note:** WP says the largest base circumference "of any non-volcanic mountain". The blurb leaves out "non-volcanic".

### Mt Robson
- elevation_m `3954`, tagline `Highest peak in the Canadian Rockies`:
  - BC Parks https://bcparks.ca/mount-robson-park/ ("Standing at 3,954 m"; "the highest peak in the Canadian Rockies").
  - CRDB 1175 (3954 m).
  - Biv 2 gives 3959 m.
- prominence_m `2829`: Biv 2 ("above Yellowhead Pass") and WP https://en.wikipedia.org/wiki/Mount_Robson.
- range `Canadian Rockies (Rainbow Range)`: WP and Biv 2 ("Park Ranges / Rainbow Range (Robson)").
- first_ascent `1913, Kain, MacCarthy & Foster`: CRDB 1175 (W.W. Foster, Albert H. MacCarthy; guide Conrad Kain) and Biv 2 (July 31, 1913). WP calls it the first *documented* ascent, since Kinney's 1909 claim is disputed.
- classic `Kain Face, IV`: WP route list ("Kain Face IV"; text: "the more popular routes are the Kain route and the southeast face"). MP https://www.mountainproject.com/route/106998345/kain-face lists it as "Easy 5th AI3 Steep Snow", FA Kain, MacCarthy and Foster 1913.

### Mt Sir Donald
- elevation_m `3284`, prominence_m `874`: Biv 2377 and WP https://en.wikipedia.org/wiki/Mount_Sir_Donald.
- range `Selkirk Mountains (Sir Donald Range)`: Biv 2377 ("Selkirk Mountains / Duncan Ranges / Sir Donald Range"). WP says Selkirk Mountains.
- first_ascent `1890, Huber, Sulzer & Cooper`: Biv 2377 ("1890 Emil Huber, Carl Sulzer, Harry Cooper (porter)") and WP.
- classic `Northwest Ridge, III 5.4`:
  - SummitPost route page https://www.summitpost.org/northwest-ridge-iii-5-4/319779 (title "Northwest Ridge, III, 5.4"). The title was seen in search results; the page itself is behind Cloudflare.
  - https://drdirtbag.com/2017/08/01/sir-donald-nw-ridge-iii-5-4-2h24m45-up-4h38-rt/ ("III 5.4").
  - MP https://www.mountainproject.com/route/106090216/northwest-ridge ("5.4", but Grade IV, 2400 ft).
  - WP says the route is in *Fifty Classic Climbs of North America*.
- rock `quartzite`: Dr. Dirtbag ("a quartzite wedge whose northwest ridge rises 2300 feet from the saddle with Mount Uto").
- **Blurb note:** the blurb says "roughly 1,000 m" of scrambling. Sources give about 700–730 m for the ridge: 2,300 ft per Dr. Dirtbag, 2,400 ft per MP.

### Mt Slesse
- elevation_m `2429`, prominence_m `852`: Biv 1207 (2429 m, TRIM; 852 m "above Hannegan Pass"). PeakVisor also gives 2,429 m. WP https://en.wikipedia.org/wiki/Slesse_Mountain gives 2439 m / 862 m without a citation.
- range `North Cascades (Skagit Range)`: WP ("Skagit Range, Cascade Mountains"). WP's North Cascades article includes the BC portion.
- first_ascent `1927, Henderson, Winram & Parkes`: WP ("August 10, 1927, by Stan Henderson, Mills Winram, and Fred Parkes") and Biv 1207.
- classic `Northeast Buttress, V 5.9, 24 pitches`:
  - MP https://www.mountainproject.com/route/106108831/northeast-buttress ("5.9", "Trad, Alpine, 24 pitches, Grade V").
  - WP ("Grade V ... 5.8 or 5.9", "24 pitch", in *Fifty Classic Climbs*, FA Beckey, Marts and Bjornstad 1963).
- rock `diorite`: WP ("The primary rock comprising Slesse is grey diorite", from the Chilliwack batholith).

### Mt Waddington
- elevation_m `4019`, prominence_m `3289`: WP https://en.wikipedia.org/wiki/Mount_Waddington (TRIM map 092N034, and Biv) and Biv 21. BCGNIS 38556 gives an older "13,177 feet (4016m)".
- tagline `Highest peak entirely in British Columbia`: BCGNIS 38556 ("Mount Waddington is the highest mountain ENTIRELY within the province"; Fairweather and Quincy Adams straddle the Alaska boundary).
- range `Coast Mountains (Waddington Range)`: WP.
- first_ascent `1936, Fritz Wiessner & Bill House`: BCGNIS 38556 ("Fritz H. Weissner ... and William P. House ... 21 July 1936"), WP (South Face) and Biv 21.
- classic omitted: I found no single graded signature route.

### Sky Pilot
- elevation_m `2031`, prominence_m `1236`: Biv 582 and WP https://en.wikipedia.org/wiki/Sky_Pilot_Mountain_(British_Columbia).
- range `Coast Mountains (Britannia Range)`: WP ("the highest mountain in the Britannia Range of the Coast Mountains").
- first_ascent `1910, Basil Darling & party`: Biv 582 ("1910 Basil Darling, Hobart Dowler, Alan Morkill, J. Huggard, Grubbe (west ridge)") and WP.

### Tantalus Range
- type `range`, range `Coast Mountains (Pacific Ranges)`: WP https://en.wikipedia.org/wiki/Tantalus_Range ("a subrange of the Pacific Ranges of the Coast Mountains").
- elevation_m `2603`: this is the high point, Mount Tantalus. Biv 39 and the WP Tantalus Range infobox (citing Biv). WP's separate Mount Tantalus article says 2608 m, also citing Biv, but the current Biv page shows 2603 m.
- first_ascent and prominence omitted because both belong to the individual summit.

### The Lions
- type `twin peaks`: WP https://en.wikipedia.org/wiki/The_Lions_(peaks) ("a pair of pointed peaks"; "these twin summits").
- elevation_m `1654`, prominence_m `369`: the higher summit, West Lion. Biv 572 gives 1654 m and 369 m. BCGNIS 1935 also gives "1654m" (East Lion 1606 m).
- range `Coast Mountains (North Shore Mountains)`: WP ("along the North Shore Mountains").
- rock `hornblende diorite`: WP Geology section ("The Lions are composed of hornblende diorite"). The blurb's "granite" is loosely right, since diorite is a granitic rock.
- first_ascent omitted because the sources conflict. Biv 572 credits the West Lion to Bell-Irving and Joe Capilano in 1889. BCGNIS 1935 and WP call 1903 the first recorded ascent: Atwell King's party on the West Lion and the Latta brothers on the East Lion.

### Wedge Mountain
- elevation_m `2892`, prominence_m `2249`: Biv 34 (TRIM; "above Tokum Corners Pass"). This matches the blurb.
  - **Discrepancy:** BCGNIS 20071 ("Elevation of 9,497 feet from P.L. Tait"), WP https://en.wikipedia.org/wiki/Wedge_Mountain and the Whistler Museum all give **2895 m**. That is the older survey figure.
- first_ascent `1923, Neal Carter & Charles Townsend`: Biv 34 and the Whistler Museum https://whistlermuseum.org/2015/09/12/monthly-mountain-wedge-mountain/ ("Neal Carter and Charles Townsend made the first recorded ascent of the peak in 1923"). BCGNIS 20071 says "credited to Neal Carter, 1921"; I treat that as an error, since both other sources agree on 1923.
- range `Coast Mountains (Garibaldi Ranges)`: WP ("the highest summit in the Garibaldi Ranges and therefore also Garibaldi Provincial Park").
- tagline omitted because the claim names a park.

---

## Glaciers

### Athabasca Glacier
- type `outlet glacier`: WP https://en.wikipedia.org/wiki/Athabasca_Glacier ("one of the six principal 'toes' of the Columbia Icefield").
- area_km2 `6`:
  - Travel Alberta https://www.travelalberta.com/listings/athabasca-glacier-1996 ("approximately 6 sq km (2.3 sq mi)").
  - WP ("covers an area of 6 km2").
- length_km `6`: WP ("approximately 6 km long"). The figure is uncited on WP but repeated by travel guides. It is about right from the map: roughly 5.5–6 km from the icefield rim to the toe.
- range `Canadian Rockies (Columbia Icefield)`: WP.
- Parks Canada's archived page (https://web.archive.org/web/20060508082540/http://www.pc.gc.ca/pn-np/ab/jasper/visit/visit32_e.asp) says "retreating more than 1.5 kms", which supports the blurb.

### Blue Glacier
- type `mountain glacier`: WP https://en.wikipedia.org/wiki/Blue_Glacier (infobox type).
- length_km `4.18`: from NPS https://www.nps.gov/olym/learn/nature/glaciers.htm ("The Blue Glacier, a 2.6-mile long glacier that descends from 7,980-foot Mount Olympus"), so 2.6 mi × 1.609344. WP gives 2.7 mi for the year 2000.
- range `Olympic Mountains (Mount Olympus)`: WP and NPS.
- area omitted because the sources conflict:
  - WP: 1.7 sq mi (4.40 km²), citing a Carleton College student report.
  - The classic *Journal of Glaciology* flow study (via web search): 4.3 km².
  - Fountain et al. 2022, JGR Earth Surface: 6.02 ± 0.30 km².

### Easton Glacier
- type `mountain glacier`: WP https://en.wikipedia.org/wiki/Easton_Glacier (infobox type).
- length_km `4.02`: WP infobox "2.5 mi", so 2.5 × 1.609344.
  - **Lower confidence:** WP gives no citation for this figure.
  - It fits the North Cascade Glacier Climate Project's elevation span, "from the slopes near Sherman Crater at 2950 m to the terminus at 1700 m" (https://glaciers.nichols.edu/easton/).
- range `North Cascades (Mount Baker)`: WP ("on Mount Baker in the North Cascades").
- area omitted because I found no per-glacier area in NCGCP or NPS pages.

### Emmons Glacier
- area_km2 `11.14`, tagline `Largest glacier in the contiguous US`: from NPS https://www.nps.gov/mora/learn/nature/glaciers.htm ("The Emmons Glacier has the largest area (4.3 square miles) ... of all glaciers in the contiguous 48 states"), so 4.3 sq mi × 2.589988. The USGS fact sheet https://wa.water.usgs.gov/pubs/fs/fs_rainier.html makes the same claim.
- type `mountain glacier`: WP https://en.wikipedia.org/wiki/Emmons_Glacier (infobox type).
- range `Cascade Range (Mount Rainier)`: WP and NPS.
- length omitted because the sources conflict: WP's infobox says "3.9 mi estimated" without a citation, and a web-search result gives 4.55 mi (2021).

---

## Passes

### Cascade Pass
- elevation_m `1643.5`: from 5,392 ft, given by WTA https://www.wta.org/go-hiking/hikes/cascade-pass ("Highest Point: 5,392 feet") and WP https://en.wikipedia.org/wiki/Cascade_Pass. The USGS EPQS 1 m DEM reads 5,321 ft at the rounded WP coordinate, which is consistent.
- type `trail pass`: WP ("crossed by only a hiking trail"). NPS https://www.nps.gov/places/cascade-pass-trail.htm describes the trail.
- range `North Cascades`: WP ("inside North Cascades National Park").

### Rogers Pass
- elevation_m `1330`, built `rail 1885, highway 1962`: Parks Canada https://parks.canada.ca/pn-np/bc/glacier/nature/controle-avalanche-control/fact
  - "Rogers Pass is 4,364 ft (1,330m) above sea level and is the third highest point along the Trans-Canada Highway."
  - "First with the railway, completed in 1885 ... Then, the Trans-Canada Highway which opened in 1962."
  - The same page's "1,315m" refers to the snowfall station, not the pass.
- road `Trans-Canada Highway (Hwy 1)`: Parks Canada, and WP https://en.wikipedia.org/wiki/Rogers_Pass_(British_Columbia) (BC Highway 1).
- range `Selkirk Mountains`: WP.

### Snoqualmie Pass
- elevation_m `921.1`: from 3,022 ft, WSDOT mountain-pass data (https://wsdot.com/Travel/Real-time/Service/api/MountainPass: "Snoqualmie Pass I-90", elevation 3022 Feet; the same data drives https://wsdot.com/travel/real-time/mountainpasses/snoqualmie). This matches the blurb. WP https://en.wikipedia.org/wiki/Snoqualmie_Pass uses GNIS's 3,015 ft.
- road `I-90`, range `Cascade Range`: WP and WSDOT.

### Stevens Pass
- elevation_m `1237.8`: from 4,061 ft, WSDOT mountain-pass data ("Stevens Pass US 2", 4061 Feet). WP https://en.wikipedia.org/wiki/Stevens_Pass agrees.
- road `US 2`, range `Cascade Range`: WP and WSDOT.

### Washington Pass
- elevation_m `1669.4`: from 5,477 ft, WSDOT mountain-pass data ("North Cascade Hwy SR 20", 5477 Feet). WP https://en.wikipedia.org/wiki/Washington_Pass also gives "el. 5477 ft".
- road `SR 20 (North Cascades Hwy)`, range `North Cascades`: WP.
- built `opened 1972`: WP https://en.wikipedia.org/wiki/Washington_State_Route_20 ("a new route across Washington Pass, which was opened in 1972"; "officially opened on September 2, 1972").
