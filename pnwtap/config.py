"""All tunable configuration for pnwtap. Edit values here only."""

# Published-CSV URL of the Google Sheet (File → Share → Publish to web → CSV).
# For local development you can bypass this with `python build.py --csv data/sample_locations.csv`.
SHEET_CSV_URL = "PASTE_YOUR_PUBLISHED_CSV_URL_HERE"

# Scoring
D_KM = 40.0                          # distance (km) at which score decays by 1/e, for a point
D_MIN_KM = 10.0                      # floor for long lines / big areas, which get a tighter decay
                                     # so a 900 km river isn't a freebie (see geometry.decay_km)
RAMP = ["easy", "medium", "hard", "hard"]   # difficulty of each round, in order
MULTIPLIERS = [1, 2, 3, 4]           # per-round score multiplier; max score = 100*sum = 1000

# Scheduling
EPOCH = "2026-07-07"                 # puzzle #1; the schedule is always built from here
HORIZON_DAYS = 400                   # days of puzzles to bake ahead of the build date
SEED = 0                             # change to reshuffle all *future* days (played days are locked)
SPREAD_KM = 80                       # a day's places prefer to be at least this far apart...
MAX_PER_CATEGORY = 2                 # ...and to repeat a category at most this often (both soft)

# Share-string emoji per difficulty tier
EMOJI = {"easy": "🏅", "medium": "🔥", "hard": "🏆"}

# Allowed sheet categories and the icon shown next to each prompt
CATEGORIES = {
    "peak": "🏔️", "hike": "🥾", "traverse": "🎿", "road": "🛣️", "climb": "🧗",
    "river": "🏞️", "town": "🏘️", "poi": "📍", "lake": "💧", "glacier": "🧊",
    "pass": "⛰️", "island": "🏝️",
}

# Region bounding box for typo validation: (min_lat, min_lng, max_lat, max_lng).
# Covers WA, OR, BC, AB, and YT — the area the stencil (data/region_mask.json) spans.
BBOX = (41.5, -141.5, 70.0, -109.5)
# Each round opens framed on this box [[south, west], [north, east]] — the populated
# south of the region (OR → southern BC/AB); players zoom out for the far north.
START_BOUNDS = [[43.0, -125.5], [53.0, -113.0]]

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
