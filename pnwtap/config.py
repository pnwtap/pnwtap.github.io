"""All tunable configuration for pnwtap. Edit values here only."""

# Published-CSV URL of the Google Sheet (File → Share → Publish to web → CSV).
# For local development you can bypass this with `python build.py --csv data/sample_locations.csv`.
SHEET_CSV_URL = "PASTE_YOUR_PUBLISHED_CSV_URL_HERE"

# Scoring
D_KM = 40.0                          # distance (km) at which score decays by 1/e
RAMP = ["easy", "medium", "hard", "hard"]   # difficulty of each round, in order
MULTIPLIERS = [1, 2, 3, 4]           # per-round score multiplier; max score = 100*sum = 1000

# Scheduling
HORIZON_DAYS = 365                   # how many days of puzzles to bake ahead
SEED = 0                             # change to reshuffle the whole schedule

# Share-string emoji per difficulty tier
EMOJI = {"easy": "🏅", "medium": "🔥", "hard": "🏆"}

# Region bounding box for typo validation: (min_lat, min_lng, max_lat, max_lng).
# Covers WA, OR, BC, AB, and YT — the area the stencil (data/region_mask.json) spans.
BBOX = (41.5, -141.5, 70.0, -109.5)
CENTER = [49.5, -122.5]              # initial map center [lat, lng] (over the populated south)
DEFAULT_ZOOM = 6

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
