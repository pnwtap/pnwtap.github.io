# Events batch 1 (+ Bill Gates's house, Valve HQ) — sources (added 2026-09-29)

Each row written and then independently fact-checked. Events use the new optional "prompt" column: the round asks with
the prompt, and the name appears on the reveal. The women's-sports rows researched alongside them were not used: the event
almost always names its place, so it can't be guessed from the description.

## Fact-check changes (events-a)

- D.B. Cooper: the prompt now asks 'Where did the FBI think he landed' instead of 'Where did he jump', since the member is a landing-zone estimate. It is 216 characters. The blurb is reworded and shortened (161 characters) with the same verified facts: $5,800, a boy of eight, Tena Bar, Lake Merwin/Ariel.
- Boeing's first flight: the blurb was rewritten because it closely followed HistoryLink. It now gives the B&W initials (Boeing + Navy Lt. Conrad Westervelt) and the Roanoke Street boathouse hangar on Lake Union. The Lake Union ring was independently re-checked against OSM (Hausdorff 0.089 km, 2.340 vs 2.333 km²).
- First gravitational waves: no text change. The OSM source now points at the 'LIGO's Detection Arms' board node instead of the Exploration Center way.
- End of the Oregon Trail: 'many' was added to the prompt ('many Oregon Trail emigrants made their final camp'), because pre-1846 arrivals came by raft and not everyone ended there. The blurb was tightened to 161 characters and says 'Many emigrants wintered...' and 'from 1846 the Barlow Road ended there'. The unused NPS source was dropped.
- Fay Fuller: a factual error in the blurb was corrected. Van Trump invited her but was not in the summit party, which was a Seattle party led by Rev. Ernest C. Smith (with Longmire, Amsden and Parrish). The blurb now also places Fay Peak near Mowich Lake.
- Phyllis Munday: the blurb's 'unmapped peak' became the 'Mystery Mountain' now called Mount Waddington. The 1924 Canadian Alpine Journal was added as a primary source: Kain guided her, she was first on top, and Annette Buck followed on the second rope.
- Henrietta Tuzo: the date changed from 'September 15, 1906' to '1906', because the day is disputed (15 September vs 21 July 1906). The blurb now gives her son J. Tuzo Wilson instead of the charter-member line. Bivouac, the 1907 CAJ, the Christian Kaufmann article and Linda Hall were added as sources.
- Maëlle Ricker: the blurb now says a run 'carries her name' (the exact signed name is uncertain) and adds that the venue was minutes from where she grew up.
- Lindsey Vonn: the blurb was replaced because the 'Dave Murray Downhill grandstand' finish claim couldn't be confirmed. The new one gives the 770 m drop from Wild Card to Lower Franz's Run and Mancuso's silver.
- Alissa St Laurent: the prompt's 'about 90 minutes ahead of every man' became 'nearly 90 minutes ahead of the fastest man'. The blurb time became '13 h 53 min' because sources differ by a second, and it now says the Sinister 7 win came under three weeks earlier. The ITRA source was replaced by Global News ('Saturday') and Running Magazine ('first weekend of August').
- Rainier Infinity Loop: the geometry changed from the Columbia Crest point to a 53-point Wonderland Trail ring built from OSM relation 4111743 (kind 'area'; all vertices pass in_region). The blurb was rewritten to drop the inaccurate 'repeats in mirror image'.
- Every final row was re-validated with the project's parse_locations (categories, region mask, facts registry): Cooper parses as 'any' with 2 point members, Boeing and Infinity Loop as 'area', and the rest as 'point'. All prompts are 220 characters or fewer, all blurbs 165 or fewer, and all fact values 40 or fewer.

### D.B. Cooper

Geometry: An 'any of' row with two point members (unchanged). Tena Bar is the Citizen Sleuths reconstruction rounded to 4 dp. The FBI's first estimate has no published coordinate, only 'a few miles southeast of Ariel, near Lake Merwin', so the point sits about 4.3 km SE of Ariel, south of the lake's west end. Re-checked: both members pass in_region, and the project parser reads the row as kind 'any' with two point members.

Notes: The money find is $5,800 (HistoryLink, Citizen Sleuths, KIRO: 290 twenty-dollar bills). Wikipedia's '$6,000' is a round figure. Citizen Sleuths calls the boy nine, but HistoryLink and Wikipedia say eight, so the row keeps eight. The 'rainy night' rests on the FBI agent's quote in Wikipedia; fbi.gov refuses automated fetches (403). I changed the prompt's question from 'Where did he jump' to 'Where did the FBI think he landed', because the member is a landing-zone estimate, not a known jump point. It is 216 characters.

- Flight 305 hijacked November 24, 1971 (the night before Thanksgiving); ticket in the name 'Dan Cooper'; $200,000 ransom; he opened the aft door, lowered the airstair and parachuted; initial extrapolations put the landing zone 'a few miles southeast of Ariel, Washington, near Lake Merwin'; FBI agent Larry Carr is quoted that he jumped 'in the pitch-black night, in the rain'; Tena Bar is about 9 mi downstream of Vancouver; Brian Ingram was eight; later recalculations favoured the Washougal River watershed — https://en.wikipedia.org/wiki/D._B._Cooper
- $5,800 found February 10, 1980 by 8-year-old Brian Ingram on Tena Bar, on the Washington side of the Columbia in Clark County; an early FBI theory centred on Lake Merwin / the reservoir behind the Ariel dam — https://www.historylink.org/file/23059
- Money-find site reconstructed from FBI photographs as lat 45.717888, long -122.759500; $5,800 in $20 bills — https://www.citizensleuths.com/tena-bar-money-find/
- Ariel, WA coordinates 45°57'24"N 122°34'15"W, used to place the drop-zone point a few miles to the SE — https://en.wikipedia.org/wiki/Ariel,_Washington

### Boeing's first flight

Geometry: Unchanged. Independently re-checked against OSM relation 2793813 (fetched from the OSM API and its outer ways polygonized). The row's 23-point ring is valid and closed, with area 2.340 km² against OSM's 2.333 km². Hausdorff deviation is 0.089 km. Every vertex passes in_region, and it parses as kind 'area'.

Notes: The facts, the Roanoke Street location and the date all check out against HistoryLink. I rewrote the blurb because the old one closely followed HistoryLink's sentence. The new one adds the B&W initials fact (Boeing + Westervelt).

- June 15, 1916: William E. Boeing pilots the B&W Bluebill, 'the first plane he helped to build', into the air above Lake Union; built in the Pacific Aero Club's hangar-boathouse at the foot of Roanoke Street; B&W reflected the initials of Boeing and his partner, Navy Lieutenant Conrad Westervelt; Pacific Aero-Products Co. incorporated July 15, 1916, later renamed Boeing Airplane Co. — https://www.historylink.org/file/369
- B & W (Model 1) first flew June 15, 1916; first Boeing product; built at Boeing's boathouse hangar on Lake Union — https://en.wikipedia.org/wiki/Boeing_Model_1
- Lake Union outline: OSM relation 2793813 (natural=water, water=lake), outer area 2.333 km² — https://www.openstreetmap.org/relation/2793813

### First gravitational waves

Geometry: The published corner-station (vertex) coordinate 46°27'18.52"N 119°24'27.56"W = 46.45514,-119.40766, rounded to 4 dp. OSM shows it inside the corner-station building cluster, about 0.4 km from the NSF LIGO Exploration Center (way 1149306547). It passes in_region.

Notes: No changes to the text. The original OSM source link pointed at way 1149306547, which is the Exploration Center, not the info board. It now points at the board node. 'Over a billion light-years' covers both the 1.3 and the 1.4 billion ly figures.

- GW150914 detected 14 September 2015 at 09:50:45 UTC by LIGO Livingston and LIGO Hanford; the chirp lasted over 0.2 s; two black holes of about 36 and 29 solar masses; about 1.4 ± 0.6 billion light-years; LIGO Hanford is on the DOE Hanford Site near Richland; 2017 Nobel Prize in Physics to Rainer Weiss, Barry Barish and Kip Thorne — https://en.wikipedia.org/wiki/First_observation_of_gravitational_waves
- 4 km interferometer arms; the two US observatories are at Hanford, WA and Livingston, LA; LIGO Hanford corner-station coordinates 46°27'18.52"N 119°24'27.56"W — https://en.wikipedia.org/wiki/LIGO
- OSM cross-check: 'LIGO's Detection Arms' information board at 46.4561,-119.4087 and the 'Beam Tubes' board and IEEE commemoration plaque at about 46.4548-46.4550,-119.4068, all among the corner-station buildings — https://www.openstreetmap.org/node/10692135455

### End of the Oregon Trail

Geometry: The Abernethy Green marker (N 45°21.880 W 122°35.657 = 45.36467,-122.59428), rounded to 4 dp. Re-checked with the OSM API: it lies inside the park polygon, about 36 m from its centroid. It passes in_region.

Notes: I added 'many' to the prompt and the blurb. Emigrants before 1846 reached Oregon City by raft from Fort Vancouver, and not every emigrant ended there, so 'emigrants made their last camp here' was an overgeneralization. I cut the blurb's 'near Willamette Falls' to bring it down to the sheet's usual length. The Oregon Encyclopedia and hmdb refuse automated fetches (403).

- Abernethy Green marker: emigrants began arriving on rafts from Fort Vancouver in 1843; arriving in late fall or early winter, most wintered in encampments at Abernethy Green; from 1846 two-thirds of emigrants took Barlow's Mount Hood Toll Road, which ended at Abernethy Green; marker at N 45°21.880 W 122°35.657 — https://www.waymarking.com/waymarks/wm655T_Abernethy_Green_Oregon_City_Oregon
- The wagon trains camped a final time on the broad creekside meadow near the Willamette River; Oregon City's Abernethy Green marked the traditional End of the Oregon Trail — https://oregon.com/attractions/end-oregon-trail
- Oregon City was capital of the Oregon Territory from its establishment in 1848 until 1851; in the 1840s and 1850s it was the last stop on the Oregon Trail; End of the Oregon Trail Interpretive Center reopened in 2013 — https://en.wikipedia.org/wiki/Oregon_City,_Oregon
- The Oregon Trail ran about 2,170 miles; traffic was heaviest from 1846 to 1869 — https://en.wikipedia.org/wiki/Oregon_Trail
- OSM park 'End of the Oregon Trail Interpretive Center' (Oregon City Parks & Recreation), centroid 45.3646,-122.5947 — https://www.openstreetmap.org/way/131816577

### Fay Fuller

Geometry: Rainier's summit, Columbia Crest (46.8529,-121.7604, 4 dp), about 130 m from the existing 'Mt Rainier' peak row point. It passes in_region.

Notes: I corrected the blurb. P. B. Van Trump invited Fuller, but he did not lead or join the summit party. HistoryLink says a Seattle party headed by Rev. Ernest C. Smith, with Longmire, Amsden and Parrish. The prompt is accurate as written.

- August 10, 1890: journalist, schoolteacher and Yelm resident Fay Fuller, two months before her 21st birthday, becomes the first woman known to reach Rainier's summit (after 4 p.m.); she wore a thick blue flannel bloomer suit, which was thought 'quite immodest'; the party spent the night in an ice cave created by steam vents; Van Trump invited her and gave permission for her to join a Seattle party headed by Rev. Ernest C. Smith; the summit party was Fuller, Smith, Len Longmire, W. O. Amsden and R. R. Parrish; Fay Peak (6,492 ft), near Mowich Lake, is named for her — https://www.historylink.org/File/7786
- On the afternoon of August 10, 1890, she and four teammates reached Columbia Crest, the first woman to climb the mountain; Fay Peak in Mount Rainier NP is named after her — https://en.wikipedia.org/wiki/Fay_Fuller

### Phyllis Munday

Geometry: Mount Robson's summit from CGNDB via Wikipedia (53°06'38"N 119°09'23"W = 53.1106,-119.1564), the same as the existing 'Mt Robson' peak row. It passes in_region.

Notes: The 1924 Canadian Alpine Journal (primary source) confirms Kain guided her and that she was first on top. The American Annette Buck, on the second rope, summited just after, so 'first woman' is correct. I rewrote the blurb: 'unmapped peak' became the 'Mystery Mountain', which is what the Mundays called it. No day is published. The climb fell during the camp (July 22–August 4, 1924), so the date stays '1924'.

- Munday's own account, 'First Ascent of Mt. Robson by Lady Members': guided by Conrad Kain; the second rope waited below the summit cornice; on top Kain told her she was the first woman on the summit. The 1924 camp report says Mrs. W. A. D. Munday and Miss A. E. Buck were the first ladies on the summit, and the ACC camp ran from July 22 to August 4, 1924 — https://alpineclubofcanada.ca/wp-content/uploads/2024/05/1924.pdf
- First woman to reach the summit of Mount Robson (with Annette Buck) in 1924; in 1925, from Mount Arrowsmith, she and Don spotted a peak they believed taller than Robson, which led to Mount Waddington ('The Mystery Mountain') — https://en.wikipedia.org/wiki/Phyllis_Munday
- In 1924 Conrad Kain led a group with two women in it to the summit of Mt. Robson; Kain told Munday she was the first woman on the peak — http://historynstuff.blogspot.com/2014/09/phyllis-munday-first-woman-to-summit.html
- First ascent July 31, 1913, led by Conrad Kain; summit 53°06'38"N 119°09'23"W; highest point of the Canadian Rockies — https://en.wikipedia.org/wiki/Mount_Robson
- First woman to summit Robson in 1924; she and Don spotted Waddington from Mount Arrowsmith in 1925 — https://www.thecanadianencyclopedia.ca/en/article/phyllis-munday

### Henrietta Tuzo

Geometry: CGNDB summit coordinate via Wikipedia (51.3016666,-116.2283333), rounded to 4 dp. It is about 40 m from bivouac's summit coordinate and about 3.8 km SW of Moraine Lake. It passes in_region.

Notes: I changed the date from 'September 15, 1906' to '1906'. The day is disputed: the Mount Tuzo infobox says 15 September 1906 without its own citation, while the Christian Kaufmann article says 21 July 1906, citing a 2003 book and a 1929 newspaper. The September date looks like a mix-up with Tuzo's 15 September 1904 Mt. Victoria climb with Kaufmann. Bivouac and the 1907 CAJ give only the year. I swapped the blurb's ACC charter-member line for the J. Tuzo Wilson connection, which is more intriguing and well sourced. 'Turquoise lake' describes Moraine Lake and is not a sourced claim.

- Named in 1907 after its first ascensionist Henrietta L. Tuzo; seventh of the Ten Peaks (Allen's 'Sagowa'); 3,246 m; on the Continental Divide (AB/BC), in the Valley of the Ten Peaks, on the Banff/Kootenay boundary; CGNDB 51.3016666,-116.2283333; Tuzo, a charter member of the ACC, became the mother of geologist John Tuzo Wilson; infobox gives the first ascent as 15 September 1906 — https://en.wikipedia.org/wiki/Mount_Tuzo
- First ascent 1906 by H. Tuzo and C. Kaufmann; summit 51.30136,-116.22836; route up the 3-4 couloir and across the Fay Glacier — https://www.bivouac.com/MtnPg.asp?MtnId=1576
- Kaufmann and Tuzo climbed Mt. Collie on 12 July 1906 and, on 21 July [1906], were first on the summit of Peak Seven above Moraine Lake; separately, Tuzo climbed Mt. Victoria with Kaufmann on 15 September 1904 — https://en.wikipedia.org/wiki/Christian_Kaufmann_(alpine_guide)
- ACC membership list: Miss H. L. Tuzo, ascents including 'Mt. Tuzo (Peak seven of the Ten Peaks, first ascent)'; Chief Mountaineer's report: on July 12 [1906] she climbed Mt. Collie under the care of the Swiss guide Christian Kaufmann — https://alpineclubofcanada.ca/wp-content/uploads/2024/05/1907.pdf
- J. Tuzo Wilson's mother Henrietta was the first to climb the 7th peak in the Valley of the Ten Peaks, later named for her — https://www.lindahall.org/tuzo-wilson/

### Maëlle Ricker

Geometry: A point on the OSM piste 'Maelle Ricker's' (way 40040601, re-fetched from the OSM API), about 60 m from the line's mean point. It is within about 1 km of the 2010 freestyle/snowboard venue, and the run named for her stands in for the unmapped SBX course. It passes in_region.

Notes: The prompt checks out. I changed the blurb from 'is now called Maelle Ricker's' to 'now carries her name', because the run's exact signed name is uncertain: OSM has "Maelle Ricker's" with alt name 'Fork', and one listing says 'Maelle Ricker's Gold'. I added the 'minutes from home' detail from Wikipedia.

- Women's snowboard cross, 2010 Winter Olympics, at Cypress Mountain on February 16, 2010; gold to Maëlle Ricker (CAN) — https://en.wikipedia.org/wiki/Snowboarding_at_the_2010_Winter_Olympics_%E2%80%93_Women%27s_snowboard_cross
- Born in North Vancouver; first Canadian woman to win an Olympic gold medal on home soil, 'just minutes from her childhood home in North Vancouver' — https://en.wikipedia.org/wiki/Ma%C3%ABlle_Ricker
- Cypress Mountain hosted the freestyle skiing and snowboarding events of the 2010 Games — https://en.wikipedia.org/wiki/Cypress_Mountain_Ski_Area
- OSM downhill piste name="Maelle Ricker's" (alt_name 'Fork'), intermediate, Black Mountain side; centre about 49.3948,-123.2110 — https://www.openstreetmap.org/way/40040601

### Lindsey Vonn

Geometry: The end node of the OSM 'Franz's' piste at the Creekside base (re-fetched from the OSM API; the row point is 3 m from it). The Dave Murray Downhill finish is 29 m away. It passes in_region.

Notes: The prompt checks out. I replaced the blurb, since its claim of a shared 'Dave Murray Downhill grandstand' finish could not be confirmed. The new blurb uses the Wikipedia course description (770 m drop, Wild Card to Lower Franz's) and the US one-two finish.

- Women's downhill, February 17, 2010, Whistler Creekside; course runs on the top part of Wildcard, the bottom of Jimmy's Joker, then finishes on Lower Franz's Run; 770 m vertical; Vonn gold in 1:44.19, the first US gold in the Olympic women's downhill; Mancuso (USA) silver, Görgl bronze; Pärson and Gisin fell on the last jump — https://en.wikipedia.org/wiki/Alpine_skiing_at_the_2010_Winter_Olympics_%E2%80%93_Women%27s_downhill
- OSM piste 'Franz's' (way 47941294) ends at 50.0937,-122.9880, beside the end of 'Dave Murray Downhill - Lower' (way 48083138) at the Creekside base — https://www.openstreetmap.org/way/47941294

### Alissa St Laurent

Geometry: The centre of OSM 'Central Park', Grande Cache (way 1528687735, re-fetched from the OSM API; the row point is 9 m from its centroid), the start named on the organiser's course page. It passes in_region.

Notes: The prompt said 'about 90 minutes ahead of every man'. Sources say 'nearly 90 minutes ahead of the top male finisher', so it now reads 'nearly 90 minutes ahead of the fastest man'. The blurb gives the time as '13 h 53 min' because sources differ by a second (13:53:34 or 13:53:35). The date is now supported without ITRA: Global News says the race was on Saturday, and Running Magazine says the first weekend of August 2015. Both mean Saturday August 1, 2015. Today's course is 118 km, but every 2015 source says 125 km.

- First female in the race's 15-year history to win the Canadian Death Race outright (2015), in 13:53:34, less than three weeks after winning the 100-mile Sinister 7 in a female course record of 18:37:19 — https://en.wikipedia.org/wiki/Alissa_St_Laurent
- Edmonton runner; 125 km; 13 h 53 min; three mountain summits and over 17,000 ft of elevation change; Grande Cache; race on Saturday; nearly 90 minutes ahead of the top male finisher, Graham Glennie; course record at the Sinister 7 earlier that summer — https://globalnews.ca/news/2147256/edmonton-woman-becomes-first-female-to-win-canadian-death-race/
- 13:53:35; first woman to win in the race's 15-year history; nearly an hour and a half ahead of the second-place finisher overall; race on the first weekend of August 2015 — https://runningmagazine.ca/trail-running/edmonton-runner-is-first-woman-to-win-canadian-death-race/
- Race held annually on the August long weekend in Grande Cache — https://en.wikipedia.org/wiki/Canadian_Death_Race
- Course starts in downtown Grande Cache at Central Park; summits Flood Mountain, Grande Mountain and Mount Hamell — https://www.sinistersports.ca/deathrace/course

### Rainier Infinity Loop

Geometry: NEW. This is the Wonderland Trail ring, replacing the summit point. OSM relation 4111743 was fetched from the OSM API (relation/full, not Overpass). Its 82 member ways were polygonized in a local km projection into one closed ring: 138.3 km perimeter, 337.9 km². It was simplified with shapely's topology-preserving Douglas-Peucker at 0.5 km (Hausdorff 0.48 km), giving 53 points. They were rounded to 4 dp and closed (first == last). Every vertex passes in_region, and the project parser reads the row as kind 'area'. So any tap inside the loop, including the summit the route crosses twice, scores as a hit. The ring runs 6.6–14.5 km from the summit.

Notes: The blurb's 'repeats in mirror image' was not accurate for this pair: per the Spokesman-Review they went up the DC route and down the Emmons both times, and only the Wonderland legs went opposite ways. The new blurb says the loop crosses the summit twice and its Wonderland legs add up to one full lap, which holds whatever the direction. If the owner prefers a point, the old value 46.8529,-121.7604 (Columbia Crest) still works. It scores almost the same, since the whole loop sits inside the flat 25 km zone.

- Borsuk (Portland) and Gerbin (Issaquah) started Thursday July 25, 2019 and finished early Tuesday, in 4 days 4 hours; 135 miles, 47,000+ ft; up the Disappointment Cleaver, down the Emmons-Winthrop to White River, 30 miles of Wonderland Trail back to Paradise, a second climb, then the remaining 63 miles of the 93-mile Wonderland; first all-women team after four earlier finishing teams (including Nate Smith & Sarah Morris, 2017); conceived by Chad Kellogg, who died in Patagonia in 2014 — https://www.spokesman.com/stories/2019/aug/09/women-complete-mount-rainier-infinity-loop-a-jaw-d/
- Route about 143.7 mi, 44,000+ ft, conceived by Chad Kellogg; Gerbin & Borsuk 4d 4h 20m, dated 2019-07-30, the first all-women's team; Sarah Morris & Nate Smith, a mixed team, 2017-07-16 — https://fastestknowntime.com/route/rainier-infinity-loop-wa
- Borsuk and Gerbin were the first all-female team to complete the Mount Rainier Infinity Loop — https://www.king5.com/article/entertainment/television/programs/evening/alex-borsuk-kaytlyn-gerbin-rainier-infinity-loop/281-1117ef42-ec3c-466a-a2fa-de1d80460fb4
- Wonderland Trail route relation (route=hiking, operator Mount Rainier National Park), OSM data 2026-09-29 — https://www.openstreetmap.org/relation/4111743

## Fact-check changes (events-b)

- Lituya Bay: moved the point from 58.6700,-137.5275 to 58.6690,-137.5275 (about 110 m). Miller's 1960 USGS report puts the 1,720 ft maximum on the crest of the spur, where the water spilled over the ridge. A fine SRTM grid, cross-checked with Mapzen and ASTER, puts the crest's about-524 m point there. The old point was on the slope facing the inlet.
- Lituya Bay: the blurb now says the water poured over the crest of the spur opposite (Miller 1960). The rest is unchanged and verified: three boats, and the Sunmore was lost with the Wagners.
- Lituya Bay: checked 'highest tsunami run-up ever recorded' against the Aug 2025 Tracy Arm megatsunami (about 481 m, second highest). The claim still holds. Added Miller 1960, Tracy Arm and Megatsunami sources.
- Oso: took 'covering about a square mile' out of the prompt. Wikipedia gives that figure with no citation, and the peer-reviewed accounts (Iverson et al. 2015; GSA Bulletin) describe the slide crossing a valley about 1 km wide and spreading about as far sideways, roughly 0.4 sq mi. The prompt now reads 'flowed across a river valley more than half a mile wide, burying a rural neighborhood and a state highway'.
- Oso: confirmed the memorial opened March 22, 2024 and the 10:37 a.m. time with the Everett Herald, and added that source and the two scientific sources. Geometry re-checked on imagery and unchanged.
- Rajneeshpuram: 'spiked salad bars at ten restaurants in The Dalles' became 'spiked restaurant salad bars in the county seat'. Naming The Dalles, about 100 km from the answer, was a strong location hint, and the CDC/JAMA study found only 8 of the 10 restaurants had salad bars. 'Sway a county election' became 'sway the county election'.
- Rajneeshpuram: rewrote the blurb to name The Dalles (about 60 mi southeast of it) so the reveal explains the gap. Corrected the Young Life wording: the camp opened in 1999 as WildHorse Canyon Camp and is now Washington Family Ranch. Added JAMA and The Dalles county-seat sources. Geometry re-checked and unchanged.
- All three points re-checked with in_region: True. Prompts are 216, 200 and 204 characters.

### Lituya Bay megatsunami

Geometry: Miller (1960, USGS PP 354-C) puts the highest point of the trimline (1,720 ft) on the crest of the spur SW of Gilbert Inlet, where the water spilled over the ridge. I sampled a 0.001 degree SRTM 30 m grid over the spur through OpenTopoData. The crest runs NW to SE, about 620 m at 58.670,-137.533 dropping to about 490 m at 58.668,-137.528. It crosses about 524-540 m (canopy-top DEM, so the ground is a little lower) at about 58.6690,-137.5275. The Mapzen and ASTER DEMs agree to within about 20 m. The earlier point (58.6700,-137.5275) was about 110 m north of this, on the inlet-facing slope. Checked in_region: True.

Notes: Gilbert Inlet is now mostly glacial outwash, so modern imagery shows gravel flats where the water was in 1958. The point is on the forested spur just SW of them. DEM error could move the true spot by 100-200 m, which is negligible at game scale. The prompt names only the state ('Alaskan fjord'). The rockslide mass differs by source (about 40 to 90 million tons), so the prompt uses Miller's volume, 40 million cubic yards (about 30 million m3). 'Highest tsunami run-up ever recorded' still holds after the 2025 Tracy Arm event (about 481 m, second highest).

- About 40 million cubic yards (about 30.6 million m3) of rock fell from the northeast wall into Gilbert Inlet. The trimline reached 1,720 ft on the spur SW of Gilbert Inlet, and at that point on the crest of the spur the water flowed across the ridge and down the far side. The quake began about 10:16 p.m. on July 9, 1958 (Miller 1960, USGS Professional Paper 354-C) — https://pubs.usgs.gov/pp/0354c/report.pdf
- Date; rockslide of 30 million m3 into Gilbert Inlet; trees cleared to 524 m (1,719 ft) at the entrance of Gilbert Inlet; two people on a fishing boat in the bay died — https://en.wikipedia.org/wiki/1958_Lituya_Bay_earthquake_and_megatsunami
- Highest trimline on the spur at the corner between Gilbert Inlet and the main bay, opposite the NE-wall slide scar. Three boats were in the bay; the Sunmore vanished and the Wagners were never found; the Badger's and Edrie's crews survived — https://earthquake.alaska.edu/60-years-ago-1958-earthquake-and-lituya-bay-megatsunami
- Lituya 1958 is still the highest run-up recorded; the Aug 10, 2025 Tracy Arm megatsunami (about 481 m) is second — https://en.wikipedia.org/wiki/Tracy_Arm
- Tallest megatsunami ever recorded (520 m run-up); Tracy Arm 2025 run-up 470-500 m — https://en.wikipedia.org/wiki/Megatsunami
- Max run-up 524 m on the spur ridge opposite the rockslide (Fritz et al.) — https://www.researchgate.net/publication/251230405_Lituya_Bay_case_Rockslide_impact_and_wave_run-up
- Lituya Bay is part of Glacier Bay National Park and Preserve — https://en.wikipedia.org/wiki/Lituya_Bay
- Gilbert Inlet position (OSM node, GNIS 1422142) — https://www.openstreetmap.org/node/369146624
- SRTM 30 m (cross-checked with Mapzen and ASTER) elevations used to find where the spur crest reaches about 524 m — https://www.opentopodata.org/datasets/srtm/

### Oso landslide

Geometry: Re-plotted the point, the OSM memorial, the OSM headscarp and the Wikipedia coordinate on current Esri World Imagery (z16). The point is on the hummocky slide deposit south of the present river channel and north of SR 530, over the former Steelhead Haven neighborhood, about 300 m NW of the memorial. The deposit spans roughly 1 km, so the point sits near its middle. Checked in_region: True.

Notes: Kept sober: date, time, what happened and the 43 deaths, with nothing graphic and no superlative. 'Deadliest US landslide' holds only with exclusions, so it was left out. The prompt avoids 'Oso', 'Stillaguamish' and 'SR 530'. The blurb names them.

- March 22, 2014 at 10:37 a.m.; mud and debris went south across the North Fork Stillaguamish River, engulfing the Steelhead Haven neighborhood; 43 killed; up to 200% of normal rain in the preceding 45 days — https://en.wikipedia.org/wiki/2014_Oso_landslide
- The landslide (about 8 million m3), after a long spell of abnormally wet weather, 'traveled across the entire ~1 km breadth of the adjacent floodplain' (Iverson et al. 2015, EPSL) — https://doi.org/10.1016/j.epsl.2014.12.020
- The landslide travelled 'across a 1-km+-wide river valley', killed 43 people and closed a well-traveled highway (GSA Bulletin, SR 530 landslide) — https://doi.org/10.1130/B35146.1
- Memorial opened Friday, March 22, 2024 (10th anniversary) along Highway 530; honors 43; slide at 10:37 a.m.; Steelhead neighborhood (Everett Herald) — https://www.heraldnet.com/news/flood-of-emotions-as-oso-landslide-memorial-opens-on-10th-anniversary/
- Oso Landslide Memorial along SR 530 east of Oso, opened March 22, 2024 — https://en.wikipedia.org/wiki/Oso_Landslide_Memorial
- Memorial location beside SR 530 (OSM 'Oso Slide Memorial'), about 48.2775,-121.8415 — https://www.openstreetmap.org/way/1194069688
- Headscarp area (OSM 'Oso Mudslide' cliff way), about 48.2836,-121.8481 — https://www.openstreetmap.org/way/1193699456

### Rajneeshpuram

Geometry: Re-plotted the point, the OSM Rajneeshpuram locality, the Washington Family Ranch node, the Big Muddy Ranch airport and the Wikipedia coordinate (44.842,-120.482) on Esri World Imagery (z15), and checked OSM named features (Muddy Reservoir, the old hotels and dining hall now used by the camp). The point is in the built-up core of the former city beside Muddy Reservoir, within about 50 m of the OSM ranch node. The Wikipedia coordinate is up a side draw and less representative. The Dalles is about 100 km (62 mi) NNW (straight line). Checked in_region: True.

Notes: Based on the owner's example prompt: 'Over 700' became the CDC figure 751. The researcher's 'at ten restaurants in The Dalles' became 'restaurant salad bars in the county seat': naming a town about 100 km from the answer was a strong location hint, and the CDC found only 8 of the 10 restaurants had salad bars. The owner's wording 'the Rajneeshpuram commune based here' is kept even though it names the commune (see open questions). The blurb now names The Dalles, so the reveal explains the distance. 'Since 1999 the ranch has been Young Life's Washington Family Ranch camp' was corrected, because the camp opened as WildHorse Canyon Camp.

- 751 people suffered food poisoning in The Dalles after deliberate Salmonella contamination of salad bars at ten local restaurants (and salad dressing). Followers led by Ma Anand Sheela hoped to incapacitate voters so their candidates would win the November 1984 Wasco County elections — https://en.wikipedia.org/wiki/1984_Rajneeshee_bioterror_attack
- CDC investigation: 751 cases, outbreak September 9 to October 10, 1984; most cases linked to 10 restaurants in The Dalles, 8 of which had salad bars; members of a religious commune deliberately contaminated the salad bars (Torok et al., JAMA 1997) — https://pubmed.ncbi.nlm.nih.gov/9244330/
- The Dalles is the county seat and largest city of Wasco County — https://en.wikipedia.org/wiki/The_Dalles,_Oregon
- Rajneeshpuram, in Wasco County, stood on the 64,281-acre Big Muddy Ranch near Antelope. Donated to Young Life in 1996; a camp has run there since 1999, first as WildHorse Canyon Camp and later as Washington Family Ranch — https://en.wikipedia.org/wiki/Rajneeshpuram
- OSM locality 'Big Muddy Ranch' (old_name 'Rajneeshpuram'), 44.8320,-120.4833 — https://www.openstreetmap.org/node/9689030836
- OSM 'Washington Family Ranch' in the former city core, 44.8352,-120.4802 — https://www.openstreetmap.org/node/905117379

## Fact-check changes (places)

- Bill Gates's house: replaced the King County Assessor parcel-record source with Guinness World Records ('Largest underground house'). Guinness independently confirms 66,000 sq ft, the earth-sheltered design and the Lake Washington setting. The tax-record page supported no fact shown in the game (its only use was a 1994 'year built' that the row does not use), so a personal property-tax record is no longer needed in the sources.
- Bill Gates's house: reworded the Spokesman-Review and Virginian-Pilot source notes to say exactly what each article says: construction began 1990, move-in Sept 1997, and pavilions terraced into the hillside, which backs the blurb's 'dug into a Medina hillside'. No change to the blurb, facts or geometry, which all checked out.
- Valve headquarters: blurb changed from 'fills nine floors of this 31-story Lincoln Square tower' to 'moved into nine floors of this 31-story Lincoln Square tower in downtown Bellevue in 2017'. The nine-floor figure is confirmed only up to about 2019, while the 2026 Steam agreement confirms only the building address.
- Valve headquarters: added ArchDaily as a second source for '9 contiguous floors' and '31-story'. Pulled the text out of the leasing-brochure PDF to confirm 'Stories: 31'. Swapped the downtownbellevue.com source for the Bellevue Reporter (Aug 16, 2016), which I could fetch and which confirms floors 11–19 and a spring 2017 move.
- Both rows: re-checked the geometry against fresh Overpass data with a point-in-polygon test (each point is inside its intended footprint and in no neighbouring building) and re-ran in_region (True for both).

### Bill Gates's house

Geometry: Point inside the OpenStreetMap footprint of way 914623154, which is tagged as the Gates house (alt_name Xanadu 2.0, wikidata Q371973). The polygon centroid rounds to a spot just outside that narrow footprint, so 47.6278,-122.2419 was used instead. It is about 6 m from Wikipedia's coordinate (47.62774,-122.24194). Fact-check: I re-fetched the way from Overpass and ran a point-in-polygon test. Both the row point and Wikipedia's coordinate fall inside way 914623154 (bbox 47.62761–47.62802, -122.24219 to -122.24181) and inside none of the neighbouring buildings. in_region = True.

Notes: Verified from other sources. The 66,000 sq ft figure appears on both Wikipedia and Guinness. The house is built into the hillside: 1997 press describes pavilions terraced down the slope, much of the house underground, and a garage tunnelled into the hill. The Xanadu 2.0 nickname comes from U.S. News (1997), and Wikipedia says 'some news articles' use it. Sources disagree on when the house was finished: the county assessor records 1994, Guinness says 1995, and 1997 press says construction began in 1990 and the family moved in in Sept 1997. I kept 1990–97 (construction start to move-in) because two independent contemporary articles support it. The blurb is original wording and accurate. The prompt is empty, as usual for a poi. Clue facts do not give the location away. Medium difficulty is reasonable.

- Wikipedia article 'Bill Gates's house': coordinates 47.62774,-122.24194 in Medina, WA; a 66,000 sq ft earth-sheltered mansion in Pacific lodge style on Lake Washington; some news articles call it Xanadu 2.0 — https://en.wikipedia.org/wiki/Bill_Gates's_house
- Guinness World Records 'Largest underground house': Bill Gates's earth-sheltered mansion in Medina, WA, overlooking Lake Washington, 6,100 m2 (66,000 sq ft); lists completion as 1995 — https://www.guinnessworldrecords.com/world-records/69303-largest-underground-house
- Construction started in 1990; seven years later (Sept 1997) the family was moving in; much of the mansion is underground — https://www.spokesman.com/stories/1997/sep/12/bills-hovel-by-the-lake-7-years-later-gates-and/
- Construction began in 1990; family began moving in September 1997; pavilions terraced down the hillside, with a garage tunnelled into the hillside — https://scholar.lib.vt.edu/VA-news/VA-Pilot/issues/1997/vp970914/09130113.htm
- 'Xanadu 2.0' nickname (U.S. News, Nov 23, 1997) — https://money.usnews.com/money/business-economy/articles/1997/11/23/xanadu-20
- Geometry: OSM way 914623154 (building=house, alt_name Xanadu 2.0, wikidata Q371973) — https://www.openstreetmap.org/way/914623154

### Valve headquarters

Geometry: Point on the 31-story office tower of Lincoln Square South, OSM way 1326151866 (building:part, building:levels 31, name 'Lincoln Square South Tower'). The 42-level hotel/residential tower to the north (OSM way 604028603) was excluded. Fact-check: I re-fetched both ways and node 5270634805 from Overpass. 47.6142,-122.2008 falls inside way 1326151866 (bbox 47.61403–47.61438, -122.20130 to -122.20046) and outside way 604028603. It is about 7 m from node 5270634805 (47.61425,-122.20072). in_region = True.

Notes: Verified. Valve's own Steam Subscriber Agreement (rev. Sept 10, 2026) confirms the HQ is still at 10400 NE 4th St. That is the Lincoln Square South office tower: the leasing brochure lists 'Stories: 31', and ArchDaily also says 31 stories. The nine floors (11–19) and the May 2017 move are confirmed by the 2016 press release, the Bellevue Reporter and ArchDaily. The founding date of 1996 matches Wikipedia. I changed the blurb from the present tense 'fills nine floors' to 'moved into nine floors ... in 2017'. Nine floors is confirmed only up to about 2019, so this wording stays true even if Valve has since added or dropped floors. The prompt is empty, as usual for a poi, and the clue facts do not reveal the location.

- Current HQ address: Steam Subscriber Agreement (revised September 10, 2026) gives Valve Corporation's address as 10400 NE 4th St., Bellevue, WA 98004 — https://store.steampowered.com/subscriber_agreement/
- Press release, Aug 3, 2016: Valve leased 225,000 sq ft on floors 11–19 of the new 710,000 sq ft Lincoln Square expansion office tower, moving in May 2017 — https://www.prweb.com/releases/valve_moving_to_lincoln_square_expansion/prweb13593429.htm
- Bellevue Reporter, Aug 16, 2016: Valve to occupy floors 11 through 19 of the new Lincoln Square office tower, move in late spring 2017 — https://www.bellevuereporter.com/business/valve-looks-toward-major-bellevue-expansion/
- Leasing brochure: Lincoln Square South Tower, 10400 NE 4th Street, Bellevue; Stories: 31 — https://www.commercialmls.com/Media/PDF/photos/pdf/fl/557017_5.pdf
- ArchDaily (Clive Wilkinson / JPC interiors): Valve HQ occupies 9 contiguous floors of Lincoln Square, a 31-story mixed-use development in Bellevue — https://www.archdaily.com/924840/valve-headquarters-clive-wilkinson-architects-plus-jpc-architects
- Valve founded August 24, 1996; HQ Bellevue, WA — https://en.wikipedia.org/wiki/Valve_Corporation
- Lincoln Square expansion (two mixed-use towers) completed January 2017 — https://en.wikipedia.org/wiki/Lincoln_Square_(Bellevue)
- Geometry: OSM way 1326151866 'Lincoln Square South Tower' (31 levels) and node 5270634805 'Valve Corporation Headquarters', 10400 NE 4th St — https://www.openstreetmap.org/way/1326151866

## Update 2026-10-01: Rajneeshpuram row moved to The Dalles

Renamed "Rajneeshee salmonella attack" and pinned to The Dalles (45.6017,-121.1847, Wikipedia city coordinates), where the
poisoning happened, so the round's default "Where did it happen?" fits. The commune site is about 101 km (63 mi) southeast;
it is now in the blurb. Prompt reworded by the owner. Ten restaurants, 751 ill, led by Ma Anand Sheela:
https://en.wikipedia.org/wiki/1984_Rajneeshee_bioterror_attack ; city coordinates: https://en.wikipedia.org/wiki/The_Dalles,_Oregon
