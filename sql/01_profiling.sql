-- =========================================
-- Data Profiling
-- Enterprise Migration Assessment
-- =========================================

-- Total Records

SELECT
    COUNT(*) AS total_records
FROM patent_source;


-- Status Distribution

SELECT
    patent_status,
    COUNT(*) AS record_count
FROM patent_source
GROUP BY patent_status
ORDER BY record_count DESC;


-- Country Distribution

SELECT
    country_code,
    COUNT(*) AS record_count
FROM patent_source
GROUP BY country_code
ORDER BY record_count DESC;


-- Duplicate Patent IDs

SELECT
    patent_id,
    COUNT(*) AS duplicate_count
FROM patent_source
GROUP BY patent_id
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;


-- Missing Inventor Names

SELECT
    COUNT(*) AS missing_inventor_count
FROM patent_source
WHERE inventor_name IS NULL
   OR inventor_name = '';


-- Unknown Inventors

SELECT
    COUNT(*) AS unknown_inventor_count
FROM patent_source
WHERE inventor_name = 'Unknown';