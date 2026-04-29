"""Fetch reviews from the Week 4 API, summarize by category, and save a CSV."""

import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

BASE_URL = "https://hcde530-week4-api.onrender.com/reviews"
OUTPUT_CSV = Path(__file__).parent / "reviews_summary_by_category.csv"
PAGE_SIZE = 100
USER_AGENT = "hcde530-week4-summary/1.0"


def fetch_reviews_page(offset: int, limit: int) -> dict:
    """Return one page of the /reviews API as a dict."""
    query = urllib.parse.urlencode({"offset": offset, "limit": limit})
    url = f"{BASE_URL}?{query}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_all_reviews() -> list[dict]:
    """Paginate until all reviews are loaded."""
    all_reviews: list[dict] = []
    offset = 0
    while True:
        data = fetch_reviews_page(offset=offset, limit=PAGE_SIZE)
        reviews = data.get("reviews") or []
        all_reviews.extend(reviews)
        total = int(data.get("total") or 0)
        returned = int(data.get("returned", len(reviews)))
        if returned == 0 or offset + returned >= total:
            break
        offset += returned
    return all_reviews


def summarize_by_category(reviews: list[dict]) -> list[dict]:
    """Per category: count, average rating, average helpful votes."""
    buckets = defaultdict(lambda: {"count": 0, "rating_sum": 0, "helpful_sum": 0})

    for review in reviews:
        category = (review.get("category") or "").strip() or "unknown"
        rating = review.get("rating")
        helpful = review.get("helpful_votes")
        try:
            r = int(rating)
        except (TypeError, ValueError):
            continue
        try:
            h = int(helpful)
        except (TypeError, ValueError):
            h = 0
        b = buckets[category]
        b["count"] += 1
        b["rating_sum"] += r
        b["helpful_sum"] += h

    rows = []
    for category, b in sorted(buckets.items()):
        n = b["count"]
        rows.append(
            {
                "category": category,
                "review_count": n,
                "avg_rating": round(b["rating_sum"] / n, 2) if n else 0,
                "avg_helpful_votes": round(b["helpful_sum"] / n, 2) if n else 0,
            }
        )
    return rows


def write_summary_csv(rows: list[dict], path: Path) -> None:
    """Write summary rows to CSV."""
    fieldnames = ["category", "review_count", "avg_rating", "avg_helpful_votes"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    try:
        reviews = fetch_all_reviews()
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as exc:
        print(f"Failed to fetch reviews: {exc}", file=sys.stderr)
        return 1

    summary = summarize_by_category(reviews)
    print(f"Loaded {len(reviews)} reviews; {len(summary)} categories.\n")
    for row in summary:
        print(
            f"{row['category']}: "
            f"n={row['review_count']}, "
            f"avg_rating={row['avg_rating']}, "
            f"avg_helpful={row['avg_helpful_votes']}"
        )

    write_summary_csv(summary, OUTPUT_CSV)
    print(f"\nSaved summary to {OUTPUT_CSV}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
