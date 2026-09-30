"""Build the JSON payload and render the static site into docs/."""
import hashlib
import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from pnwtap.facts import card
from pnwtap.geometry import encode_polyline


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
            **({"prompt": loc.prompt} if loc.prompt else {}),
            "kind": loc.kind,
            "facts": card(loc.facts, loc.category, config.FACTS, config.CARDS),
        })
        if loc.members:                     # an "any of" place: its targets carry the geometry
            locs[-1]["geometry"] = []
            locs[-1]["members"] = [{"name": m.name, "geometry": [[lat, lng] for (lat, lng) in m.geometry],
                                    "kind": m.kind} for m in loc.members]
    return {
        "locations": locs,
        "schedule": schedule,
        "regionMask": region_mask or [],
        "config": {
            "epoch": config.EPOCH,
            "timeZone": config.TIME_ZONE,
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


def tile_origin(tile_url: str) -> str:
    """https://host of the imagery tiles, for the page's preconnect hint."""
    return "/".join(tile_url.split("/")[:3])


def phone_tile_urls(config) -> list[str]:
    """The imagery tiles a phone's opening view shows (config.PHONE_START_TILES)."""
    t = getattr(config, "PHONE_START_TILES", None)
    if not t:
        return []
    return [config.TILE_URL.format(z=t["z"], x=x, y=y)
            for y in range(t["y"][0], t["y"][1] + 1) for x in range(t["x"][0], t["x"][1] + 1)]


def render_site(locations, schedule, image_map, config, *, docs_dir, template_dir, static_dir, region_mask=None) -> Path:
    docs_dir = Path(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    payload = build_payload(locations, schedule, image_map, config, region_mask)
    for loc in payload["locations"]:                  # paths travel as encoded polylines
        loc["geometry"] = encode_polyline(loc["geometry"])
        for m in loc.get("members", []):
            m["geometry"] = encode_polyline(m["geometry"])
    payload["regionMask"] = [encode_polyline(ring) for ring in payload["regionMask"]]
    data_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    data_json = data_json.replace("<", "\\u003c")  # keep any "</script>" in blurbs safe

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=True,
    )
    # each asset gets its own content hash as ?v=, so browsers never pair a fresh
    # index.html with a stale cached game.js (GitHub Pages caches ~10 min), and an
    # unchanged file (Leaflet) stays cached across releases
    versions = {src.name: hashlib.sha1(src.read_bytes()).hexdigest()[:10]
                for src in Path(static_dir).iterdir() if src.is_file()}
    html = env.get_template("index.html.jinja").render(
        data_json=data_json,
        asset=lambda name: f"{name}?v={versions[name]}",
        tile_origin=tile_origin(config.TILE_URL),
        phone_tiles=phone_tile_urls(config),
        goatcounter=getattr(config, "GOATCOUNTER", ""),
    )

    index_path = docs_dir / "index.html"
    index_path.write_text(html, encoding="utf-8")
    for src in Path(static_dir).iterdir():
        if src.is_file():
            shutil.copy(src, docs_dir / src.name)
    return index_path
