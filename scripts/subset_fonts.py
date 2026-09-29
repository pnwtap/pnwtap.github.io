"""Subset Open Sans into the two small woff2 files the site serves from static/.

Self-hosting (rather than Google Fonts) keeps two extra origins and a render-blocking
stylesheet off the page's critical path. Only re-run this to change the character set.

    python -m venv /tmp/fontenv && /tmp/fontenv/bin/pip install fonttools brotli
    curl -L -o /tmp/OpenSans.ttf 'https://github.com/google/fonts/raw/main/ofl/opensans/OpenSans%5Bwdth,wght%5D.ttf'
    curl -L -o /tmp/OpenSans-Italic.ttf 'https://github.com/google/fonts/raw/main/ofl/opensans/OpenSans-Italic%5Bwdth,wght%5D.ttf'
    /tmp/fontenv/bin/python scripts/subset_fonts.py /tmp/OpenSans.ttf /tmp/OpenSans-Italic.ttf

Upright: variable, weights 400–700 (the page uses 400/600/700). Italic: static 400.
If you change the files, bump the number in their names (static/style.css and
templates/index.html.jinja refer to them) so browsers fetch the new ones.
"""
import io
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

STATIC = Path(__file__).resolve().parent.parent / "static"

# Latin-1, general punctuation (– — ‘ ’ “ ” • …), and a few symbols the blurbs use.
# Keep in sync with the unicode-range in static/style.css.
UNICODES = "U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2212,U+2248,U+2260,U+2264-2265"


def build(src: str, out: Path, axes: dict) -> None:
    buf = io.BytesIO()
    instancer.instantiateVariableFont(TTFont(src), axes).save(buf)
    buf.seek(0)
    font = TTFont(buf)   # reload: subsetting a freshly instanced font trips over lazy gvar data
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.hinting = False
    opts.layout_features = ["kern", "liga", "ccmp", "locl", "mark", "mkmk", "tnum", "lnum"]
    opts.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]   # keep copyright + licence strings
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=subset.parse_unicodes(UNICODES))
    sub.subset(font)
    font.flavor = "woff2"
    font.save(out)
    print(f"{out.name}: {out.stat().st_size:,} bytes")


if __name__ == "__main__":
    upright, italic = sys.argv[1:3]
    build(upright, STATIC / "open-sans-1.woff2", {"wdth": 100, "wght": (400, 700)})
    build(italic, STATIC / "open-sans-italic-1.woff2", {"wdth": 100, "wght": 400})
