"""Download prompt images referenced in the sheet into docs/img/ so the site is self-contained."""
import hashlib
from pathlib import Path

import requests

_EXT_BY_TYPE = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
}


def _default_download(url: str) -> tuple[bytes, str]:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.content, resp.headers.get("content-type", "")


def localize_images(locations, docs_dir, download=_default_download) -> dict[int, str]:
    img_dir = Path(docs_dir) / "img"
    img_dir.mkdir(parents=True, exist_ok=True)

    mapping: dict[int, str] = {}
    for idx, loc in enumerate(locations):
        if not loc.image:
            continue
        stem = hashlib.sha1(loc.image.encode()).hexdigest()[:12]

        cached = next(iter(img_dir.glob(stem + ".*")), None)
        if cached is not None:
            mapping[idx] = "img/" + cached.name
            continue

        try:
            content, content_type = download(loc.image)
        except Exception as exc:
            raise ValueError(f"location {loc.name!r}: failed to download image {loc.image}: {exc}") from exc

        ext = _EXT_BY_TYPE.get(content_type.split(";")[0].strip()) or Path(loc.image).suffix or ".jpg"
        name = stem + ext
        (img_dir / name).write_bytes(content)
        mapping[idx] = "img/" + name
    return mapping
