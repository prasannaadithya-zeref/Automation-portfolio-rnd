"""
LEARNING LAB: Python No Limits - Advanced Features
==================================================
To truly claim "Expert" status, you must understand the internals.
1. Decorators (Modifying functions dynamically)
2. Generators (Memory efficient loops)
3. Magic Methods (Dunders)
4. Context Managers
"""

import time
from contextlib import contextmanager

print("--- [1] DECORATORS ---")
# Concept: A function that takes a function and returns a wrapper.
# Use Case: Timing, Logging, Auth checks.

def performance_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] executed in {end - start:.5f} sec")
        return result
    return wrapper

@performance_timer
def slow_log_parser(lines):
    print("Parsing logs...")
    time.sleep(0.5) # Simulate work
    return len(lines)

# Run it
slow_log_parser(["Error 1", "Error 2"])


print("\n--- [2] GENERATORS ---")
# Concept: Return one item at a time using 'yield'. 
# Diff vs List: Lists store all in RAM. Generators compute on fly.
# Use Case: Reading 100GB log files.

def log_reader_generator(total_lines):
    for i in range(total_lines):
        yield f"Line {i}: Data content..."

# Processing 1M lines without memory crash
gen = log_reader_generator(5) # Valid for small demo
for line in gen:
    print(line)


print("\n--- [3] MAGIC METHODS (OOP Deep Dive) ---")
# Concept: Customize how objects behave with operators (+, -, str)

class ReportMetadata:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows
    
    def __str__(self):
        """Called by print()"""
        return f"Report({self.name}, rows={self.rows})"
    
    def __add__(self, other):
        """Called by + operator"""
        return ReportMetadata(f"{self.name} & {other.name}", self.rows + other.rows)

r1 = ReportMetadata("Daily", 100)
r2 = ReportMetadata("Weekly", 500)
print(f"Object String: {r1}")
r3 = r1 + r2 # Combining objects!
print(f"Combined: {r3}")


print("\n--- [4] CONTEXT MANAGERS ---")
# Concept: Managing resources (files, DB connections) automatically.
# The 'with' keyword uses __enter__ and __exit__.

class DBConnectionScope:
    def __enter__(self):
        print("[DB] Opening connection...")
        return "Connection_Obj"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[DB] Closing connection (Auto-cleanup)")

with DBConnectionScope() as conn:
    print(f"Executing query on {conn}")
