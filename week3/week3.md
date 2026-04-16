# Week 3 Competency Claim

## What it means
Loading messy real-world data with Python, finding what is broken, and fixing it so the script runs cleanly on any valid input. Reading error messages as diagnostic information. Writing scripts that produce consistent, repeatable output.

## Claim
This week I demonstrated that I can load messy CSV data in Python, use error messages to diagnose failures, and refactor the code so it runs reliably and produces consistent outputs.

## Evidence
- `week3/week3_survey_messy.csv`: messy, real-world-style input data (includes non-numeric text like `"fifteen"` in `experience_years`).
- `week3/week3_analysis_buggy.py`:
  - reads CSV data with `csv.DictReader`
  - fixes the crash caused by invalid numeric conversion by validating/parsing safely
  - computes consistent summary outputs (role counts, average experience, top satisfaction scores)
  - writes a repeatable cleaned output file: `week3/week3_survey_cleaned.csv`

## Reflection
The key lesson was that “messy data” is normal. Scripts should assume fields can be missing, formatted inconsistently, or contain unexpected text. The fastest way to improve reliability was to treat error messages (like `ValueError`) as clues, then add small, well-named helper functions so the same cleaning/parsing rules are applied consistently every run.
