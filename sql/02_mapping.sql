-- ====================================
-- Status Mapping Analysis
-- ====================================

SELECT
    patent_status AS source_status,

    CASE
        WHEN patent_status IN ('Active','ACTIVE','A')
        THEN 'OPEN'

        WHEN patent_status IN ('Expired','EXP')
        THEN 'CLOSED'

        ELSE 'REVIEW'
    END AS target_status,

    COUNT(*) AS record_count

FROM patent_source

GROUP BY
    patent_status

ORDER BY
    record_count DESC;


-- ====================================
-- Country Mapping Analysis
-- ====================================

SELECT
    country_code AS source_country,

    CASE
        WHEN country_code IN ('JP','JPN','Japan')
        THEN 'Japan'

        WHEN country_code IN ('US','USA')
        THEN 'United States'

        ELSE 'REVIEW'
    END AS target_country,

    COUNT(*) AS record_count

FROM patent_source

GROUP BY
    country_code

ORDER BY
    record_count DESC;


-- ====================================
-- Records Requiring Manual Review
-- ====================================

SELECT
    patent_id,
    inventor_name

FROM patent_source

WHERE inventor_name IS NULL
   OR inventor_name = ''
   OR inventor_name = 'Unknown';