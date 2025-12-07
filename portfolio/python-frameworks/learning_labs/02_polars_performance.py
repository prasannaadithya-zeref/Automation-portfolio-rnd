"""
LEARNING LAB: High-Performance Data Validation with Polars
==========================================================
Pandas is great, but Polars is the future for large datasets (Rust-based).
This module compares Validation Logic using both libraries.

Key Concepts:
- Eager vs Lazy Execution (Polars)
- Performance on larger data
"""

import polars as pl
import pandas as pd
import time
import numpy as np

def generate_dummy_data(rows=100000):
    """Generates a larger dataset to show performance diff."""
    data = {
        "id": range(rows),
        "amount": np.random.rand(rows) * 1000,
        "category": np.random.choice(['A', 'B', 'C'], rows)
    }
    return data

def pandas_validation():
    print("\n[Pandas] Starting Validation...")
    start = time.time()
    
    # 1. Create DataFrame
    df = pd.DataFrame(generate_dummy_data())
    
    # 2. Filtering
    high_value = df[df['amount'] > 500]
    
    # 3. Aggregation
    result = high_value.groupby('category')['amount'].sum()
    
    print(f"[Pandas] Time taken: {time.time() - start:.4f} seconds")
    return result

def polars_validation():
    print("\n[Polars] Starting Validation (Lazy API)...")
    start = time.time()
    
    # 1. Create DataFrame (Polars can handle this much faster)
    data = generate_dummy_data()
    df = pl.DataFrame(data)
    
    # 2. Validation using Expressions (The Polars Way)
    # Lazy execution allows optimization before running
    q = (
        df.lazy()
        .filter(pl.col("amount") > 500)
        .group_by("category")
        .agg(pl.col("amount").sum())
    )
    
    result = q.collect() # Trigger execution
    
    print(f"[Polars] Time taken: {time.time() - start:.4f} seconds")
    return result

if __name__ == "__main__":
    print("--- Performance Check: Pandas vs Polars ---")
    pandas_validation()
    polars_validation()
    
    print("\n[Expert Tip] Use Polars when validating CSVs > 500MB.")
