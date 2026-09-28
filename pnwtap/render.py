"""Build the JSON payload and render the static site into docs/."""
import hashlib
import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from pnwtap.facts import card


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
            "kind": loc.kind,
            "facts": card(loc.facts, loc.category, config.FACTS, config.CARDS),
        })
    return {
        "locations": locs,
        "schedule": schedule,
        "regionMask": region_mask or [],
        "config": {
            "epoch": config.EPOCH,
            "categories": {k: {"icon": icon, "label": label} for k, (icon, label) in config.CATEGORIES.items()},
            "scoreNearKm": config.SCORE_NEAR_KM,
            "scoreZeroKm": config.SCORE_ZERO_KM,
            "scoreShape": config.SCORE_SHAPE,
            "feedback": {
                "key": config.FEEDBACK_ACCESS_KEY, "endpoint": config.FEEDBACK_ENDPOINT,
                "bug": config.FEEDBACK_BUG_URL, "place": config.FEEDBACK_PLACE_URL,
            },
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
    data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    data_json = data_json.replace("<", "\\u003c")  # keep any "</script>" in blurbs safe

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
    html = env.get_template("index.html.jinja").render(
        data_json=data_json, v=digest.hexdigest()[:10], goatcounter=getattr(config, "GOATCOUNTER", ""),
    )

    index_path = docs_dir / "index.html"
    index_path.write_text(html, encoding="utf-8")
    for src in Path(static_dir).iterdir():
        if src.is_file():
            shutil.copy(src, docs_dir / src.name)
    return index_path
