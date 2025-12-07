/*
=============================================================================
LEARNING GUIDE: MongoDB - Aggregations & Queries
=============================================================================
Mongo is a Document DB. We don't use SQL; we use JSON-like queries.
This file is a Javascript/Shell script.

SECTION 1: CRUD Operations
--------------------------
*/

// 1. Insert
db.users.insertOne({
    "name": "Prasanna",
    "role": "Engineer",
    "skills": ["Python", "Mongo"],
    "address": { "city": "Bangalore", "zip": "560001" }
});

// 2. Find (Select equivalent)
// Find users where role is Engineer AND has "Python" skill
db.users.find({
    "role": "Engineer",
    "skills": "Python"
});

// 3. Update
db.users.updateOne(
    { "name": "Prasanna" },
    { "$set": { "active": true } } // Atomic operator
);

/*
SECTION 2: AGGREGATION PIPELINE (The "Group By" of Mongo)
---------------------------------------------------------
Scenario: Count users by City.
SQL equivalent: SELECT city, count(*) FROM users GROUP BY city
*/

db.users.aggregate([
    // Stage 1: Filter (WHERE)
    { "$match": { "active": true } },

    // Stage 2: Group (GROUP BY)
    {
        "$group": {
            "_id": "$address.city",   // Group by nested field
            "total_users": { "$sum": 1 }
        }
    },

    // Stage 3: Project (SELECT)
    {
        "$project": {
            "city": "$_id",
            "count": "$total_users",
            "_id": 0
        }
    }
]);

/*
SECTION 3: USEFUL OPERATORS
---------------------------
$in, $gt (greater than), $exists
*/

db.orders.find({
    "amount": { "$gt": 500 },
    "status": { "$in": ["shipped", "delivered"] }
});
