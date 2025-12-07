"""
PYTHON LEVEL 3: ADVANCED
========================
Topic: High Performance & Professional Python.

[THEORY]
1. Decorators: Modifying functions dynamically (Logging, Timing).
2. Generators: Memory efficient iteration (yield).
3. Threading: Running tasks in parallel.
4. Regex: Advanced pattern matching.
5. Context Managers: Custom 'with' statements.
"""

import time
import threading
import re
from contextlib import contextmanager

# --- 1. Decorators ---
def test_step_logger(func):
    """Decorator to log start and end of a test step."""
    def wrapper(*args, **kwargs):
        print(f"\n[STEP START] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[STEP END] {func.__name__}")
        return result
    return wrapper

@test_step_logger
def click_button(btn_name):
    print(f"Clicking {btn_name}...")
    time.sleep(0.5)

# --- 2. Generators (Yield) ---
def large_file_reader(lines):
    """Simulates reading separate chunks without loading all to RAM."""
    for i in range(lines):
        yield f"Row_Data_{i}"

# --- 3. Multithreading ---
def api_call_simulator(thread_name):
    print(f"[{thread_name}] Fetching data...")
    time.sleep(1)
    print(f"[{thread_name}] Done.")

def run_threads():
    t1 = threading.Thread(target=api_call_simulator, args=("Thread-1",))
    t2 = threading.Thread(target=api_call_simulator, args=("Thread-2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# --- 4. Regex (Regular Expressions) ---
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        print(f"Valid Email: {email}")
    else:
        print(f"Invalid Email: {email}")

# --- PRACTICE TASK ---
# Task: Write a decorator @retry that attempts a function 3 times if it fails.
def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                print("Retrying...")
        raise Exception("Failed after 3 retries")
    return wrapper

if __name__ == "__main__":
    click_button("Submit")
    
    print("\n[Generator Output]")
    for row in large_file_reader(3):
        print(row)
        
    print("\n[Threading]")
    run_threads()
    
    print("\n[Regex]")
    validate_email("test.user@company.com")
