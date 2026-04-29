"""Episodes airing on a birthday date via TVMaze."""

import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path
# This api url is looking at the tvmaze and it looking at episodes that are airing on my birthdte 
API_BASE = "https://api.tvmaze.com"
#I am extrating the date 09-17-2001 because it is my birthday and i am curious to see what aired lol
TARGET_DATE = "2001-09-17"
OUTPUT_CSV = Path(__file__).parent / f"shows_on_mybday_{TARGET_DATE}.csv"
OUTPUT_CSV_SUMMARY = Path(__file__).parent / f"mybday_categories_{TARGET_DATE}.csv"
USER_AGENT = "hcde530-shows-on-mybday/1.0"


def fetch_schedule_for_date(iso_date: str) -> list[dict]:
    """Return TVMaze schedule entries for a calendar date (YYYY-MM-DD)."""
    query = urllib.parse.urlencode({"date": iso_date})
    url = f"{API_BASE}/schedule?{query}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def show_category_label(show: dict) -> str:
    """
    TVMaze has no single 'category' field; combine show type and genres for a readable label.
    """
    show_type = (show.get("type") or "").strip()
    genres = show.get("genres") or []
    genre_text = ", ".join(genres) if genres else ""
    if show_type and genre_text:
        return f"{show_type} ({genre_text})"
    if show_type:
        return show_type
    if genre_text:
        return genre_text
    return "unknown"


def main() -> int:
    try:
        entries = fetch_schedule_for_date(TARGET_DATE)
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as exc:
        print(f"Failed to fetch schedule: {exc}", file=sys.stderr)
        return 1

    #  #API is reuturing a list of the episoodes that were airied that day 

    rows = []
    for entry in entries:
        if (entry.get("airdate") or "") != TARGET_DATE:
            continue
        show = entry.get("show") or {}
        category = show_category_label(show)
        rows.append(
            {
                "show_name": (show.get("name") or "").strip(),
                "episode_name": (entry.get("name") or "").strip(),
                "airdate": entry.get("airdate") or "",
                "category": category,
            }
        )

    for row in rows:
        print(f"{row['category']}\t{row['show_name']}\t{row['episode_name']}")

    fieldnames = ["show_name", "episode_name", "airdate", "category"]
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    category_counts = Counter(row["category"] for row in rows)
    with OUTPUT_CSV_SUMMARY.open("w", encoding="utf-8", newline="") as handle:
        summary_writer = csv.DictWriter(
            handle, fieldnames=["category", "episode_count"]
        )
        summary_writer.writeheader()
        for category, count in sorted(category_counts.items()):
            summary_writer.writerow(
                {"category": category, "episode_count": count}
            )

    print(f"\nSaved {len(rows)} rows to {OUTPUT_CSV}", file=sys.stderr)
    print(f"Saved category summary to {OUTPUT_CSV_SUMMARY}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())