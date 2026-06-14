-- =========================================
-- Migration Validation Framework
-- =========================================

-- Record Count Validation

SELECT
    COUNT(*) AS source_record_count
FROM patent_source;


SELECT
    COUNT(*) AS target_record_count
FROM standardized_patent_data;


-- Status Validation

SELECT
    standardized_status,
    COUNT(*) AS record_count
FROM standardized_patent_data
GROUP BY standardized_status;


-- Country Validation

SELECT
    standardized_country,
    COUNT(*) AS record_count
FROM standardized_patent_data
GROUP BY standardized_country;


-- Duplicate Patent IDs

SELECT
    patent_id,
    COUNT(*) AS duplicate_count
FROM standardized_patent_data
GROUP BY patent_id
HAVING COUNT(*) > 1;


-- Records Requiring Manual Review

SELECT
    *
FROM standardized_patent_data
WHERE standardized_status = 'REVIEW'
   OR standardized_country = 'REVIEW'
   OR inventor_name IS NULL
   OR inventor_name = ''
   OR inventor_name = 'Unknown';