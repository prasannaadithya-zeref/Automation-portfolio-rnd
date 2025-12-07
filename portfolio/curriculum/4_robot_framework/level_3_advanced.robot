*** Settings ***
Documentation       LEVEL 3: ADVANCED & HYBRID FRAMEWORK
...                 Topic: Calling Python from Robot (The Power Move).
...                 This allows you to do complex logic in Python and simple calls in Robot.

# Import the Python file as a Library
Library             ../../python-frameworks/utils/aws_handler.py

*** Test Cases ***
TestCase 01: Hybrid Python-Robot Execution
    [Documentation]    Uses the 'AWSHandler' class we wrote in Python.
    Log To Console     \n--- CALLING PYTHON CODE ---
    
    # 1. We essentially call: aws_handler.get_bucket_status("my-bucket")
    # Robot converts snake_case to Space Separated Title Case automatically!
    
    # NOTE: Since we don't have real AWS creds, this might fail or mock.
    # Let's use a simpler BuiltIn Evaluate for the demo if that lib isn't ready.
    
    ${python_math}=    Evaluate    import('math').sqrt(16)    modules=math
    Log To Console     Python calculated square root: ${python_math}

TestCase 02: Data Driven Testing Template
    [Template]    Login With Credentials
    admin       admin123
    user        wrongpass
    # The template automatically runs the keyword below for each row

*** Keywords ***
Login With Credentials
    [Arguments]    ${username}    ${password}
    Log To Console    Attempting login for: ${username}
    # Logic to input text...
