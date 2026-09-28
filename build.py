"""Build the pnwtap static site from the sheet (or a local CSV) into docs/."""
import argparse
import json
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

from pnwtap import config, sheet, schedule, images, render

ROOT = Path(__file__).resolve().parent
LOCAL_CSV = ROOT / "data" / "locations.csv"
MASK_PATH = ROOT / "data" / "region_mask.json"
LOCK_PATH = ROOT / "data" / "schedule_lock.json"


def load_csv(csv_arg: str | None) -> str:
    if csv_arg:
        return Path(csv_arg).read_text(encoding="utf-8")
    if config.SHEET_CSV_URL.startswith("http"):
        return sheet.fetch_csv(config.SHEET_CSV_URL)
    print(f"SHEET_CSV_URL not set in pnwtap/config.py — using {LOCAL_CSV.relative_to(ROOT)}")
    return LOCAL_CSV.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the pnwtap static site.")
    parser.add_argument("--csv", help="local CSV file to use instead of the published sheet URL")
    parser.add_argument("--today", help="ISO date to treat as today (default: the real date)")
    parser.add_argument("--no-lock", action="store_true",
                        help="ignore and don't update data/schedule_lock.json (for experiments)")
    args = parser.parse_args()

    region_mask = json.loads(MASK_PATH.read_text(encoding="utf-8")) if MASK_PATH.exists() else []

    locations = sheet.parse_locations(
        load_csv(args.csv), config.BBOX, categories=set(config.CATEGORIES), region=region_mask,
    )
    tiers = Counter(loc.difficulty for loc in locations)
    print(f"loaded {len(locations)} locations "
          f"({tiers['easy']} easy / {tiers['medium']} medium / {tiers['hard']} hard)")

    docs_dir = ROOT / "docs"
    image_map = images.localize_images(locations, docs_dir)
    if image_map:
        print(f"localized {len(image_map)} images")

    today = date.fromisoformat(args.today) if args.today else date.today()
    epoch = date.fromisoformat(config.EPOCH)

    lock: dict[str, list[str]] = {}
    if not args.no_lock and LOCK_PATH.exists():
        lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    locked, dropped = schedule.resolve_lock(lock, locations)
    if dropped:
        print(f"warning: {len(dropped)} locked day(s) reference removed/renamed locations and were "
              f"re-rolled: {', '.join(dropped[-5:])}{' …' if len(dropped) > 5 else ''}")

    horizon = (today - epoch).days + config.HORIZON_DAYS + 1
    sched = schedule.build_schedule(locations, epoch, horizon, config.RAMP, config.SEED, locked=locked)
    last = epoch + timedelta(days=horizon - 1)
    print(f"scheduled {len(sched)} days, {epoch.isoformat()} → {last.isoformat()} "
          f"({len(locked)} locked)")

    if not args.no_lock:
        lock.update(schedule.lock_through(sched, locations, today))
        lines = [f"  {json.dumps(d)}: {json.dumps(n, ensure_ascii=False)}" for d, n in sorted(lock.items())]
        LOCK_PATH.write_text("{\n" + ",\n".join(lines) + "\n}\n", encoding="utf-8")

    index_path = render.render_site(
        locations, sched, image_map, config,
        docs_dir=docs_dir, template_dir=ROOT / "templates", static_dir=ROOT / "static",
        region_mask=region_mask,
    )
    print(f"wrote {index_path}")


if __name__ == "__main__":
    main()
