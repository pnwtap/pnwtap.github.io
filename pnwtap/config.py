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

# PNW bounding box for typo validation: (min_lat, min_lng, max_lat, max_lng)
BBOX = (41.0, -126.0, 56.0, -112.0)
CENTER = [48.5, -121.0]              # initial map center [lat, lng]
DEFAULT_ZOOM = 6

# Unlabeled shaded-relief terrain tiles (Esri, no API key required)
TILE_URL = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}"
TILE_ATTRIBUTION = "Tiles © Esri — Source: Esri"
