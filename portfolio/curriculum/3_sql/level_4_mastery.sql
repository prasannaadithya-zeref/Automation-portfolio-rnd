-- SQL LEVEL 4: MASTERY (Performance & Tuning)
-- Topic: Why is my query slow? (Indexes & Plans)

-- 1. INDEXING
-- Analogy: Index is like the "Table of Contents" in a book.
-- Without it, SQL does a "Full Table Scan" (Reads every page).

CREATE INDEX idx_emp_salary ON employees(salary);
-- Now, queries filtering by 'salary' are instant.

-- 2. EXPLAIN PLAN (The Debugger)
-- Run this before the query to see how DB executes it.
EXPLAIN ANALYZE 
SELECT * FROM employees WHERE salary > 100000;

-- Look for:
-- "Seq Scan": Bad (Scanning everything).
-- "Index Scan": Good (Jumping to data).

-- 3. PARTITIONING (Big Data)
-- Splitting a 1 Billion row table into month-based chunks.
CREATE TABLE sales_2023 PARTITION OF sales
FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');

-- [HANDS ON TASK]
-- You have a slow query joining 3 tables. 
-- What is the first thing you check? (Hint: See if the ON columns have Indexes).
