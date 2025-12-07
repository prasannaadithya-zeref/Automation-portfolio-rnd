"""
DATA ENGINEERING LEVEL 3 & 4: ADVANCED VALIDATION MASTERY
=========================================================
Topics: Custom Validation Frameworks, Rule Engines, Performance.

[THEORY]
1. Row-wise/Column-wise Validation: Checking logic across columns.
2. Rule Engines: Storing rules in JSON/DB instead of hardcoding.
3. Chunking: Processing 5GB files on a 1GB RAM machine.
4. Reconciliation: Comparing Source (DB) vs Target (File).
"""

import pandas as pd
import numpy as np

# --- 1. Rule Engine Pattern (Mastery) ---
def validate_with_rules(df, rules_config):
    """
    Dynamic Validator.
    :param rules_config: Dict of rules e.g. {"col_name": "min_value"}
    """
    print("\n--- RULE ENGINE EXECUTION ---")
    results = {}
    
    for col, criteria in rules_config.items():
        if "min" in criteria:
            min_val = criteria["min"]
            # Vectorized check (Advanced Performance)
            failures = df[df[col] < min_val]
            
            if not failures.empty:
                results[col] = f"FAILED: {len(failures)} rows < {min_val}"
            else:
                results[col] = "PASS"
                
    return results

# --- 2. Advanced Reconciliation (Source vs Target) ---
def reconciliation_engine():
    print("\n--- RECONCILIATION ENGINE ---")
    source = pd.DataFrame({"id": [1, 2], "amount": [100, 200]})
    target = pd.DataFrame({"id": [1, 2], "amount": [100, 199]}) # ID 2 mismatch
    
    # Merge with indicator
    comp = pd.merge(source, target, on="id", suffixes=('_src', '_tgt'), indicator=True)
    
    # Find Mismatches
    mismatches = comp[comp["amount_src"] != comp["amount_tgt"]]
    print("Mismatched Rows:")
    print(mismatches[["id", "amount_src", "amount_tgt"]])

# --- 3. Chunk Processing (Big Data Optimization) ---
def chunk_process_demo():
    print("\n--- CHUNK PROCESSING ---")
    # Simulate a large file by chunking a DataFrame manually
    df_huge = pd.DataFrame({"obj": range(100)}) # Imagine 100 Million rows
    
    chunk_size = 33
    total = 0
    
    # In real life: pd.read_csv(..., chunksize=1000)
    for i in range(0, len(df_huge), chunk_size):
        chunk = df_huge.iloc[i:i+chunk_size]
        # Process small piece
        total += chunk["obj"].sum()
        print(f"Processed chunk {i}-{i+chunk_size}")
        
    print(f"Total Sum: {total}")

if __name__ == "__main__":
    # Test Data
    data = {"age": [25, 17, 30], "salary": [50000, 0, 80000]}
    df = pd.DataFrame(data)
    
    # Define Rules Dynamically
    rules = {
        "age": {"min": 18},
        "salary": {"min": 1000}
    }
    
    report = validate_with_rules(df, rules)
    print("Validation Report:", json.dumps(report, indent=2))
    
    reconciliation_engine()
    chunk_process_demo()
