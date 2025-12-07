# 📊 ETL Testing Mastery: What Actually Matters?
*ETL = Extract, Transform, Load. It's about moving Data.*

## What are we testing?
We compare **Source** (Raw File/DB) vs **Target** (Data Warehouse).

## 1. The Big 4 Validations
1.  **Count Validation** (Completeness)
    *   Source has 1000 rows. Target MUST have 1000 rows.
    *   *SQL*: `SELECT COUNT(*) FROM source` vs `SELECT COUNT(*) FROM target`.

2.  **Data Correctness** (Transformation Logic)
    *   Rule: "Convert Names to Uppercase".
    *   Source: "john". Target must be "JOHN".
    *   *Bug*: Target is "John" (Mixed case).

3.  **Constraint Checks** (Integrity)
    *   Primary Keys: No duplicates in Target.
    *   Foreign Keys: No orphans.
    *   Nulls: Critical columns cannot be NULL.

4.  **Duplicate Check**
    *   Did the ETL job run twice and double the data?
    *   *SQL*: `SELECT id, COUNT(*) FROM target GROUP BY id HAVING COUNT(*) > 1`.

## 2. Testing Strategies
*   **Minus Query**:
    *   `(SELECT * FROM source) MINUS (SELECT * FROM target)` should be 0.
*   **Sample Testing**:
    *   Pick 1 random row. Check all 50 columns manually.
