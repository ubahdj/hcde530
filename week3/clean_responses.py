"""Clean response rows from responses.csv and write normalized output."""

import argparse
import csv
from pathlib import Path


INPUT_FILE = "responses.csv"
OUTPUT_FILE = "responses_cleaned.csv"


def clean_responses(input_path: Path, output_path: Path) -> None:
    """Filter empty names and capitalize all values in the 'row' column."""
    with input_path.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        fieldnames = reader.fieldnames or []
        cleaned_rows = []

        for response in reader:
            name_value = (response.get("name") or "").strip()
            if not name_value:
                continue

            row_value = (response.get("row") or "").strip().capitalize()
            response["row"] = row_value
            cleaned_rows.append(response)

    with output_path.open("w", encoding="utf-8", newline="") as destination:
        writer = csv.DictWriter(destination, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)


def parse_args() -> argparse.Namespace:
    """Parse optional input/output file paths from the command line."""
    parser = argparse.ArgumentParser(description="Clean response CSV data.")
    parser.add_argument("input_file", nargs="?", default=INPUT_FILE)
    parser.add_argument("output_file", nargs="?", default=OUTPUT_FILE)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    source_path = Path(args.input_file)
    destination_path = Path(args.output_file)

    if not source_path.exists():
        print(f"Input file not found: {INPUT_FILE}")
    else:
        clean_responses(source_path, destination_path)
        print(f"Cleaned data written to {OUTPUT_FILE}")
