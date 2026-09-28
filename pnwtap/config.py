"""All tunable configuration for pnwtap. Edit values here only."""

# Published-CSV URL of the Google Sheet (File → Share → Publish to web → CSV).
# For local development you can bypass this with `python build.py --csv data/sample_locations.csv`.
SHEET_CSV_URL = "PASTE_YOUR_PUBLISHED_CSV_URL_HERE"

# Scoring. A round scores on how far the tap lands from the feature (0 km inside an
# area or on a line):  100 * (1 - ln(1 + (d/NEAR)^SHAPE) / ln(1 + (ZERO/NEAR)^SHAPE)).
# Within about NEAR a miss costs almost nothing; beyond it the curve is log-scale, so
# every halving of the miss is worth the same ~14 points — the right valley, the right
# region and the right province all count — and 0 takes a miss of SCORE_ZERO_KM.
# With these values: 3 km → 99, 10 → 93, 20 → 84, 50 → 67, 100 → 54, 200 → 40,
# 500 → 22, 1000 → 8.
SCORE_NEAR_KM = 10.0
SCORE_ZERO_KM = 1500.0
SCORE_SHAPE = 2.0
RAMP = ["easy", "medium", "hard", "hard"]   # difficulty of each round, in order
MULTIPLIERS = [1, 2, 3, 4]           # per-round score multiplier; max score = 100*sum = 1000

# Scheduling
EPOCH = "2026-09-28"                 # puzzle #1 (launch day); curated days before it are "practice"
HORIZON_DAYS = 400                   # days of puzzles to bake ahead of the build date
SEED = 0                             # change to reshuffle all *future* days (played days are locked)
SPREAD_KM = 80                       # a day's places prefer to be at least this far apart...
MAX_PER_CATEGORY = 2                 # ...and to repeat a category at most this often (both soft)

# Share-string emoji per difficulty tier
EMOJI = {"easy": "🏅", "medium": "🔥", "hard": "🏆"}

# Allowed sheet categories: (icon, label shown to players)
CATEGORIES = {
    "peak": ("🏔️", "peak"), "hike": ("🥾", "hike"), "traverse": ("🎿", "traverse"),
    "road": ("🛣️", "road"), "climb": ("🧗", "climb"), "river": ("🏞️", "river"),
    "town": ("🏘️", "town"), "poi": ("📍", "landmark"), "lake": ("💧", "lake"),
    "glacier": ("🧊", "glacier"), "pass": ("⛰️", "pass"), "island": ("🏝️", "island"),
    "ski": ("⛷️", "ski area"), "waterfall": ("🌊", "waterfall"), "park": ("🌲", "park"),
}

# Facts: the optional `facts` column holds "key: value | key: value". Each key has a
# label, a unit kind (m / km / km2 get metric + imperial; int / str are shown as is),
# and whether it's a *clue* — safe to show on the guess prompt because it says what
# the place is, not where (grades, heights, populations). Everything shows on the
# reveal card. data/candidates/FACTS_SPEC.md documents the keys for sheet editors.
FACTS = {
    # key            (label,            kind,  clue)
    "tagline":       ("",               "str", True),    # its own line under the name
    "type":          ("Type",           "str", True),
    "grade":         ("Grade",          "str", True),
    "style":         ("Style",          "str", True),
    "pitches":       ("Pitches",        "int", True),
    "length_m":      ("Length",         "m",   True),
    "elevation_m":   ("Elevation",      "m",   True),
    "prominence_m":  ("Prominence",     "m",   False),
    "height_m":      ("Height",         "m",   True),
    "length_km":     ("Length",         "km",  True),
    "gain_m":        ("Elevation gain", "m",   True),
    "high_point_m":  ("High point",     "m",   True),
    "vertical_m":    ("Vertical",       "m",   True),
    "lifts":         ("Lifts",          "int", False),
    "area_km2":      ("Area",           "km2", True),
    "depth_m":       ("Max depth",      "m",   False),
    "days":          ("Days",           "str", True),
    "population":    ("Population",     "str", True),
    "rock":          ("Rock",           "str", False),
    "classic":       ("Classic",        "str", False),
    "range":         ("Range",          "str", False),
    "region":        ("Region",         "str", False),
    "founded":       ("Founded",        "str", False),
    "first_ascent":  ("First ascent",   "str", False),
    "first_done":    ("First done",     "str", False),
    "built":         ("Built",          "str", False),
    "last_eruption": ("Last eruption",  "str", False),
    "source":        ("Source",         "str", False),
    "mouth":         ("Mouth",          "str", False),
    "road":          ("Road",           "str", False),
    "season":        ("Season",         "str", False),
}

# The card for each landmark type: which facts lead, in order. Facts a row has that
# aren't listed still show, after these. The prompt's clue line takes the first three
# clue facts in this order.
CARDS = {
    "peak":      ["elevation_m", "type", "prominence_m", "range", "classic", "first_ascent", "last_eruption"],
    "climb":     ["grade", "style", "pitches", "length_m", "type", "rock", "height_m", "elevation_m",
                  "gain_m", "classic", "first_ascent", "first_done", "season"],
    "traverse":  ["style", "length_km", "days", "gain_m", "high_point_m", "first_done", "season"],
    "hike":      ["length_km", "gain_m", "days", "high_point_m", "season"],
    "town":      ["population", "type", "elevation_m", "region", "founded"],
    "lake":      ["type", "area_km2", "length_km", "depth_m", "elevation_m"],
    "river":     ["length_km", "source", "mouth"],
    "road":      ["type", "length_km", "high_point_m", "road", "built", "season"],
    "glacier":   ["type", "area_km2", "length_km", "range"],
    "pass":      ["elevation_m", "type", "road", "range"],
    "island":    ["type", "area_km2", "population", "high_point_m"],
    "ski":       ["vertical_m", "elevation_m", "lifts", "built"],
    "waterfall": ["height_m", "type"],
    "park":      ["type", "area_km2", "founded", "built"],
    "poi":       ["type", "height_m", "elevation_m", "area_km2", "length_km", "built"],
}

# Region bounding box for typo validation: (min_lat, min_lng, max_lat, max_lng).
# Covers WA, OR, BC, AB, and YT — the area the stencil (data/region_mask.json) spans.
BBOX = (41.5, -141.5, 70.0, -109.5)
# Each round opens framed on this box [[south, west], [north, east]] — the populated
# south of the region (OR → southern BC/AB); players zoom out for the far north.
START_BOUNDS = [[43.0, -125.5], [53.0, -113.0]]

# Hit counting: a GoatCounter site code (https://<code>.goatcounter.com). Empty = no
# counting. Counts page views plus a few events (started / finished / score band /
# shared); no cookies. Nothing is counted in ?playtest or on localhost.
GOATCOUNTER = "pnwtap"

# Map tiles (Esri, unlabeled, no API key): satellite imagery — naturally
# colourful (forest, snow, rock, water), deep zoom, and no place-name labels
# so answers aren't given away. Set HILLSHADE_URL to overlay shaded relief;
# left empty because the imagery already reads as terrain.
TILE_URL = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
HILLSHADE_URL = ""
TILE_ATTRIBUTION = "Imagery © Esri, Maxar, Earthstar Geographics"

# Zoom limits (MIN_ZOOM 4 lets you pull back to see the whole region framed
# against the solid background; tiles only render inside the region box)
MIN_ZOOM = 4
MAX_ZOOM = 12
