# Value Mapping Sheet

## Patent Status Mapping

| Source Value | Target Value | Business Meaning |
|-------------|-------------|-------------|
| Active | OPEN | Active Patent |
| ACTIVE | OPEN | Active Patent |
| A | OPEN | Active Patent |
| Expired | CLOSED | Expired Patent |
| EXP | CLOSED | Expired Patent |

---

## Country Mapping

| Source Value | Target Value |
|-------------|-------------|
| JP | Japan |
| JPN | Japan |
| Japan | Japan |
| US | United States |
| USA | United States |

---

## Business Rules

Rule 1:
All active status definitions must be standardized to OPEN.

Rule 2:
All expired status definitions must be standardized to CLOSED.

Rule 3:
Country names must follow ISO-aligned business standards.

Rule 4:
Duplicate patent IDs require manual review before migration.