-- POSTGRES MASTERCLASS: BASICS TO EXPERT
-- Covers: Select, Case, Coalesce, PL/pgSQL Loops, Ranking, Padding

/*
=============================================================================
SECTION 1: HANDLING NULLS (COALESCE)
=============================================================================
Postgres does NOT use NVL. We use COALESCE.
*/
SELECT 
    name,
    -- COALESCE: Returns first non-null value and checks data types strictly
    COALESCE(email, phone, 'No Contact Info') as primary_contact
FROM users;

/*
=============================================================================
SECTION 2: CONDITIONAL LOGIC (CASE)
=============================================================================
*/
SELECT title, price,
    CASE 
        WHEN price > 100 THEN 'Premium'
        ELSE 'Regular'
    END as type
FROM products;

/*
=============================================================================
SECTION 3: STRING MANIPULATION (LPAD, RPAD)
=============================================================================
*/
SELECT 
    product_code,
    -- Pad with zeros: 123 -> 00123
    LPAD(product_code::text, 5, '0') as standard_code
FROM products;

/*
=============================================================================
SECTION 4: WINDOW FUNCTIONS (RANK, DENSE_RANK, ROW_NUMBER)
=============================================================================
*/
SELECT name, category, score,
    RANK() OVER (PARTITION BY category ORDER BY score DESC) as rnk,
    DENSE_RANK() OVER (PARTITION BY category ORDER BY score DESC) as dense,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY score DESC) as row_num
FROM scores;

/*
=============================================================================
SECTION 5: PL/pgSQL LOOPS (DO Block)
=============================================================================
Postgres uses 'DO $$ ... $$' for anonymous blocks.
*/
DO $$
DECLARE 
    counter INT := 1;
BEGIN
    -- WHILE LOOP
    WHILE counter <= 5 LOOP
        RAISE NOTICE 'Counter: %', counter;
        counter := counter + 1;
    END LOOP;
    
    -- FOR LOOP through query results
    -- FOR r IN SELECT * FROM products LOOP
    --    RAISE NOTICE 'Product: %', r.name;
    -- END LOOP;
END $$;
