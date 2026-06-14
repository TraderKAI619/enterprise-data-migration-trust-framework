-- =========================================
-- Migration Trust Dashboard
-- =========================================

-- Migration Readiness

SELECT

    1120 AS total_records,

    62 AS manual_review_records,

    ROUND(
        (1120 - 62) * 100.0 / 1120,
        2
    ) AS migration_readiness_pct;


-- Data Quality Score

SELECT

    1120 AS total_records,

    120 AS duplicate_records,

    44 AS missing_inventors,

    18 AS unknown_inventors,

    ROUND(
        (
            1120
            - 120
            - 44
            - 18
        ) * 100.0 / 1120,
        2
    ) AS data_quality_score;


-- Trust Summary

SELECT

    'READY WITH REVIEW REQUIRED'
        AS migration_status;