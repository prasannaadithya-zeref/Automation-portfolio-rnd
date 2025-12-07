"""
PYTHON LEVEL 2: INTERMEDIATE
============================
Topic: Building Real Applications.

[THEORY]
1. OOP: Modeling real-world objects (Encapsulation, Inheritance).
2. File I/O: Reading/Writing logs and configs.
3. Exceptions: Handling crashes gracefully.
4. Lambdas: One-line functions.
5. Modules: Organizing code into files.
"""

import os
import json

# --- 1. OOP (Classes & Inheritance) ---
class BrowserDriver:
    def __init__(self, browser_name):
        self.browser = browser_name
        self._session_id = None # Encapsulation (Protected)

    def open(self):
        print(f"Opening {self.browser}...")
        self._session_id = 12345

    def close(self):
        print("Closing browser.")

# Inheritance
class MobileDriver(BrowserDriver):
    def get_orientation(self):
        return "Portrait"

# --- 2. File Handling & Context Managers ---
def file_operations_demo():
    filename = "test_log.txt"
    # Write
    with open(filename, "w") as f:
        f.write("Test started.\nTest finished.")
    
    # Read
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()
            print(f"\n[File Content]:\n{content}")

# --- 3. Exception Handling ---
def risky_operation():
    try:
        data = {"key": "val"}
        print(data["missing_key"]) # This fails
    except KeyError as e:
        print(f"\n[Handled Error]: Key not found -> {e}")
    finally:
        print("Cleanup operations always run.")

# --- 4. Lambdas & Comprehensions ---
def advanced_transformation():
    nums = [1, 2, 3, 4]
    # List Comprehension (Pythonic way to loop)
    squares = [x*x for x in nums] 
    
    # Lambda (Anonymous function)
    is_even = lambda x: x % 2 == 0
    evens = list(filter(is_even, nums))
    
    print(f"\n[Comprehension]: {squares}")
    print(f"[Lambda Filter]: {evens}")

# --- PRACTICE TASK ---
# Task: Create a class 'ConfigLoader' that reads a JSON file in __init__
# and has a method get_value(key). Handle FileNotFoundError.

class ConfigLoaderPractice:
    def __init__(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
            print("Config file missing!")

    def get_value(self, key):
        return self.data.get(key, None)

if __name__ == "__main__":
    driver = MobileDriver("Chrome")
    driver.open()
    
    file_operations_demo()
    risky_operation()
    advanced_transformation()
