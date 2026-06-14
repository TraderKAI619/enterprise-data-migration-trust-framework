import csv
import random
from datetime import datetime, timedelta

# Reproducible results
random.seed(42)

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

# Intentionally inconsistent legacy values
STATUSES = [
    "Active",
    "ACTIVE",
    "A",
    "Expired",
    "EXP"
]

COUNTRIES = [
    "JP",
    "JPN",
    "Japan",
    "US",
    "USA"
]


def random_filing_date():
    start = datetime(2018, 1, 1)
    end = datetime(2024, 12, 31)

    days = (end - start).days

    return start + timedelta(days=random.randint(0, days))


records = []

# Generate base dataset
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

    # Missing inventor (~4%)
    if random.random() < 0.04:
        record["inventor_name"] = ""

    # Unknown inventor (~2%)
    elif random.random() < 0.02:
        record["inventor_name"] = "Unknown"

    records.append(record)


# Inject duplicate records
for _ in range(120):

    source_record = random.choice(records)

    duplicate_record = source_record.copy()

    records.append(duplicate_record)


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

print("=" * 50)
print("Synthetic Patent Dataset Generated")
print("=" * 50)
print(f"Total Records: {len(records)}")
print("Expected Characteristics:")
print("- Duplicate Records: ~120")
print("- Missing Inventors: ~40")
print("- Unknown Inventors: ~20")
print("- Status Variations: Active / ACTIVE / A / Expired / EXP")
print("- Country Variations: JP / JPN / Japan / US / USA")
print(f"Output File: {OUTPUT_FILE}")
print("=" * 50)