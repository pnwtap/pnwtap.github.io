"""Build the pnwtap static site from the sheet (or a local CSV) into docs/."""
import argparse
import json
from datetime import date
from pathlib import Path

from pnwtap import config, sheet, schedule, images, render

ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the pnwtap static site.")
    parser.add_argument("--csv", help="local CSV file to use instead of the published sheet URL")
    parser.add_argument("--start", help="ISO start date for the schedule (default: today)")
    args = parser.parse_args()

    if args.csv:
        csv_text = Path(args.csv).read_text(encoding="utf-8")
    else:
        csv_text = sheet.fetch_csv(config.SHEET_CSV_URL)

    locations = sheet.parse_locations(csv_text, config.BBOX)
    print(f"loaded {len(locations)} locations")

    docs_dir = ROOT / "docs"
    image_map = images.localize_images(locations, docs_dir)
    if image_map:
        print(f"localized {len(image_map)} images")

    start = date.fromisoformat(args.start) if args.start else date.today()
    sched = schedule.build_schedule(locations, start, config.HORIZON_DAYS, config.RAMP, config.SEED)
    print(f"scheduled {len(sched)} days starting {start.isoformat()}")

    mask_path = ROOT / "data" / "region_mask.json"
    region_mask = json.loads(mask_path.read_text(encoding="utf-8")) if mask_path.exists() else []
    if region_mask:
        print(f"loaded region stencil: {len(region_mask)} rings")

    index_path = render.render_site(
        locations, sched, image_map, config,
        docs_dir=docs_dir, template_dir=ROOT / "templates", static_dir=ROOT / "static",
        region_mask=region_mask,
    )
    print(f"wrote {index_path}")


if __name__ == "__main__":
    main()
