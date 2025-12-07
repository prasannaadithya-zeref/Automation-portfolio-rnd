/*
=============================================================================
LEARNING GUIDE: PostgreSQL - Advanced Features
=============================================================================
Postgres is famous for its JSONB support and Window Functions.

SECTION 1: WINDOW FUNCTIONS
---------------------------
Scenario: Rank employees by salary WITHIN their department.
*/

CREATE TABLE employees_pg (
    id SERIAL PRIMARY KEY,
    name TEXT,
    dept TEXT,
    salary INT
);

INSERT INTO employees_pg (name, dept, salary) VALUES
('Alice', 'Sales', 5000),
('Bob', 'Sales', 4500),
('Charlie', 'Sales', 6000),
('David', 'IT', 7000),
('Eve', 'IT', 7200);

-- Query: Show Rank
SELECT name, dept, salary,
       RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rank
FROM employees_pg;
-- Result: Charlie (1), Alice (2), Bob (3) in Sales.

/*
SECTION 2: JSONB (NoSQL in SQL)
-------------------------------
Postgres allows storing JSON documents that you can query efficiently.
*/

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    details JSONB
);

INSERT INTO products (details) VALUES 
('{"color": "red", "tags": ["sale", "summer"]}'),
('{"color": "blue", "tags": ["winter"]}');

-- Query 1: Find all Red products
-- "->" gets object, "->>" gets text
SELECT * FROM products 
WHERE details->>'color' = 'red';

-- Query 2: Find products with "sale" tag (Using contains operator @>)
SELECT * FROM products 
WHERE details @> '{"tags": ["sale"]}';

/*
SECTION 3: COMMON TABLE EXPRESSIONS (CTE)
-----------------------------------------
Cleaner way to write complex subqueries.
*/

WITH DeptSalaries AS (
    SELECT dept, AVG(salary) as avg_sal
    FROM employees_pg
    GROUP BY dept
)
SELECT e.name, e.salary, d.avg_sal
FROM employees_pg e
JOIN DeptSalaries d ON e.dept = d.dept
WHERE e.salary > d.avg_sal; -- Employees earning more than average
