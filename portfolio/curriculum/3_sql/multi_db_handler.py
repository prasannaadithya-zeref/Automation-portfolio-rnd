"""
MULTI-DATABASE HANDLER
======================
Demonstrates how to handle Oracle, Postgres, Redshift, and Mongo
in a single unified way.

Key Concepts:
1. Input Difference: Connection Strings (URI)
2. Query Separation: Reading from 'queries.yaml'
"""

import os
import yaml
import sys
# Mocking libraries so you can run this file immediately
# In real life: import psycopg2, cx_Oracle, pymongo

class DatabaseHandler:
    def __init__(self, env_file=".env", query_file="queries.yaml"):
        # Load Queries
        with open(query_file, 'r') as f:
            self.queries = yaml.safe_load(f)
        
        # Simulating loading .env
        self.config = {
            "POSTGRES_HOST": "localhost",
            "MONGO_URI": "mongodb://localhost:27017"
        }
        print(f"[INIT] Loaded Queries: {list(self.queries.keys())}")

    def get_query(self, db_type, query_name):
        """Fetches the raw SQL/JSON from yaml."""
        return self.queries.get(db_type, {}).get(query_name)

    def execute_sql(self, db_type, query_name):
        """Simulates execution for SQL DBs."""
        sql = self.get_query(db_type, query_name)
        
        if db_type == 'postgres':
            # conn = psycopg2.connect(...)
            print(f"[POSTGRES] Connecting to {self.config['POSTGRES_HOST']}...")
            print(f"[POSTGRES] Executing: {sql}")
        
        elif db_type == 'oracle':
            # dsn = cx_Oracle.makedsn(...)
            print(f"[ORACLE] Connecting via TNS Service...")
            print(f"[ORACLE] Executing: {sql}")
            
        elif db_type == 'redshift':
            # Redshift uses Postgres drivers usually
            print(f"[REDSHIFT] Connecting to AWS Cluster...")
            print(f"[REDSHIFT] Executing: {sql}")

    def execute_nosql(self, query_name):
        """Simulates execution for Mongo."""
        filter_json = self.get_query('mongo', query_name)
        
        # client = pymongo.MongoClient(self.config['MONGO_URI'])
        print(f"[MONGO] Connecting to URI: {self.config['MONGO_URI']}")
        print(f"[MONGO] db.collection.find({filter_json})")


if __name__ == "__main__":
    db = DatabaseHandler()
    
    print("\n--- 1. POSTGRES EXECUTION ---")
    db.execute_sql("postgres", "get_all_users")
    
    print("\n--- 2. ORACLE EXECUTION ---")
    db.execute_sql("oracle", "get_daily_report")
    
    print("\n--- 3. MONGO EXECUTION ---")
    db.execute_nosql("find_active_users")
