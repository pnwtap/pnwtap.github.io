# facts_routes.csv sources

Group `routes`: 28 rows (5 routes, 10 crags/formations, 7 traverses, 6 hikes). "Brave New World" is
excluded because the owner wrote that card himself.

**Conversions.** Where the source figure is in feet or miles, the metric value comes straight from
that figure: 1 ft = 0.3048 m, rounded to 1 decimal, and 1 mi = 1.609344 km, rounded to 2 decimals.
The game can then show the familiar imperial number again. Metric sources (Parks Canada, ACC,
Wikipedia metric infoboxes) are copied as plain numbers.

**Abbreviations.** MP = Mountain Project, WP = Wikipedia, WTA = Washington Trails Association,
USFS = US Forest Service, PC = Parks Canada, ACC = Alpine Club of Canada. All pages were read on
2026-09-28. The "RT" and "one-way" notes say how each distance is normally quoted.

**`style` values** are my classification into the spec's fixed list, based on the sources cited for
each row. Grades are copied from MP as shown.

---

## Specific routes

### Infinite Bliss
- grade `5.10c R`, pitches `23`, length_m `792.5` (2,600 ft), first_ascent `2003, Leland Windham & Steve Martin`:
  MP https://www.mountainproject.com/route/108170867/infinite-bliss. The page shows "5.10c … R" and
  "Type: Trad, 2600 ft (788 m), 23 pitches, Grade IV". The FA reads "Leland Windham and Steve Martin – Aug 2003".
  theCrag also gives "5.10c R" (https://www.thecrag.com/en/climbing/united-states/central-cascade-mountains/route/563911656).
  A climbing.com article gives "23-pitch Infinite Bliss (5.10c; 2,600 feet)".
- tagline: MP says "it's quite possible it's the longest bolted climb in the USA and Canada and the
  second longest in North America". The Washington Climbers Coalition says Rock and Ice billed it as the
  "longest sport route in America" (https://washingtonclimbers.org/index.php/2004/06/30/infinite-bliss-defused/).
  The tagline is worded as "one of the longest" to match MP's hedge.
- style `sport`: **the sources disagree.** MP lists the type as *Trad* and says "This route is not a
  sport climb. It is a bolt-protected slab climb" (runouts up to 100 ft, with little or no gear to
  place). theCrag calls it "Mixed". StephAbegg.com calls it "sport", in quotes. The protection is bolts
  only, and it is widely billed as a sport route, so I used `sport`. The `R` in the grade covers the runouts.
  Switch to `trad` if you want to match MP's label.

### Flyboys
- grade `5.9`, style `sport`, pitches `18`, length_m `548.6` (1,800 ft): MP
  https://www.mountainproject.com/route/113665378/flyboys shows "Type: Sport, 1800 ft (545 m), 18 pitches, Grade IV".
  Climbing.com and StephAbegg.com both give 1,500 ft. MP is the main source, so the table uses 1,800 ft.
- first_ascent `2016–17, Bryan Burdo & Jerry Daniels`, rock `andesite`, season `Apr–Oct`: climbing.com,
  "Flyboys: Washington's 18-Pitch 5.9 Sport Route", read via the archived copy at
  http://web.archive.org/web/20230205133820/https://www.climbing.com/places/flyboys-washingtons-18-pitch-5-9-sport-route/.
  It says "Between 2016 and 2017 … Bryan Burdo and Jerry Daniels", "Goat Wall, an andesite dome", and
  gives "Season April–October". StephAbegg.com describes the wall as "andesitic breccia and tuff" and
  gives "established in 2016 and 2017" (https://stephabegg.com/trip-reports/washington/goat-wall-flyboys/).
- No tagline. The same climbing.com article calls Flyboys "possibly the longest bolted 5.9 in the
  United States". I left it out to stay within the tagline budget, but it is available as a swap.

### Coleman-Deming Route
- grade `II, moderate snow`, first_ascent `1868, Edmund Coleman and party`: MP
  https://www.mountainproject.com/route/105920598/colemandeming-glacier ("Mod. Snow", "Grade II",
  "FA: Edmund Coleman and party, 1868"). WP Mount Baker says the 17 Aug 1868 party went up "via the
  Middle Fork Nooksack River, Marmot Ridge, Coleman Glacier, and the north margin of the Roman Wall",
  which is this route's upper line.
- gain_m `2158.0` (7,080 ft): MP route length "7080 ft" (trailhead to summit). The Peak Seeker gives
  "Elevation change: 7,080 feet" (https://thepeakseeker.com/routes/coleman-deming-route-mount-baker/).
- length_km `17.70` (11 mi RT): The Peak Seeker, "Route distance: 11 miles round trip". The Colorado
  Mountain Club gives 11.8 mi from a different trailhead reference.
- high_point_m `3286.0` (10,781 ft): WP Mount Baker, the summit.
- style `glacier climb`, season `late May–Aug`: USFS Coleman Glacier Climbing Route
  (https://www.fs.usda.gov/r06/mbs/recreation/coleman-glacier-climbing-route) says "The best conditions are from late May to August".

### Mt Adams South Spur
- grade `easy snow`: MP https://www.mountainproject.com/route/105883004/south-spur ("Easy Snow").
- gain_m `2042.2` (6,700 ft), length_km `19.31` (12 mi RT): USFS Trail #183 South Climb
  (https://www.fs.usda.gov/r06/giffordpinchot/recreation/trails/trail-183-south-climb) says "about 6,700
  vertical feet" and "about 12 miles" trailhead to summit and back. WTA "Mount Adams South Climb" agrees
  (12.0 mi RT, 6,700 ft).
- high_point_m `3741.7` (12,276 ft): USFS Mt. Adams Summit page and WTA. WP gives 12,276 ft in the lead
  and 12,281 ft (NAVD88) in the body. I used the figure USFS publishes.
- season `May–Sep`: USFS requires a climbing pass "from May 1st to September 30th" and calls October–April the off-season.
- first_ascent omitted. MP says "Unknown. 1860s likely". WP says the 1854 first ascent of Adams
  probably went up the North Cleaver, not this route.

### Worm Flows
- grade `easy snow`: MP https://www.mountainproject.com/route/107353369/worm-flows.
- gain_m `1737.4` (5,700 ft): USFS Worm Flows trailhead page and WP Mount St. Helens ("gains about
  5,700 feet"). WTA gives 5,699 ft. MP gives 5,800 ft and the Mount St. Helens Institute gives 5,563 ft.
- length_km `19.31` (12 mi RT): USFS (https://www.fs.usda.gov/r06/giffordpinchot/recreation/trailhead-worm-flows-winter-climbing-route),
  "Round trip is approximately 12 miles". WTA also lists 12.0 mi RT.
- high_point_m `2549.0` (8,363 ft): WP Mount St. Helens, post-1980 summit. The true summit is about
  0.3 mi west along the rim (MP).
- season `winter–early spring`: USFS says it "is the primary route used by climbers during the winter and early spring".

## Crags and formations

### The Chief
- tagline, type `granite monolith`, height_m `700`: WP Stawamus Chief says it "towers over 700 m … above
  … Howe Sound. It is one of the largest granite monoliths in the world." Summit (Third Peak) 702 m, not used.
- rock `granite`: WP ("granitic dome"; the geology section specifies granodiorite). style `trad`: MP
  Stawamus Chief (https://www.mountainproject.com/area/105805895/stawamus-chief).
- classic `Grand Wall, 5.11a A0, 9 pitches`: MP https://www.mountainproject.com/route/105806397/the-grand-wall
  ("Trad, Aid, 1000 ft, 9 pitches, Grade III"; FA July 1961, Ed Cooper & Jim Baldwin).

### Smith Rock
- tagline: WP Smith Rock State Park says "generally considered the birthplace of modern American sport climbing".
- height_m `182.9` (600 ft): WP says "making the cliffs about 600 feet (182.9 meters) high".
- type `sport crag`, style `sport & trad`, rock `welded tuff`: MP
  https://www.mountainproject.com/area/105788989/smith-rock says "one of the best sport climbing areas in
  the United States … Although best known for its sport climbing traditional climbers can find plenty",
  and "The main cliffs are made of volcanic welded tuff".
- classic `Chain Reaction, 5.12c`: MP https://www.mountainproject.com/route/105789917/chain-reaction
  (Sport, one pitch, FA Alan Watts Feb 1983, "One of the most fun and photogenic routes at Smith (and
  maybe the whole U.S.)"). I picked it over *To Bolt or Not to Be* (5.14a) because the blurb already names that one.

### Index Town Walls
- rock `granite`, style `sport & trad`, height_m `152.4` (500 ft): MP Index
  (https://www.mountainproject.com/area/105790635/index) says "the state's best steep granite", "now
  Index has roughly as much sport as trad", and "long 500'-high walls".
- type `granite cliffs`: descriptive, from the same page.
- classic `Great Northern Slab, 5.7, 3 pitches`: MP https://www.mountainproject.com/route/105790657/great-northern-slab
  ("Trad, 250 ft, 3 pitches, Grade II"). It is one of MP's most-voted Lower Town Wall classics (630 votes).
  **Judgment call:** Godzilla (5.9, 853 votes) and City Park (5.13+, America's hardest crack when freed in 1986) are the other candidates.

### Vantage
- type `columnar basalt crag`, rock `basalt`, style `sport & trad`: MP Frenchman Coulee (Vantage)
  (https://www.mountainproject.com/area/105792231/frenchman-coulee-vantage) says "The columnar basalt
  creates a great balance of sport and trad routes". WP Frenchman Coulee confirms the basalt bedrock.
- No `classic`: there is no single signature route. MP's most-voted classic is Air Guitar (5.10a), if you want one.

### Skaha Bluffs
- type `sport crag`, style `sport`, rock `gneiss`, season `Mar–Oct/Nov`: MP Skaha Bluffs
  (https://www.mountainproject.com/area/105946462/skaha-bluffs) says it is "primarily known for its
  abundance of moderate sport climbs", "The rock is Gneiss", and "The season runs from March to October or November".
- No `classic`, for the same reason as Vantage. MP's most-voted is Plum Line (5.9+).

### Castle Rock (Leavenworth)
- style `trad`, type `trad crag`: MP Castle Rock (https://www.mountainproject.com/area/105790784/castle-rock)
  says "options for trad leaders". Wenatchee Outdoors says "top notch 'trad' climbing".
- rock `quartz diorite`: MP Tumwater Canyon (https://www.mountainproject.com/area/105794001/tumwater-canyon)
  says "rock type (quartz diorite)". Wenatchee Outdoors calls it "granite".
- classic `Saber, 5.6, 2 pitches`: MP https://www.mountainproject.com/route/105792672/saber ("Trad, 280 ft,
  2 pitches"; first climbed 1950, FA Pete Schoening).

### Yamnuska
- elevation_m `2240`: WP Mount John Laurie ("approximately 2,240 m").
- rock `limestone`, style `trad`, type `limestone wall`: MP Yamnuska
  (https://www.mountainproject.com/area/105916245/yamnuska) says "home to traditional climbing in the
  Canadian Rockies" and "the rock is limestone". WP describes the face as Cambrian Eldon Formation carbonate.
- classic `Grillmair's Chimneys, 5.6, 8 pitches`: MP https://www.mountainproject.com/route/105933306/grillmairs-chimneys
  ("5.6 PG13, Trad, 1000 ft, 8 pitches, Grade III"; "the first route put up on Yamnuska").

### Bugaboos
- rock `granite`, style `alpine rock`, season `Jun–Sep`: MP Bugaboos
  (https://www.mountainproject.com/area/105868061/bugaboos) says "All the rock is alpine granite" and
  "The climbing season is generally June to September".
- classic `Bugaboo Spire NE Ridge, 5.8, 10 pitches`: MP https://www.mountainproject.com/route/105889511/north-east-ridge
  ("Trad, Alpine, 1500 ft, 10 pitches, Grade IV"). WP Bugaboo Spire says it is in *Fifty Classic Climbs*
  and gives "12 pitches"; I used MP's count.
- No `elevation_m`, because the row covers a group of spires. The map pin sits on Bugaboo Spire, which
  is 3,204 m per WP, but North Howser (3,412 m) is the group's highest point.

### Howser Towers
- elevation_m `3412`, first_ascent `1916, Conrad Kain and party`: WP Howser Spire. The North Tower is
  3,412 m, the highest in the Bugaboos. Its first ascent was Aug 1916 by Kain, A. & E. MacCarthy,
  J. Vincent and H. Frind. Both figures refer to the North Tower.
- classic `Beckey-Chouinard, 5.10, 15 pitches`: MP https://www.mountainproject.com/route/105872592/beckey-chouinard
  ("Trad, Alpine, 2000 ft, 15 pitches, Grade IV"; FA Beckey & Chouinard, Aug 1961).
- rock, style, season: MP Howser Towers and MP Bugaboos (same park-wide season).

### Liberty Bell
- elevation_m `2353.1` (7,720 ft): MP Liberty Bell (https://www.mountainproject.com/area/105797864/liberty-bell)
  says "The summit is at 7720'". The WP infobox gives 7,720 ft (peakbagger).
- first_ascent `1946, Beckey, O'Neil & Welsh`: WP says 27 Sep 1946, Fred Beckey, Jerry O'Neil and Charles
  Welsh, by the Beckey Route. MP agrees.
- rock `granite`, season `Jul–Sep`: WP ("carved from the granite of the Golden Horn batholith"; "July through
  September offer the most favorable weather").
- classic `Beckey Route, 5.6, 4 pitches`: MP https://www.mountainproject.com/route/105797867/beckey-route-sw-face
  ("Trad, Alpine, 500 ft, 4 pitches, Grade II"). WP's route list gives 3 pitches; I used MP's count.

## Traverses

### Birthday Tour
- gain_m `1066.8` (3,500 ft), high_point_m `2316.5` (7,600 ft): skimo.co https://skimo.co/the-birthday-tour-washington.
- season `Apr–Jun`: derived from skimo, which says "The highway usually opens anywhere from mid April to
  mid May and the tour remains viable for usually a month after opening". climberkyle.com
  (https://climberkyle.com/2019/05/12/wa-pass-birthday-tour/) calls it a half-day tour.
- No length: the only mileage found ("about 5 miles") is a reader comment describing a hairpin-start variant.

### Enchantments
- length_km `28.97` (18.0 mi one-way thru-hike), gain_m `1371.6` (4,500 ft), high_point_m `2377.4`
  (7,800 ft, Aasgard Pass): WTA https://www.wta.org/go-hiking/hikes/enchantment-lakes. The thru-hike runs
  from Stuart Lake trailhead to Snow Lakes trailhead, as the blurb describes.
- No days or season: WTA gives neither for the thru-hike.

### Isolation Traverse
- length_km `43.45` (about 27 mi), gain_m `4267.2` (14,000 ft): climberkyle.com
  (https://climberkyle.com/2020/05/27/the-isolation-traverse/) gives "~ 27 miles, 14,000+ ft gain". skimo.co
  (https://skimo.co/isolation-traverse-washington) gives 14,000 ft and "Distance 28.00" with no unit shown.
- days `3–5`: skimo describes a three-day version. turns-all-year.com's report took five days
  (https://www.turns-all-year.com/trip-reports/june-17-21-north-cascades-np-isolation-traverse). Fast
  parties do it in one push.
- season `Apr–Jun`: skimo says "as early as April most years, but May is the optimal time". climberkyle
  says late May to early June is prime. The turns-all-year trip was 17–21 June.

### Magic S Loop
- gain_m `2438.4` (8,000 ft), high_point_m `2377.4` (7,800 ft): skimo.co https://skimo.co/magic-s-loop-washington.
  climberkyle.com (https://climberkyle.com/2020/06/23/the-magic-s-loop/) gives "about 8000 ft of gain"
  and wildsnow.com gives "about 8,000 feet".
- first_done `2007, Sky Sjue & Dan Helmstadter`: climberkyle ("First done in June 2007") and wildsnow
  (https://wildsnow.com/7788/magic-s-loop-ski-tour-pnw/).
- days `1`: climberkyle's party took 10 h car to car and wildsnow's took 12 h.
- season `Apr–early Jul`: skimo says "The window for this tour is April to late June or early July".
- No length: skimo shows "Distance 10.00" with no unit.

### Ptarmigan Traverse
- first_done `1938, Ptarmigan Climbing Club`: WP Ptarmigan Traverse. The party was Bill Cox, Calder
  Bressler, Ray Clough and Tom Myers, and the trip took 13 days in July 1938.
- length_km `48.28` (30 mi): climberkyle.com (https://climberkyle.com/2019/07/09/the-extended-ptarmigan-traverse/)
  says "It crosses 30 miles … from Cascade Pass to the Suiattle River". StephAbegg.com gives "30+ miles".
  A Mountaineers trip report says "35+ mile".
- days `5–7`: StephAbegg.com (https://stephabegg.com/trip-reports/washington/ptarmigan-traverse-s-to-n/)
  says "Most parties take 5-7 days".
- style `mountaineering`: WP calls it "an alpine climbing route". It is also skied in spring.
- No gain or high point: the only figure found ("13000+ ft gain/loss") mixes gain and loss.

### Spearhead Traverse
- length_km `35`: Spearhead Huts Society (https://spearheadhuts.org/) says "the 35-kilometre Spearhead
  Traverse" with "13 glaciers". The Outbound also gives 35 km.
- gain_m `2000`, days `1–3`: The Outbound (https://www.theoutbound.com/canada/skiing/winter-traversing-of-spearhead)
  gives "Elevation Gain: ~ 6560 ft. / 2000 m" and "Duration: 1 - 3 Days". Saul Greenberg's GPS page gives
  "~2000m overall" and 1–3+ days.

### Wapta Traverse
- length_km `50`, gain_m `2400`: ACC Ski Traverses (https://alpineclubofcanada.ca/ski-traverses/) gives
  "Wapta Traverse 50km 2400m ascent 2700m descent", Peyto Hut to Sherbrooke Lake. **Other sources give
  about 40 km**: Cloud Nine Guides says "more than 40km" and voyageurtripper gives "5 days / 40 km".
  I used the hut operator's figure.
- days `5`, season `Mar–Apr`: 57hours guided trip (https://57hours.com/adventure/wapta-traverse-hut-to-hut-skiing/)
  says "5 full days" and "Season March through April". voyageurtripper also gives 5 days.

## Hikes

### Chilkoot Trail
- length_km `53.1` (33 mi one-way, Dyea to Bennett): PC Chilkoot (https://parks.canada.ca/lhn-nhs/yt/chilkoot/activ/randonnee-cdn-hiking)
  lists "Bennett: kilometre 53.1 / mile 33". NPS gives "33 mile".
- days `3–5`: WP Chilkoot Trail ("normally takes three to five days"). PC gives 3 to 5 nights.
- season `Jun–mid Sep`: PC ("summer hiking season (June to mid September)").
- No gain or high point. PC says "over 1000 meters (3500 feet)" of gain, which is a lower bound. The
  pass elevation varies by source: 3,501, 3,525, 3,556 or 3,759 ft.

### Crypt Lake
- length_km `17.2` (return), gain_m `675`: PC Waterton day hikes
  (https://parks.canada.ca/pn-np/ab/waterton/activ/experiences/randonee-hiking/journee-day). WP gives
  17.2 km RT and about 700 m.

### Dog Mountain
- length_km `9.66` (6.0 mi RT), gain_m `853.4` (2,800 ft), high_point_m `898.6` (2,948 ft): WTA
  https://www.wta.org/go-hiking/hikes/dog-mountain. Oregon Hikers gives 6.9 mi for its loop, with the same
  gain and high point. No season: the hike is open all year, and only spring weekends need permits.

### Rattlesnake Ledge
- length_km `6.44` (4.0 mi RT), gain_m `353.6` (1,160 ft), high_point_m `633.4` (2,078 ft): WTA
  https://www.wta.org/go-hiking/hikes/rattlesnake-ledge. WP Rattlesnake Ridge also gives 1,160 ft above the lake.

### Skyline Trail
- length_km `44.1` (one-way), days `2–3`, high_point_m `2510` (The Notch), season `early Jul–early Oct`:
  PC Jasper (https://parks.canada.ca/pn-np/ab/jasper/activ/passez-stay/arrierepays-backcountry/sugg-sentiers_trip-ideas/skyline)
  says "44.1 km one-way", "2 - 3 days", "The Notch (2510 m)", and "can typically only be hiked between
  early July and early October". No total gain is published.

### Timberline Trail
- length_km `64.37` (about 40 mi loop), days `3–4`, built: USFS Timberline Trail #600
  (https://www.fs.usda.gov/r06/mthood/recreation/trails/timberline-trail-600) says "~40-mile trail",
  "Most backpackers take 3 or 4 days", and "constructed primarily by the Civilian Conservation Corps in
  the 1930s". WP also says the CCC built it. WTA says "roughly 40-mile"; Oregon Hikers gives 38.3 mi.
- gain_m `2743.2` (9,000 ft): WP and Oregon Hikers
  (https://www.oregonhikers.org/field_guide/Timberline_Trail_around_Mount_Hood_Hike) both give 9,000 ft.
  WTA's calculated figure is 12,338 ft.
- high_point_m `2240.3` (7,350 ft): Oregon Hikers. WTA gives 7,336 ft.
- season `summer–early fall`: Oregon Hikers ("Summer and early Fall").
