-- File: validation_queries.sql
-- Description: Common SQL patterns used for Data Validation

-- 1. Check for duplicate primary keys
SELECT transaction_id, COUNT(*)
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- 2. Validate orphan records (Foreign Key Check)
SELECT count(*) 
FROM orders o 
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- 3. Recon: Compare total amount between source (staging) and target (prod) tables
SELECT 'Staging' as source, SUM(amount) as total_amt FROM staging_txns
UNION ALL
SELECT 'Prod' as source, SUM(amount) as total_amt FROM prod_txns;

-- 4. Data Type / Format Validation (Regex in PostgreSQL)
SELECT user_id, email
FROM users
WHERE email !~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$';
