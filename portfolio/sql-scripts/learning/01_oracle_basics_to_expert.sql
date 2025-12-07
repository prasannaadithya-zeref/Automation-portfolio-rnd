/*
=============================================================================
LEARNING GUIDE: Oracle SQL - From Basics to Expert
=============================================================================
This file is a self-paced tutorial. Copy-paste these queries into your SQL Editor.

SECTION 1: THE BASICS (DDL & DML)
---------------------------------
Concepts: Data Types, Creating Tables, Inserting Data.
*/

-- 1. Create a Table (DDL)
-- NUMBER(5) means up to 5 digits. VARCHAR2 is Oracle's String.
CREATE TABLE employees_demo (
    emp_id NUMBER(5) PRIMARY KEY,
    name VARCHAR2(50),
    role VARCHAR2(30),
    salary NUMBER(10, 2), -- 10 digits total, 2 decimals
    join_date DATE
);

-- 2. Insert Data (DML)
INSERT INTO employees_demo VALUES (101, 'Alice', 'Engineer', 75000.00, SYSDATE);
INSERT INTO employees_demo VALUES (102, 'Bob', 'Manager', 95000.00, TO_DATE('2023-01-15', 'YYYY-MM-DD'));
COMMIT; -- Essential in Oracle to save changes!

/*
SECTION 2: INTERMEDIATE QUERIES
-------------------------------
Concepts: Filtering, Aggregation, Case Statements.
*/

-- 1. The CASE Statement (Logic in SQL)
-- "If salary > 80k then High, else Normal"
SELECT name, salary,
    CASE 
        WHEN salary > 80000 THEN 'High Earner'
        ELSE 'Standard Band'
    END as salary_band
FROM employees_demo;

-- 2. DECODE (Oracle specific shortcut for IF-ELSE equality)
SELECT name, DECODE(role, 'Manager', 'Key Personnel', 'Staff') as status
FROM employees_demo;

/*
SECTION 3: ADVANCED (PL/SQL)
----------------------------
Concepts: Variables, Cursors, Stored Procedures.
Only run this in a PL/SQL block.
*/

SET SERVEROUTPUT ON; -- Enable printing output

DECLARE
    -- Variable Declaration
    v_name employees_demo.name%TYPE; -- specific type matching the table column
    v_sal  NUMBER;
    
    -- Cursor: A pointer to a result set (like a row iterator)
    CURSOR c_emps IS SELECT name, salary FROM employees_demo;
BEGIN
    OPEN c_emps;
    LOOP
        FETCH c_emps INTO v_name, v_sal;
        EXIT WHEN c_emps%NOTFOUND; -- Break loop when no more rows
        
        -- Logic inside the loop
        DBMS_OUTPUT.PUT_LINE('Employee: ' || v_name || ' earns ' || v_sal);
    END LOOP;
    CLOSE c_emps;
END;
/

/*
SECTION 4: FUNCTIONS & PROCEDURES (Reusable Logic)
--------------------------------------------------
Concepts: IN/OUT Parameters, Return Values.
*/

-- 1. Create a Function (Returns a value)
CREATE OR REPLACE FUNCTION calculate_bonus(salary IN NUMBER) 
RETURN NUMBER 
IS
BEGIN
    RETURN salary * 0.10; -- 10% bonus
END;
/

-- 2. Create a Procedure (Action oriented)
CREATE OR REPLACE PROCEDURE promote_employee(p_emp_id IN NUMBER) 
IS
BEGIN
    UPDATE employees_demo 
    SET role = 'Senior ' || role, salary = salary + 5000
    WHERE emp_id = p_emp_id;
    COMMIT;
END;
/

/*
SECTION 5: ADVANCED LOOPING
---------------------------
Concepts: FOR Loop, WHILE Loop.
*/

BEGIN
    -- FOR Loop (Fixed range)
    FOR i IN 1..5 LOOP
        DBMS_OUTPUT.PUT_LINE('Iteration: ' || i);
    END LOOP;

    -- WHILE Loop (Condition based)
    DECLARE
        counter NUMBER := 10;
    BEGIN
        WHILE counter < 15 LOOP
            DBMS_OUTPUT.PUT_LINE('Counter: ' || counter);
            counter := counter + 1;
        END LOOP;
    END;
END;
/

