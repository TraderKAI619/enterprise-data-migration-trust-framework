import csv
import os

INPUT_FILE = "data/raw/patent_source.csv"
OUTPUT_FILE = "data/target/migrated_patent.csv"

os.makedirs(
    "data/target",
    exist_ok=True
)

STATUS_MAP = {
    "Active": "OPEN",
    "ACTIVE": "OPEN",
    "A": "OPEN",
    "Expired": "CLOSED",
    "EXP": "CLOSED"
}

COUNTRY_MAP = {
    "JP": "Japan",
    "JPN": "Japan",
    "Japan": "Japan",
    "US": "United States",
    "USA": "United States"
}

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    records = list(csv.DictReader(f))

seen = set()
deduped = []

for r in records:
    if r["patent_id"] not in seen:
        seen.add(r["patent_id"])
        deduped.append(r)

transformed = []

for r in deduped:

    transformed.append({
        "patent_id": r["patent_id"],
        "patent_title": r["patent_title"],
        "patent_status": STATUS_MAP.get(
            r["patent_status"],
            "REVIEW"
        ),
        "country": COUNTRY_MAP.get(
            r["country_code"],
            "REVIEW"
        ),
        "inventor_name": (
            r["inventor_name"]
            if r["inventor_name"] not in (
                "",
                "Unknown"
            )
            else "NOT PROVIDED"
        ),
        "filing_date": r["filing_date"],
        "expiration_date": r["expiration_date"]
    })

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=transformed[0].keys()
    )

    writer.writeheader()
    writer.writerows(transformed)

print(f"Source Records: {len(records)}")
print(f"Target Records: {len(transformed)}")

status_summary = {}

for r in transformed:

    status_summary[
        r["patent_status"]
    ] = (
        status_summary.get(
            r["patent_status"],
            0
        )
        + 1
    )

print()
print("Status Summary:")
print(status_summary)

print()
print(f"Output File: {OUTPUT_FILE}")