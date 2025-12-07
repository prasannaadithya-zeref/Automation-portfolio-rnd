"""
LEARNING LAB: Python - From Scripts to Frameworks
=================================================
A guide for Automation Engineers to master Python.

SECTION 1: BASICS (The Foundation)
----------------------------------
Every script uses these. if you know this, skip to Section 2.
"""

def basic_concepts():
    print("--- [1] BASICS ---")
    
    # 1. Variables & Primitive Types
    name = "Prasanna"   # String
    experience = 5      # Integer
    is_active = True    # Boolean
    rating = 4.5        # Float

    # 2. Data Structures (The "Big 4")
    # LIST: Ordered, MUTABLE (Changeable)
    skills = ["Python", "SQL", "Testing"] 
    skills.append("AWS") # We can add to it

    # TUPLE: Ordered, IMMUTABLE (Read-Only)
    # Use for fixed configs (DB Connection tuples)
    db_config = ("localhost", 5432) 
    
    # SET: Unordered, UNIQUE values only
    # Excellent for finding duplicates
    ids = {101, 102, 101} # Result: {101, 102} (duplicate removed)

    # DICTIONARY: Key-Value Pairs
    user = {
        "id": 1,
        "role": "Admin",
        "access": ["read", "write"] # Nested List
    }

    # 3. Control Flow
    if experience > 3:
        print(f"{name} is Senior.")
    elif experience > 1:
        print(f"{name} is Junior.")
    else:
        print(f"{name} is Fresher.")
    
    # 4. Looping
    print("Skills:")
    for s in skills:
        print(f" - {s}")

    # While Loop
    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1
        
    # 5. Error Handling (Try-Except)
    # Define config for demo
    config = {"env": "QA", "timeout": 30}
    try:
        print(config["invalid_key"])
    except KeyError as e:
        print(f"Error caught: Missing config key {e}")

"""
SECTION 1.5: FUNCTIONS DEEP DIVE
--------------------------------
"""
def power_function(base, exponent=2): 
    """Function with Default Argument"""
    return base ** exponent

def dynamic_args(*args, **kwargs):
    """
    *args = Tuple of positional arguments
    **kwargs = Dictionary of keyword arguments
    """
    print(f"Positional: {args}")
    print(f"Keywords: {kwargs}")

# Lambda (Anonymous Function)
square = lambda x: x * x

"""
SECTION 2: INTERMEDIATE (Functions & Files)
-------------------------------------------
Writing reusable logic and handling I/O.
"""

def file_handling_demo():
    print("\n--- [2] FILE HANDLING ---")
    filename = "demo.txt"
    
    # Context Manager ('with') automatically closes file even if error occurs
    with open(filename, "w") as f:
        f.write("Log Entry 1\nLog Entry 2")
        
    # Reading back
    with open(filename, "r") as f:
        # List comprehension: compact loop
        lines = [line.strip() for line in f.readlines()] 
        print(f"Read {len(lines)} lines from file.")

"""
SECTION 3: EXPERT (OOP & Recursion)
-----------------------------------
This is what differentiates a Coder from a Scripter.
"""

# Recursive Function: A function that calls itself
# Common use case: Scanning deep directory structures with unknown depth
def traverse_virtual_dir(structure, indent=0):
    for key, value in structure.items():
        print(" " * indent + f"[DIR] {key}")
        if isinstance(value, dict):
            traverse_virtual_dir(value, indent + 2) # Recursive call
        else:
            print(" " * (indent+2) + f"[FILE] {value}")

# Classes: Encapsulation
class AutomationJob:
    def __init__(self, name):
        self._name = name # Protected variable
        
    @property
    def name(self):
        """Getter: Allows accessing .name but protecting _name"""
        return self._name.upper()

def expert_concepts():
    print("\n--- [3] EXPERT CONCEPTS ---")
    
    # 1. Recursion Demo
    folder_structure = {
        "project": {
            "src": {"main.py": "code", "utils.py": "code"},
            "tests": {"test_api.py": "code"}
        }
    }
    print("Recursive Directory Scan:")
    traverse_virtual_dir(folder_structure)
    
    # 2. OOP Demo
    job = AutomationJob("etl_daily_run")
    print(f"Running Job: {job.name}") # Uses @property getter

if __name__ == "__main__":
    basic_concepts()
    file_handling_demo()
    expert_concepts()
