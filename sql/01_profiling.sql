-- Data Profiling
-- Duplicate Analysis
-- Null Analysis
-- Status Distribution
-- Country Distribution
-- Total Records

SELECT COUNT(*) AS total_records
FROM patent_source;

-- Status Distribution

SELECT
    patent_status,
    COUNT(*) AS record_count
FROM patent_source
GROUP BY patent_status;

-- Country Distribution

SELECT
    country_code,
    COUNT(*) AS record_count
FROM patent_source
GROUP BY country_code;

-- Duplicate Patent IDs

SELECT
    patent_id,
    COUNT(*) AS duplicate_count
FROM patent_source
GROUP BY patent_id
HAVING COUNT(*) > 1;

-- Missing Inventors

SELECT COUNT(*)
FROM patent_source
WHERE inventor_name IS NULL;