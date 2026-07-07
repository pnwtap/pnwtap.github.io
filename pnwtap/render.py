"""Build the JSON payload and render the static site into docs/."""
import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


def build_payload(locations, schedule, image_map, config) -> dict:
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
        "config": {
            "D_km": config.D_KM,
            "multipliers": config.MULTIPLIERS,
            "ramp": config.RAMP,
            "emoji": config.EMOJI,
            "tileUrl": config.TILE_URL,
            "tileAttribution": config.TILE_ATTRIBUTION,
            "bbox": config.BBOX,
            "center": config.CENTER,
            "zoom": config.DEFAULT_ZOOM,
        },
    }


def render_site(locations, schedule, image_map, config, *, docs_dir, template_dir, static_dir) -> Path:
    docs_dir = Path(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    payload = build_payload(locations, schedule, image_map, config)
    data_json = json.dumps(payload).replace("<", "\\u003c")  # keep any "</script>" in blurbs safe

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html"]),
    )
    html = env.get_template("index.html.jinja").render(data_json=data_json)

    index_path = docs_dir / "index.html"
    index_path.write_text(html, encoding="utf-8")
    for fname in ("game.js", "style.css"):
        shutil.copy(Path(static_dir) / fname, docs_dir / fname)
    return index_path
