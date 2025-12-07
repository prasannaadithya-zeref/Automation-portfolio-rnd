*** Settings ***
Documentation       LEVEL 1: ROBOT FRAMEWORK BASICS
...                 Topic: Structure, Keywords, and Variables.
...                 [THEORY]
...                 1. Sections: Settings, Variables, Test Cases, Keywords.
...                 2. Indentation: Robot uses 4 spaces (or tabs).
...                 3. Logging: Log to console or HTML report.

*** Variables ***
${APP_URL}          https://google.com
${BROWSER}          Chrome
${RETRY_COUNT}      3

*** Test Cases ***
TestCase 01: Verify Variable Usage
    [Documentation]    This test demonstrates how to print variables.
    Log To Console     \nHello, welcome to Robot Framework!
    Log To Console     Testing URL: ${APP_URL}
    
    # Validation step (Assertion)
    Should Be Equal    ${BROWSER}    Chrome

TestCase 02: Using Custom Keywords
    [Documentation]    Calls a keyword defined below.
    Calculate Square    5

*** Keywords ***
Calculate Square
    [Arguments]    ${number}
    ${result}=    Evaluate    ${number} * ${number}
    Log To Console    The square of ${number} is ${result}

# --- HANDS ON TASK ---
# Create a test case that takes two variables, ${FIRST} and ${SECOND},
# and checks if they are NOT equal.
