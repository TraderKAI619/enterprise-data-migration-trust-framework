import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = "data/raw/patent_source.csv"

PATENT_TITLES = [
    "AI Drug Discovery Platform",
    "Medical Imaging Algorithm",
    "Gene Analysis System",
    "Smart Manufacturing Process",
    "Clinical Data Framework",
    "Biotech Research Engine",
    "Healthcare Analytics Platform"
]

INVENTORS = [
    "John Smith",
    "Michael Chen",
    "Yuki Tanaka",
    "Sarah Johnson",
    "David Wilson",
    "Emily Brown",
    "Kenji Sato"
]

STATUSES = [
    "Active",
    "Expired"
]

COUNTRIES = [
    "JP",
    "US"
]


def random_filing_date():
    start = datetime(2018, 1, 1)
    end = datetime(2024, 12, 31)

    days = (end - start).days

    return start + timedelta(days=random.randint(0, days))


records = []

for i in range(1, 1001):

    filing_date = random_filing_date()
    expiration_date = filing_date.replace(
        year=filing_date.year + 20
    )

    record = {
        "patent_id": f"P{i:06d}",
        "patent_title": random.choice(PATENT_TITLES),
        "patent_status": random.choice(STATUSES),
        "country_code": random.choice(COUNTRIES),
        "inventor_name": random.choice(INVENTORS),
        "filing_date": filing_date.date(),
        "expiration_date": expiration_date.date()
    }

    records.append(record)


with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=records[0].keys()
    )

    writer.writeheader()
    writer.writerows(records)

print(f"Generated {len(records)} records")
print(f"Output: {OUTPUT_FILE}")