-- ORACLE MASTERCLASS: BASICS TO EXPERT
-- Covers: Select, Case, NVL, Loops, Ranking, Padding

/*
=============================================================================
SECTION 1: HANDLING NULLS (NVL vs COALESCE)
=============================================================================
*/
SELECT 
    name,
    salary,
    commission_pct,
    -- NVL: If commission is null, return 0. (Oracle Specific)
    NVL(commission_pct, 0) as comm_fixed,
    -- COALESCE: Returns first non-null value. (ANSI Standard)
    COALESCE(commission_pct, bonus, 0) as total_earnings
FROM employees;

/*
=============================================================================
SECTION 2: CONDITIONAL LOGIC (CASE, DECODE)
=============================================================================
*/
SELECT name, job_id,
    -- CASE: The standard "If-Then-Else" in SQL
    CASE 
        WHEN salary > 10000 THEN 'High Earner'
        WHEN salary BETWEEN 5000 AND 10000 THEN 'Mid Earner'
        ELSE 'Junior'
    END as salary_band,
    
    -- DECODE: Old Oracle specific syntax (like Switch-Case)
    DECODE(job_id, 'IT_PROG', 'Programmer', 'SA_REP', 'Sales', 'Other') as job_desc
FROM employees;

/*
=============================================================================
SECTION 3: STRING MANIPULATION (LPAD, RPAD)
=============================================================================
Useful for report formatting or generating codes.
*/
SELECT 
    name,
    -- LPAD: Pad left side with '*' until length is 10
    LPAD(salary, 10, '*') as protective_salary, -- Result: *****24000
    -- RPAD: Pad right side
    RPAD(name, 20, '.') as report_name
FROM employees;

/*
=============================================================================
SECTION 4: RANKING FUNCTIONS (Window Functions)
=============================================================================
Scenario: Top 3 Earners PER department.
*/
SELECT name, dept_id, salary,
    -- RANK: Skips numbers if tie (1, 1, 3)
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rnk,
    -- DENSE_RANK: No skipping (1, 1, 2)
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as dense_rnk
FROM employees;

/*
=============================================================================
SECTION 5: PL/SQL LOOPS & PROCEDURES
=============================================================================
*/
SET SERVEROUTPUT ON;

DECLARE
    v_counter NUMBER := 1;
BEGIN
    -- BASIC LOOP
    LOOP
        DBMS_OUTPUT.PUT_LINE('Loop Iteration: ' || v_counter);
        v_counter := v_counter + 1;
        EXIT WHEN v_counter > 3;
    END LOOP;
    
    -- FOR LOOP
    FOR i IN 1..5 LOOP
         DBMS_OUTPUT.PUT_LINE('For Loop: ' || i);
    END LOOP;
END;
/
