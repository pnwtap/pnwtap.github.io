"""Build the JSON payload and render the static site into docs/."""
import hashlib
import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def build_payload(locations, schedule, image_map, config, region_mask=None) -> dict:
    locs = []
    for idx, loc in enumerate(locations):
        locs.append({
            "name": loc.name,
            "category": loc.category,
            "difficulty": loc.difficulty,
            "geometry": [[lat, lng] for (lat, lng) in loc.geometry],
            "image": image_map.get(idx),
            "blurb": loc.blurb,
        })
    return {
        "locations": locs,
        "schedule": schedule,
        "regionMask": region_mask or [],
        "config": {
            "epoch": config.EPOCH,
            "categories": config.CATEGORIES,
            "D_km": config.D_KM,
            "multipliers": config.MULTIPLIERS,
            "ramp": config.RAMP,
            "emoji": config.EMOJI,
            "tileUrl": config.TILE_URL,
            "hillshadeUrl": config.HILLSHADE_URL,
            "tileAttribution": config.TILE_ATTRIBUTION,
            "bbox": config.BBOX,
            "startBounds": config.START_BOUNDS,
            "minZoom": config.MIN_ZOOM,
            "maxZoom": config.MAX_ZOOM,
        },
    }


def render_site(locations, schedule, image_map, config, *, docs_dir, template_dir, static_dir, region_mask=None) -> Path:
    docs_dir = Path(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    payload = build_payload(locations, schedule, image_map, config, region_mask)
    data_json = json.dumps(payload).replace("<", "\\u003c")  # keep any "</script>" in blurbs safe

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=True,
    )
    # content hash of the static assets, appended as ?v= so browsers never pair a
    # fresh index.html with a stale cached game.js (GitHub Pages caches ~10 min)
    digest = hashlib.sha1()
    for src in sorted(Path(static_dir).iterdir()):
        if src.is_file():
            digest.update(src.read_bytes())
    html = env.get_template("index.html.jinja").render(data_json=data_json, v=digest.hexdigest()[:10])

    index_path = docs_dir / "index.html"
    index_path.write_text(html, encoding="utf-8")
    for src in Path(static_dir).iterdir():
        if src.is_file():
            shutil.copy(src, docs_dir / src.name)
    return index_path
