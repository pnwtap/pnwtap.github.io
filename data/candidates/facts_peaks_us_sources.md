# facts_peaks_us — sources

Researched 2026-09-28 for the 46 `peaks_us` rows. Peakbagger, listsofjohn, SummitPost and the
Smithsonian GVP site all served Cloudflare/403 blocks, so peakbagger and GVP figures are taken
**as quoted in Wikipedia** (infobox refs name the peakbagger pid / NGS PID / GVP number). Direct
checks used USGS volcano pages, USGS CVO, NGS datasheets, Mountain Project (MP) route pages and WTA.

**Conventions**

- `ft→m` means a feet source converted as ft × 0.3048, rounded half-up to **one decimal**, so the
  game's imperial display returns the source number (e.g. 14,410 ft → 4392.2). Values from natively
  metric sources (NGS datasheets, USGS metric text) are written as given (e.g. NGS 1716.9 m).
- Elevation: the Wikipedia infobox figure by default (mostly peakbagger/NGS). Exceptions (infobox
  figure is a contour floor, unsourced, contested or outdated) are named in the row.
- Prominence: Wikipedia infobox (peakbagger). Where the infobox has none, the rendered tables of
  Wikipedia's [List of mountain peaks of Oregon](https://en.wikipedia.org/wiki/List_of_mountain_peaks_of_Oregon) /
  [List of mountain peaks of Washington](https://en.wikipedia.org/wiki/List_of_mountain_peaks_of_Washington)
  (peakbagger, retrieved 2016/2020). Those lists run about 15–40 ft higher than the infoboxes for the
  same peaks (NAVD88 adjustment and a different retrieval date). This is noted, not "fixed".
- `range`: "North Cascades" is used for peaks north of US 2 / Stevens Pass, the boundary used by
  Wikipedia's [North Cascades](https://en.wikipedia.org/wiki/North_Cascades) article (which follows
  Beckey and peakbagger and names Glacier Peak as a North Cascades volcano). Peaks south of US 2
  use "Cascade Range", except the "Stuart Range" pair. "Oregon Cascades" is the term used in
  Wikipedia's Oregon peak list for the Cascades in Oregon.
- `classic` is written as "route, commitment grade + difficulty". The grade and pitch count come from
  the cited MP route page. Pitches are added only for multipitch rock routes. "Signature" status is
  backed by the row's blurb, Wikipedia, a Fifty Classics listing or an MP "most popular/standard"
  statement, as noted per row.
- `last_eruption` is given only where USGS and GVP agree (Hood, St Helens, Newberry, Three Sisters).
  It is left out where they conflict: Rainier (GVP 1450 vs USGS "about 1,000 years ago"), Baker (GVP 1880 vs
  USGS 6,700 yr), Glacier Peak (GVP 1700 vs USGS 1,100 yr), Adams (GVP 950 CE vs USGS 3,800 yr),
  Jefferson (GVP 950 CE vs USGS ~15,000 yr) and Bachelor (GVP 5800 BC vs USGS ~9,500 yr). It is also
  left out for extinct or eroded cones.
- USGS volcano quick-facts pages used: https://www.usgs.gov/volcanoes/mount-rainier ,
  …/mount-baker , …/glacier-peak , …/mount-adams , …/mount-st.-helens , …/mount-hood ,
  …/mount-jefferson , …/three-sisters , …/newberry , …/mount-bachelor
- USGS CVO first ascents: https://volcanoes.usgs.gov/observatories/cvo/Historical/first_ascents_and_discoveries.shtml
- NGS datasheets: https://geodesy.noaa.gov/cgi-bin/ds_mark.prl?PidBox=PID

## Rows

- **Broken Top**: https://en.wikipedia.org/wiki/Broken_Top
  - elevation 9,177 ft (infobox, Hildreth 2007 USGS) ft→m 2797.1. The Oregon list gives 9,180 ft (NAVD88).
  - prominence 2,195 ft (Oregon list; the infobox has none) ft→m 669.0.
  - type: "glacially eroded complex stratovolcano" (lead).
  - first_ascent 1910, Thomas Eliot, Harley Prouty & Charles Whittlesey: MP NW Ridge FA (https://www.mountainproject.com/route/108309829/northwest-ridge) and fr.wikipedia infobox and text (https://fr.wikipedia.org/wiki/Broken_Top).
  - classic: MP Northwest Ridge, "Easy 5th", Grade II. The MP area page says "The standard route is the Northwest ridge, class 4 or 5 easy" (https://www.mountainproject.com/area/108309793/broken-top). Wikipedia says class 4 to low 5th.
- **Chair Peak**: https://en.wikipedia.org/wiki/Chair_Peak
  - elevation 6,238 ft and prominence 878 ft (peakbagger pid 2103) ft→m 1901.3 / 267.6.
  - first_ascent: infobox (Beckey, *Cascade Alpine Guide*).
  - classic: MP Northeast Buttress: 5.4, AI2-3, M1-2, Grade III, 4 pitches; MP calls it "A popular winter climb" (https://www.mountainproject.com/route/107989626/northeast-buttress). The row's blurb also names it.
- **Cutthroat Peak**: https://en.wikipedia.org/wiki/Cutthroat_Peak
  - elevation 8,066 ft and prominence 1,766 ft (listsofjohn 48864 via infobox) ft→m 2458.5 / 538.3. The WA list gives 8,054 / 1,750 ft.
  - range: North Cascades (infobox lists Okanagan Range / North Cascades).
  - first_ascent July 22, 1937, Kenneth Adam & Raffi Bedayn (Beckey vol. 3 p. 302).
  - classic: MP South Buttress, 5.8, Grade III, 12 pitches, FA Beckey & Gordon 1958 (https://www.mountainproject.com/route/109326651/south-buttress).
- **Dragontail Peak**: https://en.wikipedia.org/wiki/Dragontail_Peak
  - elevation "8,840+ ft" NGVD29 (a contour floor, peakbagger 2179) ft→m 2694.4. The WA list gives an interpolated 8,865 ft (NAVD88).
  - prominence 1,760 ft ft→m 536.4.
  - range: "a mountain in the Stuart Range" (lead).
  - classic: MP Backbone Ridge, 5.9, Grade IV, 12 pitches (https://www.mountainproject.com/route/106073405/backbone-ridge).
    - The row's blurb names both Backbone Ridge and Serpentine Arête. MP gives Serpentine Arête IV 5.8, 13 pitches (https://www.mountainproject.com/route/106015955/serpentine-arete), so either could be used.
  - No first ascent: the WA list gives only a year (1937), with no party.
- **Eagle Cap**: https://en.wikipedia.org/wiki/Eagle_Cap
  - elevation 9,577 ft and prominence 1,212 ft (peakbagger 3167) ft→m 2919.1 / 369.4. The Oregon list gives prominence 1,211.
  - range: Wallowa Mountains.
- **Eldorado Peak**: https://en.wikipedia.org/wiki/Eldorado_Peak
  - elevation 8,872.9 ft ±30 cm: Gilbertson et al. 2025 survey of the rock summit now that the ice cap has melted (the infobox figure). ft→m 2704.5. The WA list gives 8,873.
  - prominence 2,188 ft (peakbagger 1846) ft→m 666.9.
  - first_ascent Aug 27, 1933, Donald Blair, Norval Grigg, Arthur Winder, Arthur Wilson (infobox, Mountaineer Annual). MP gives the same party.
  - classic: MP East Ridge, Easy Snow, Grade II (https://www.mountainproject.com/route/108131635/east-ridge).
- **Forbidden Peak**: https://en.wikipedia.org/wiki/Forbidden_Peak
  - elevation 8,815 ft NGVD29 and prominence 1,055 ft (peakbagger 1849) ft→m 2686.8 / 321.6.
  - first_ascent June 1, 1940, Lloyd Anderson, Fred & Helmy Beckey, Jim Crooks, Dave Lind (Beckey vol. 2 p. 322; MP gives the same).
  - classic: MP West Ridge, 5.6, Grade III (https://www.mountainproject.com/route/106450596/west-ridge). Wikipedia's [Fifty Classic Climbs list](https://en.wikipedia.org/wiki/Fifty_Classic_Climbs_of_North_America) gives "II 5.6". MP's grade is used.
- **Glacier Peak**: https://en.wikipedia.org/wiki/Glacier_Peak + USGS glacier-peak
  - elevation 10,541 ft (USGS quick facts, "3,213 m / 10,541 ft"; also the Wikipedia body) ft→m 3212.9. The infobox's "10,525+" is a contour floor (peakbagger 1972). The WA list gives 10,545 (NAVD88).
  - prominence 7,498 ft (peakbagger via infobox) ft→m 2285.4.
  - type: USGS "Stratovolcano".
  - range: North Cascades (the North Cascades article names it).
  - Omitted: last_eruption (GVP 1700 vs USGS 1,100 years ago). Also first_ascent: the infobox says 1898 and the body says 1897 (both cite Beckey), and MP says June 1897. A search result also reports that the 1897 USGS party may have reached a sub-summit in fog.
- **Goat Rocks** (high point Gilbert Peak): https://en.wikipedia.org/wiki/Goat_Rocks + https://en.wikipedia.org/wiki/Gilbert_Peak_(Washington)
  - elevation 8,184 ft and prominence 3,664 ft (Gilbert Peak, peakbagger 2337) ft→m 2494.5 / 1116.8. USFS rounds it to 2,500 m. The WA list gives 8,188 / 3,684.
  - type: "extinct stratovolcano" (Goat Rocks lead).
  - first_ascent: Gilbert Peak 1899, Fred G. Plummer (Goat Rocks article, Beckey p. 72).
- **Granite Mountain**: https://en.wikipedia.org/wiki/Granite_Mountain_(King_County,_Washington)
  - elevation from NGS SX1579 "Granite Mtn": NAVD88 1716.9 m (5,633 ft), natively metric.
  - prominence 1,149 ft (peakbagger 2119) ft→m 350.2.
- **Hurricane Hill**: https://en.wikipedia.org/wiki/Hurricane_Hill
  - elevation 5,757 ft and prominence 707 ft (peakbagger 907) ft→m 1754.7 / 215.5.
  - range: Olympic Mountains.
- **Jove Peak**: https://en.wikipedia.org/wiki/Jove_Peak
  - elevation 6,007 ft and prominence 647 ft (peakbagger 24528) ft→m 1830.9 / 197.2.
  - range: North Cascades (infobox; north of Stevens Pass).
- **Mount Bachelor**: https://en.wikipedia.org/wiki/Mount_Bachelor + USGS mount-bachelor
  - elevation 9,068 ft (NGS PB0762 and USGS "2,764 m / 9,068 ft") ft→m 2763.9.
  - prominence 2,685 ft (Oregon list; the infobox has none) ft→m 818.4.
  - type: USGS "Stratovolcano".
- **Mount Hood**: https://en.wikipedia.org/wiki/Mount_Hood + USGS mount-hood
  - elevation 11,249 ft (infobox, NGS RC2244 as retrieved in 2008) ft→m 3428.7. The current NGS RC2244 datasheet shows 3428.9 m / 11,250 ft (VERTCON3), and USGS quick facts show 3,426 m / 11,240 ft (legacy).
  - prominence 7,706 ft (peakbagger 2382; the Oregon list agrees) ft→m 2348.8.
  - tagline: "the highest mountain in the U.S. state of Oregon" (lead).
  - first_ascent July 11, 1857, Henry Pittock, W. L. Chittenden, Wilbur Cornell, Rev. T. A. Wood (infobox, McNeil 1937). USGS CVO lists Dryer's 1854 ascent only as "one claim", and MP credits Chittenden & Dierdorff, Aug 6 1857.
  - classic: MP South Side Route (Hogsback), AI1 Easy Snow, Grade II (https://www.mountainproject.com/route/105792904/south-side-route). The Hogsback is named in the Wikipedia climbing section.
  - last_eruption: USGS "1865 AD"; GVP 322010 (via infobox) 21 Sep 1865 – Jan 1866.
- **Mount Jefferson**: https://en.wikipedia.org/wiki/Mount_Jefferson_(Oregon) + USGS mount-jefferson
  - elevation 10,502 ft NAVD88 (peakbagger 2401, 2019) ft→m 3201.0. USGS quick facts give 3,199 m / 10,495 ft, which is the figure in the row's blurb.
  - prominence 5,777 ft (peakbagger 2019) ft→m 1760.8. The Oregon list (2016) gives 5,797.
  - first_ascent Aug 12, 1888, Ray L. Farmer & E. C. Cross (USGS CVO and Wikipedia).
  - classic: MP Jefferson Park Glacier, 5.2 (summit pinnacle), Mod. Snow (https://www.mountainproject.com/route/106666868/jefferson-park-glacier).
    - Timberline Mountain Guides: "The Jefferson Park Glacier is the quintessential alpine climb of the Oregon Cascades" (https://timberlinemtguides.com/trip/jefferson-park-glacier/).
    - Web sources describe the Whitewater Glacier as the most-travelled route, so "classic" here means signature, not busiest.
- **Mount McLoughlin**: https://en.wikipedia.org/wiki/Mount_McLoughlin
  - elevation 9,493 ft (Wikipedia text, cited to NGS NZ1067) ft→m 2893.5. Other figures: Harris 2005 gives 9,496; the Oregon list gives 9,499 (NGVD29 +4.28 ft to NAVD88); the blurb says 9,495.
  - prominence 4,475 ft (infobox and Oregon list agree) ft→m 1364.0.
  - first_ascent 1858, Joseph Burpee and five others from Jacksonville (LaLande 1995 p. 42).
- **Mount Si**: https://en.wikipedia.org/wiki/Mount_Si
  - elevation 4,167 ft NGVD29 and prominence 247 ft (peakbagger 2087) ft→m 1270.1 / 75.3.
- **Mount Thielsen**: https://en.wikipedia.org/wiki/Mount_Thielsen
  - elevation from NGS PC0809 "Mt Thielsen": NAVD88 2799.5 m (9,185 ft), natively metric. The infobox gives 9,184 ft.
  - prominence 3,342 ft (peakbagger 2441, 2008) ft→m 1018.6. The Oregon list (2016) gives 3,362.
  - type: "extinct shield volcano" (lead).
  - first_ascent 1883, E. E. Hayden (infobox via skimountaineer.com). MP West Ridge FA "Ensign Hayden (1883)".
  - classic: MP West Ridge, 4th class (https://www.mountainproject.com/route/109205359/west-ridge).
- **Mount Washington (Oregon)**: https://en.wikipedia.org/wiki/Mount_Washington_(Oregon)
  - elevation 7,795 ft (Wood & Kienle 1990; Hildreth 2007) ft→m 2375.9. No prominence source.
  - type: Wikipedia says "deeply eroded volcano" with "a volcanic plug occupying its summit cone"; MP says "an eroded volcanic plug".
  - first_ascent Aug 26, 1923, six Bend boys: Ervin McNeal, Phil Philbrook, Armin Furrer, Wilbur Watkins, Leo Harryman, Ronald Sellars (Wikipedia; MP "1923 by E. McNeal and party").
  - classic: MP North Ridge, 5.3, 2 pitches (https://www.mountainproject.com/route/106204660/north-ridge). The MP area page says "the most popular is the North Ridge route" (https://www.mountainproject.com/area/106204644/mt-washington).
- **Mt Adams**: https://en.wikipedia.org/wiki/Mount_Adams_(Washington) + USGS mount-adams
  - elevation from NGS SB1004 "Mount Adams": NAVD88 3743.4 m (12,281 ft), natively metric. USGS quick facts give 3,742 m / 12,277 ft.
  - prominence 8,116 ft (peakbagger via infobox) ft→m 2473.8. The WA list gives 8,136.
  - first_ascent late Aug/early Sep 1854, A. G. Aiken, Edward J. Allen, Andrew J. Burge (USGS CVO; Wikipedia).
  - classic: MP South Spur, Easy Snow, "easiest route on the mountain" (https://www.mountainproject.com/route/105883004/south-spur).
- **Mt Baker**: https://en.wikipedia.org/wiki/Mount_Baker + USGS mount-baker
  - elevation 10,786 ft NAVD88 (peakbagger via infobox; the WA list agrees) ft→m 3287.6. USGS quick facts give 3,286 m / 10,781 ft.
  - prominence 8,812 ft ft→m 2685.9. The WA list gives 8,845.
  - range: the lead says "in the Cascade Volcanic Arc and the North Cascades".
  - first_ascent Aug 17, 1868, Edmund T. Coleman, John Tennant, Thomas Stratton, David Ogilvy (Wikipedia; USGS CVO).
  - classic: MP Coleman/Deming Glacier, Mod. Snow, Grade II (https://www.mountainproject.com/route/105920598/colemandeming-glacier).
- **Mt Constance**: https://en.wikipedia.org/wiki/Mount_Constance
  - elevation 7,756 ft and prominence 1,956 ft (peakbagger 1022) ft→m 2364.0 / 596.2. The WA list gives 7,759 / 1,976.
  - first_ascent: 1922, Robert Schellin & A. E. Smith (infobox and body; not cited inline).
- **Mt Daniel**: https://en.wikipedia.org/wiki/Mount_Daniel
  - elevation "7,960+ ft" NGVD29 (West Summit, 1965 USGS topo, peakbagger 2132) ft→m 2426.2.
    - Eric Gilbertson's 2023 survey measured the main (west) summit at 7,972.5 ft (https://www.countryhighpoints.com/mt-daniel-survey/).
    - The WA list's "NW summit 7,904 ft" comes from NGS mark SX1207 "DANIELS", whose height is map-scaled, so it was not used.
  - prominence 3,480 ft ft→m 1060.7.
  - first_ascent: "first known ascent … by The Mountaineers 1925 outing", via Lynch Glacier (Beckey).
- **Mt Herman**: https://en.wikipedia.org/wiki/Mount_Hermann
  - The official name is **Mount Hermann**; "Mount Herman" is a recorded variant. The Wikipedia coords 48.86624,-121.702476 match the row's pin.
  - elevation "6,240+ ft" and prominence 1,120 ft (peakbagger 24825 "Mount Herman") ft→m 1902.0 / 341.4.
  - range: North Cascades (Skagit Range).
- **Mt Olympus**: https://en.wikipedia.org/wiki/Mount_Olympus_(Washington)
  - elevation from NGS SY1857 "Mt Olympus": NAVD88 2432.4 m (7,980 ft), natively metric.
  - prominence 7,838 ft (peakbagger 950; the WA list agrees) ft→m 2389.0.
  - first_ascent 1907, L. A. Nelson and party (*Climber's Guide to the Olympic Mountains* 1988 p. 163). An 1890 O'Neil party is presumed to have reached the south peak.
  - classic: MP "North Ridge via Blue Glacier", 5.3, Grade II (https://www.mountainproject.com/route/109143016/blue-glacier).
- **Mt Pilchuck**: https://en.wikipedia.org/wiki/Mount_Pilchuck
  - elevation 5,344 ft and prominence 2,860 ft (peakbagger 1798) ft→m 1628.9 / 871.7.
  - range: North Cascades (north of US 2, per the North Cascades article; the infobox just says "Cascades").
- **Mt Rainier**: https://en.wikipedia.org/wiki/Mount_Rainier + USGS mount-rainier
  - elevation 14,410 ft: the official NPS/USGS figure (Columbia Crest, NGVD29 1956; USGS quick facts "4,392 m / 14,410 ft") ft→m 4392.2. Other figures:
    - The Wikipedia infobox now shows 14,406 ft (2025, NAVD88; Gilbertson 2025 / Beason & Kenyon 2026), because the melted crest is no longer the high point.
    - Gilbertson gives 14,399.6 ft NGVD29.
    - The WA list gives 14,417 ft (NAVD88).
  - prominence 13,210 ft (infobox) ft→m 4026.4. The WA list gives 13,246.
  - tagline: "the most heavily glaciated peak in the lower 48 states" (cited to USGS Driedger / Topinka).
  - first_ascent Aug 17, 1870, Hazard Stevens & P. B. Van Trump (USGS CVO).
  - classic: "The normal route … is the Disappointment Cleaver Route, YDS grade II-III" (Wikipedia). MP's Ingraham Glacier–DC page gives "Mod. Snow" with no grade.
- **Mt Shuksan**: https://en.wikipedia.org/wiki/Mount_Shuksan
  - elevation 9,131 ft NGVD29 and prominence 4,411 ft (peakbagger 1630) ft→m 2783.1 / 1344.5. The WA list gives 9,135 / 4,431.
  - first_ascent Sep 7, 1906, Asahel Curtis & W. Montelius Price ("usually attributed"). C. E. Rusk credited Joseph Morovits in 1897.
  - classic: MP Fisher Chimneys, 4th class, AI1, Grade III (https://www.mountainproject.com/route/112041948/fisher-chimneys). The Fifty Classics route here is the Price Glacier (MP IV).
- **Mt St Helens**: https://en.wikipedia.org/wiki/Mount_St._Helens + USGS mount-st.-helens
  - elevation 2539 m, natively metric. USGS: "a 1982 survey … 2549.7 m (8365 ft). However, a lidar survey done in 2009 found the maximum elevation to be 2539 m (8330 ft) … erosion and loss of rimrock". The Wikipedia infobox's 8,363 ft is the 1980s figure.
  - prominence 4,593 ft (WA list, peakbagger 2020; the infobox's 4,605 is unsourced) ft→m 1399.9.
  - tagline: the 1980 eruption "is the most economically destructive volcanic event in U.S. history" (Wikipedia lead, USFS). "Costliest" is used as a paraphrase.
  - first_ascent Aug 26, 1853, Thomas J. Dryer, John Wilson, ?Drew, ?Smith (USGS CVO).
  - classic: MP Monitor Ridge, "most popular … route to the summit", Easy Snow (https://www.mountainproject.com/route/107211932/monitor-ridge).
  - last_eruption: USGS "1980, 2004–2008".
- **Mt Stuart**: https://en.wikipedia.org/wiki/Mount_Stuart
  - elevation 9,415 ft NGVD29 and prominence 5,354 ft (peakbagger 2182) ft→m 2869.7 / 1631.9.
  - range: "the highest peak in the Stuart Range" (lead).
  - classic: MP North Ridge, 5.9, Grade IV, 18 pitches (https://www.mountainproject.com/route/106050599/north-ridge). The MP area page says "The North Ridge climb on Mt. Stuart is one of the 50 North American Classic Climbs". The Wikipedia Fifty Classics list gives "III 5.9".
  - first_ascent omitted: the article says "It is not known for sure who made the first ascent". There is an 1873 "Angus McPherson" summit stick; Frank Tweedy made the first documented ascent in 1883.
- **Naches Peak**: https://en.wikipedia.org/wiki/Naches_Peak
  - elevation 6,452 ft and prominence 692 ft (peakbagger 2250) ft→m 1966.6 / 210.9.
- **Newberry Volcano** (pin and high point = Paulina Peak): https://en.wikipedia.org/wiki/Newberry_Volcano + https://en.wikipedia.org/wiki/Paulina_Peak + USGS newberry
  - elevation 7,989 ft (Paulina Peak, NGS PB0696 via Wikipedia; the Oregon list agrees) ft→m 2435.0. USGS gives 2,434 m / 7,986 ft; the Paulina Peak article gives 7,984 ft (USFS).
  - prominence 3,219 ft (Oregon list; the Paulina Peak infobox's 3,220 is unsourced) ft→m 981.2.
  - type: USGS "broad shield-shaped composite volcano".
  - last_eruption: USGS "about 1,300 years ago" (GVP 690 CE via Wikipedia).
  - tagline: "With more than 400 vents, Newberry has more individual subfeatures than any other volcano in the contiguous United States" (Wikipedia, Harris 2005 p. 167).
  - No range given: the volcano is east of the Cascade crest, and the Oregon list puts it in the Paulina Mountains.
- **Red Mountain (Snoqualmie)**: https://en.wikipedia.org/wiki/Red_Mountain_(King_County,_Washington)
  - elevation 5,890 ft and prominence 530 ft (peakbagger 2107) ft→m 1795.3 / 161.5.
  - first_ascent 1898, W. C. Mendenhall (Beckey).
- **Ruth Mountain**: https://en.wikipedia.org/wiki/Ruth_Mountain
  - elevation 7,115 ft and prominence 1,315 ft (peakbagger 1627) ft→m 2168.7 / 400.8.
  - No first_ascent: Beckey gives the year (1916) only.
- **Sahale Peak**: https://en.wikipedia.org/wiki/Sahale_Mountain
  - elevation "8,680+ ft" NGVD29 (contour floor, peakbagger 1854) ft→m 2645.7.
  - prominence 80 ft (a sub-summit of Boston Peak) ft→m 24.4.
  - first_ascent August 1897, John Charlton & Albert H. Sylvester (Beckey vol. 3 pp. 330–331).
  - classic: MP Sahale Glacier route, Grade II (https://www.mountainproject.com/route/111724517/sahale-glacier). The MP area page says "The most common of the two is the Cascade Pass/Sahale Arm route" (https://www.mountainproject.com/area/107848148/sahale-peak).
    - No class is given in the CSV because sources disagree on the summit block: MP's route page says Easy 5th (5.0 chimney), MP's area page says "easy fourth class", and the Wikipedia infobox says class 3–4.
- **Shuksan Arm**:
  - type: Wikipedia calls it "a ridge feature known as Shuksan Arm" (https://en.wikipedia.org/wiki/White_Salmon_Glacier_(Mount_Shuksan)). It is the Mt. Baker Ski Area's "Shuksan Arm backcountry area" (https://en.wikipedia.org/wiki/Mt._Baker_Ski_Area).
  - range: North Cascades.
  - No sourced high-point elevation was found, so it is omitted.
- **Silver Star Mountain**: https://en.wikipedia.org/wiki/Silver_Star_Mountain_(Okanogan_County,_Washington)
  - elevation 8,876 ft and prominence 2,436 ft (peakbagger 1914) ft→m 2705.4 / 742.5. The WA list gives 8,881 / 2,456.
  - first_ascent 1926, Lage Wernstedt (Majors 1975 p. 41).
  - classic: MP Silver Star Glacier, 4th class, Steep Snow, Grade II (https://www.mountainproject.com/route/111875736/silver-star-glacier). The MP area page says "There is a commonly done glacier route that involves some 4th/low 5th scrambling" (https://www.mountainproject.com/area/111875731/silver-star-mountain).
- **Sloan Peak**: https://en.wikipedia.org/wiki/Sloan_Peak
  - elevation 7,835 ft and prominence 3,875 ft (peakbagger 1803) ft→m 2388.1 / 1181.1.
  - first_ascent July 30, 1921, Harry Bedal & Nels Skaar via the Corkscrew (Beckey). MP spells it "Henry Bedal".
  - classic: MP Corkscrew Route, 3rd class, Grade II (https://www.mountainproject.com/route/117524006/corkscrew-route).
- **Snoqualmie Mountain**: https://en.wikipedia.org/wiki/Snoqualmie_Mountain + https://www.wta.org/go-hiking/hikes/mount-snoqualmie
  - elevation 6,278 ft (WTA "Highest Point") ft→m 1913.5. The Wikipedia infobox gives 6,270 ft, sourced only to a 1920 *The Mountaineer*. No prominence source.
  - first_ascent: "first recorded ascent was by Albert H. Sylvester in 1897 or 1898" (Majors 1975 p. 87).
- **Steamboat Rock**: https://en.wikipedia.org/wiki/Steamboat_Rock_State_Park
  - type "a basalt butte".
  - elevation 2,293 ft (GNIS 1513296) ft→m 698.9.
  - height_m: "rises 800 ft above the lake", ft→m 243.8. This is its rise above Banks Lake.
- **Steens Mountain**: https://en.wikipedia.org/wiki/Steens_Mountain
  - elevation 9,738 ft and prominence 4,373 ft (peakbagger 3338) ft→m 2968.1 / 1332.9. The Oregon list gives 4,383.
  - type "large fault-block mountain".
  - tagline: the loop road "reaches an elevation of 9,700 ft, making it the highest road in Oregon" (Wikipedia, Harney County Chamber of Commerce).
  - No range given: the article says it "is not part of a mountain range".
- **Tatoosh Range** (high point Unicorn Peak): https://en.wikipedia.org/wiki/Tatoosh_Range + https://en.wikipedia.org/wiki/Unicorn_Peak
  - elevation 6,971 ft (Unicorn Peak, peakbagger 2327; NPS park map) ft→m 2124.8. The WA list gives 6,975.
  - prominence 2,091 ft (Unicorn Peak) ft→m 637.3.
  - type "a mountain range".
- **The Brothers**: https://en.wikipedia.org/wiki/The_Brothers_(Olympic_Mountains)
  - elevation 6,842 ft NGVD29 (south peak) and prominence 2,682 ft (peakbagger 1036) ft→m 2085.4 / 817.5.
  - classic: MP South Couloir, 3rd class, Easy Snow (https://www.mountainproject.com/route/106150761/south-couloir).
- **Three Fingered Jack**: https://en.wikipedia.org/wiki/Three_Fingered_Jack
  - elevation 7,844 ft (NGS QD1735, a map-scaled height) ft→m 2390.9. No prominence source.
  - type: "summit of a shield volcano … highly eroded".
  - first_ascent Sep 3, 1923, Ervin McNeal, Phil Philbrook, Armin Furrer, Wilbur Watkins, Leo Harryman, Ronald Sellars (Wikipedia, Sellars 1923).
  - classic: MP South Ridge Route, 5.2, 2 pitches (https://www.mountainproject.com/route/106266547/south-ridge-route).
- **Three Sisters** (pin is near Middle Sister; high point South Sister): https://en.wikipedia.org/wiki/Three_Sisters_(Oregon) + USGS three-sisters
  - elevation from NGS QD1872 "South Sister": NAVD88 3158.5 m (10,363 ft), natively metric. USGS quick facts give 3,157 m / 10,358 ft (NGVD29).
  - prominence 5,588 ft (South Sister, Andy Martin's Oregon P2000 list via infobox) ft→m 1703.2. The Oregon list gives 5,593.
  - type: USGS "Complex volcano".
  - last_eruption: USGS "The most recent eruptions were of rhyolite near South Sister, about 2,000 years ago".
- **Vesper Peak**: https://en.wikipedia.org/wiki/Vesper_Peak
  - elevation from NGS TQ0518: NAVD88 1896.1 m (6,221 ft), natively metric.
  - prominence 1,574 ft (peakbagger 1805) ft→m 479.8.
  - classic: MP Ragged Edge, 5.7, Grade II, 6 pitches (https://www.mountainproject.com/route/111130499/ragged-edge).
  - No first_ascent: the 1918 Mountaineers ascent was "likely preceded by prospectors and a geological survey party".
