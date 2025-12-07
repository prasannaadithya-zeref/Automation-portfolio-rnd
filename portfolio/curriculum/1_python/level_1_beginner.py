"""
PYTHON LEVEL 1: BEGINNER
========================
Topic: Foundations of Python Programming.

[THEORY]
1. Variables: Containers for storing data values.
2. Data Types: String (text), Integer (whole numbers), Float (decimals), Boolean (True/False).
3. Lists/Dicts: Ways to store collections of data.
4. Loops: Repeating actions (For/While).
5. Functions: Reusable blocks of code.

[REAL WORLD EXAMPLE]
A login script needs variables (username), conditions (if password correct), 
and functions (validate_login).
"""

def topic_1_variables_datatypes():
    print("\n--- 1. VARIABLES & DATA TYPES ---")
    # Theory: Python is dynamically typed.
    user_name = "AutomationBot" # String
    retry_count = 3             # Integer
    success_rate = 99.5         # Float
    is_active = True            # Boolean
    
    print(f"User: {user_name}, Type: {type(user_name)}")

def topic_2_collections():
    print("\n--- 2. LISTS, TUPLES, SETS, DICTIONARIES ---")
    
    # LIST: Ordered, Mutable. Use for lists of items.
    browsers = ["Chrome", "Firefox", "Edge"]
    browsers.append("Safari")
    
    # TUPLE: Ordered, Immutable. Use for fixed configs.
    resolution = (1920, 1080)
    
    # SET: Unordered, Unique. Use for removing duplicates.
    tags = {"smoke", "regression", "smoke"} # "smoke" appears once
    
    # DICT: Key-Value. Use for object properties.
    config = {
        "url": "google.com",
        "timeout": 10
    }
    
    print(f"Browsers: {browsers}")
    print(f"Config timeout: {config['timeout']}")

def topic_3_loops_conditions():
    print("\n--- 3. LOOPS & CONDITIONS ---")
    
    test_results = ["PASS", "FAIL", "PASS"]
    
    # For Loop
    for result in test_results:
        if result == "FAIL":
            print(f"Found a failure! Triggering alert...")
        else:
            print("Test passed.")

def topic_4_functions(name, role="Tester"):
    """
    Param 'role' is a default argument.
    """
    print(f"\n--- 4. FUNCTIONS ---")
    print(f"Welcome {name}, your role is {role}")
    return True

# --- PRACTICE TASK ---
# Task: Write a function 'calculate_grade' that takes a score (0-100)
# and returns 'A', 'B', 'C', or 'F' based on thresholds (90, 80, 70).
# Try writing it below!

def practice_task_solution(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    else: return 'F'

if __name__ == "__main__":
    topic_1_variables_datatypes()
    topic_2_collections()
    topic_3_loops_conditions()
    topic_4_functions("Prasanna", "Lead SDET")
    print(f"Practice Grade: {practice_task_solution(85)}")
