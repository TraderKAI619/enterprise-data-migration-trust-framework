import csv

SOURCE_FILE = "data/raw/patent_source.csv"
TARGET_FILE = "data/target/migrated_patent.csv"

OUTPUT_FILE = "reports/reconciliation_report.csv"


with open(SOURCE_FILE, newline="", encoding="utf-8") as f:
    source_records = list(csv.DictReader(f))

with open(TARGET_FILE, newline="", encoding="utf-8") as f:
    target_records = list(csv.DictReader(f))


source_count = len(source_records)
target_count = len(target_records)

source_unique_ids = len(
    set(r["patent_id"] for r in source_records)
)

target_unique_ids = len(
    set(r["patent_id"] for r in target_records)
)

status_values = len(
    set(r["patent_status"] for r in target_records)
)

country_values = len(
    set(r["country"] for r in target_records)
)

results = [
    ["check_name", "result"],
    ["source_record_count", source_count],
    ["target_record_count", target_count],
    ["source_unique_patents", source_unique_ids],
    ["target_unique_patents", target_unique_ids],
    ["standardized_status_values", status_values],
    ["standardized_country_values", country_values]
]

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)
    writer.writerows(results)

print("\n=== Reconciliation Report ===")

for row in results[1:]:
    print(f"{row[0]}: {row[1]}")

print(f"\nSaved to {OUTPUT_FILE}")