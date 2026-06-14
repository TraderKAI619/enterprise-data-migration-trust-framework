import csv
from collections import Counter

INPUT_FILE = "data/raw/patent_source.csv"
OUTPUT_FILE = "reports/profiling_report.csv"

total_records = 0
patent_ids = []
missing_inventors = 0
unknown_inventors = 0
status_values = set()
country_values = set()

with open(INPUT_FILE, newline="", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:

        total_records += 1

        patent_ids.append(row["patent_id"])

        status_values.add(row["patent_status"])

        country_values.add(row["country_code"])

        inventor = row["inventor_name"].strip()

        if inventor == "":
            missing_inventors += 1

        if inventor == "Unknown":
            unknown_inventors += 1


duplicate_records = (
    total_records - len(set(patent_ids))
)

results = [
    ["metric", "result"],
    ["total_records", total_records],
    ["unique_patent_ids", len(set(patent_ids))],
    ["duplicate_records", duplicate_records],
    ["missing_inventors", missing_inventors],
    ["unknown_inventors", unknown_inventors],
    ["unique_status_values", len(status_values)],
    ["unique_country_values", len(country_values)]
]

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerows(results)

print("\n=== Profiling Report ===")

for row in results[1:]:
    print(f"{row[0]}: {row[1]}")

print(f"\nSaved to {OUTPUT_FILE}")