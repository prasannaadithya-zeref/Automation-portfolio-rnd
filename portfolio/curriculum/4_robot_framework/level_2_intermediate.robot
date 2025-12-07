*** Settings ***
Documentation       LEVEL 2: INTERMEDIATE ROBOT
...                 Topic: Loops, Conditions, and Collections.
Library             Collections

*** Variables ***
@{SKILLS_LIST}      Python    Robot    SQL    AWS
&{USER_DICT}        name=Prasanna    role=SDET

*** Test Cases ***
TestCase 01: Looping Through A List
    [Documentation]    Iterate over list items (For Loop).
    Log To Console     \n--- SKILLS LIST ---
    FOR    ${skill}    IN    @{SKILLS_LIST}
        Log To Console    I have mastered: ${skill}
        Run Keyword If    '${skill}' == 'AWS'    Log To Console    (High Demand Skill!)
    END

TestCase 02: Dictionary Usage
    [Documentation]    Accessing Key-Value pairs.
    Log To Console     \n--- USER DETAILS ---
    Log To Console     User Name: ${USER_DICT.name}
    
    # Verify Dictionary Key Exists
    Dictionary Should Contain Key    ${USER_DICT}    role

# --- HANDS ON TASK ---
# Create a test that has a list of numbers @{NUMS} = 1 2 3 4
# Loop through them and Log "Even" if the number is divisible by 2.
# Hint: Use '${num} % 2' in Evaluate.
