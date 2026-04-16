import csv
from pathlib import Path


def calculate_average_experience(rows):
    """Return the average numeric experience_years value, or None if unavailable."""
    total_experience = 0
    valid_experience_rows = 0

    for row in rows:
        raw_years = row["experience_years"].strip()
        try:
            years = int(raw_years)
        except ValueError:
            # Fixed error: ValueError invalid literal for int() with base 10: 'fifteen'
            continue
        total_experience += years
        valid_experience_rows += 1

    if valid_experience_rows == 0:
        return None
    return total_experience / valid_experience_rows


def write_cleaned_rows(rows, fieldnames, output_path):
    """Write cleaned survey rows to a new CSV file."""
    cleaned_rows = []
    for row in rows:
        cleaned_row = {key: (value or "").strip() for key, value in row.items()}
        cleaned_row["role"] = cleaned_row["role"].title()
        cleaned_rows.append(cleaned_row)

    with open(output_path, "w", newline="", encoding="utf-8") as cleaned_file:
        writer = csv.DictWriter(cleaned_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)


# Load the survey data from a CSV file
filename = Path(__file__).parent / "week3_survey_messy.csv"
cleaned_filename = Path(__file__).parent / "week3_survey_cleaned.csv"
rows = []
fieldnames = []

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames or []
    for row in reader:
        rows.append(row)

# Count responses by role
# Normalize role names so "ux researcher" and "UX Researcher" are counted together
role_counts = {}

for row in rows:
    role = row["role"].strip().title()
    if role in role_counts:
        role_counts[role] += 1
    else:
        role_counts[role] = 1

print("Responses by role:")
for role, count in sorted(role_counts.items()):
    print(f"  {role}: {count}")

# Calculate the average years of experience
avg_experience = calculate_average_experience(rows)
if avg_experience is not None:
    print(f"\nAverage years of experience: {avg_experience:.1f}")
else:
    print("\nAverage years of experience: n/a")

# Find the top 5 highest satisfaction scores
# This was to find the actual scores and sorting them in descending order 
scored_rows = []
for row in rows:
    if row["satisfaction_score"].strip():
        scored_rows.append((row["participant_name"], int(row["satisfaction_score"])))

# Fixed error: top-5 logic previously sorted ascending, which returned lowest scores.
scored_rows.sort(key=lambda x: x[1], reverse=True)
top5 = scored_rows[:5]

print("\nTop 5 satisfaction scores:")
for name, score in top5:
    print(f"  {name}: {score}")

write_cleaned_rows(rows, fieldnames, cleaned_filename)
print(f"\nCleaned survey data written to: {cleaned_filename.name}")
