-- =========================================
-- Enterprise Data Migration Transformation
-- =========================================

SELECT

    patent_id,

    patent_title,

    CASE

        WHEN patent_status IN (
            'Active',
            'ACTIVE',
            'A'
        )
        THEN 'OPEN'

        WHEN patent_status IN (
            'Expired',
            'EXP'
        )
        THEN 'CLOSED'

        ELSE 'REVIEW'

    END AS standardized_status,

    CASE

        WHEN country_code IN (
            'JP',
            'JPN',
            'Japan'
        )
        THEN 'Japan'

        WHEN country_code IN (
            'US',
            'USA'
        )
        THEN 'United States'

        ELSE 'REVIEW'

    END AS standardized_country,

    inventor_name,

    filing_date,

    expiration_date

FROM patent_source;