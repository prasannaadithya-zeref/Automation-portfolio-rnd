"""
DATA ENGINEERING LEVEL 1 & 2: PANDAS ESSENTIALS
=================================================
Topics: Reading, Cleaning, Joining, Aggregating.

[THEORY]
1. DataFrame: The excel-sheet equivalent in Python.
2. NaNs: How pandas represents missing data.
3. GroupBy: The pivot-table equivalent.
4. Joins: Merging datasources (SQL style).
"""

import pandas as pd
import numpy as np

def beginner_basics():
    print("\n--- BEGINNER: DATAFRAMES ---")
    data = {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", None], # None becomes NaN
        "sales": [500, 200, 300]
    }
    df = pd.read_json(json.dumps(data)) if False else pd.DataFrame(data) 
    
    print("1. Original Data:")
    print(df)
    
    # Filtering
    high_sales = df[df["sales"] > 250]
    print("\n2. High Sales (>250):")
    print(high_sales)

def intermediate_cleaning():
    print("\n--- INTERMEDIATE: CLEANING & JOINS ---")
    df = pd.DataFrame({
        "id": [1, 2],
        "val": [None, 50],
        "cat": ["A", "B"]
    })
    
    # 1. Null Handling
    # Fill NaN with 0
    df_clean = df.fillna(0)
    print("Cleaned Data (NaN -> 0):")
    print(df_clean)
    
    # 2. Joins
    other_df = pd.DataFrame({"id": [1, 2], "location": ["NY", "CA"]})
    merged = pd.merge(df_clean, other_df, on="id", how="inner")
    print("\nMerged Data:")
    print(merged)
    
    # 3. Aggregation (GroupBy)
    print("\nAggregation Mean:")
    print(merged.groupby("location")["val"].mean())

import json 
# Small hack for the 'read_json' comment above to be valid python if uncommented

if __name__ == "__main__":
    beginner_basics()
    intermediate_cleaning()
