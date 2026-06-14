# Source System Design

## Business Context

A global pharmaceutical company is migrating patent records from a legacy IP management system into a modern enterprise platform.

The migration objective is not only to move data, but to standardize business rules and improve data trust.

---

## Source System

### Patent Table

| Column          | Description            |
| --------------- | ---------------------- |
| patent_id       | Patent identifier      |
| patent_title    | Patent title           |
| patent_status   | Raw patent status      |
| country_code    | Filing country         |
| inventor_name   | Inventor name          |
| filing_date     | Patent filing date     |
| expiration_date | Patent expiration date |

---

## Known Data Quality Issues

### Status Standardization

The legacy system contains multiple definitions for the same business meaning:

* Active
* ACTIVE
* A
* Expired
* EXP

---

### Country Standardization

The legacy system contains inconsistent country formats:

* JP
* JPN
* Japan
* US
* USA

---

### Missing Values

Some records contain:

* NULL inventor names
* Empty inventor names
* Unknown inventor names

---

### Duplicate Records

Duplicate patent identifiers exist due to historical data consolidation issues.

---

## Migration Goal

Standardize business definitions, remove inconsistencies, validate migration quality, and provide trusted reporting outputs.