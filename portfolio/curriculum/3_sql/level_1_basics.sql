-- SQL LEVEL 1: BEGINNER (Foundations)
-- Topic: The Holy Trinity (SELECT, WHERE, JOIN)

-- 1. Retrieving Data
SELECT first_name, last_name 
FROM employees
WHERE salary > 50000;

-- 2. Aggregating Data (Grouping)
-- Scenario: "How many employees in each department?"
SELECT department_id, COUNT(*) as emp_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5; -- Filter groups, not rows!

-- 3. JOINING Tables (Crucial!)
-- Scenario: Get Employee Name AND Department Name
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;
-- INNER JOIN: Only matching rows.
-- LEFT JOIN: All employees, even if they have no department.

-- [HANDS ON TASK]
-- Write a query to find the Average Salary per Department, 
-- but only for departments starting with 'IT'.
