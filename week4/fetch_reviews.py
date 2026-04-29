"""Fetch app reviews from the Week 4 API and export category and helpful votes to CSV."""

import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://hcde530-week4-api.onrender.com/reviews"
OUTPUT_CSV = Path(__file__).parent / "reviews_category_helpful.csv"
PAGE_SIZE = 100
# Cap how many reviews to pull, print, and write (full dataset is 500).
MAX_RESPONSES = 70
USER_AGENT = "hcde530-week4-fetch/1.0"

# This function is fetch the reviews from the API 
def fetch_reviews_page(offset: int, limit: int) -> dict:
    """Return one page of the /reviews API as a dict."""
    query = urllib.parse.urlencode({"offset": offset, "limit": limit})
    url = f"{BASE_URL}?{query}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_reviews_limited(max_count: int) -> list[dict]:
    """Fetch up to max_count reviews from the first page(s) of the API."""
    all_reviews: list[dict] = []
    offset = 0
    while len(all_reviews) < max_count:
        chunk_limit = min(PAGE_SIZE, max_count - len(all_reviews))
        data = fetch_reviews_page(offset=offset, limit=chunk_limit)
        reviews = data.get("reviews") or []
        if not reviews:
            break
        remaining = max_count - len(all_reviews)
        all_reviews.extend(reviews[:remaining])

        total = int(data.get("total") or 0)
        returned = int(data.get("returned", len(reviews)))
        if returned == 0 or offset + returned >= total:
            break
        offset += returned

    return all_reviews


def write_csv(rows: list[dict], path: Path) -> None:
    """Write category and helpful_votes columns to path."""
    fieldnames = ["category", "helpful_votes"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "category": (row.get("category") or "").strip(),
                    "helpful_votes": row.get("helpful_votes", ""),
                }
            )


def main() -> int:
    try:
        reviews = fetch_reviews_limited(MAX_RESPONSES)
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as exc:
        print(f"Failed to fetch reviews: {exc}", file=sys.stderr)
        return 1

    for review in reviews:
        category = (review.get("category") or "").strip()
        helpful = review.get("helpful_votes", "")
        print(f"{category}\t{helpful}")

    write_csv(reviews, OUTPUT_CSV)
    print(f"\nSaved {len(reviews)} rows to {OUTPUT_CSV}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
