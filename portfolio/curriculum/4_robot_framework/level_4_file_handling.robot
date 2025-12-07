*** Settings ***
Documentation       LEVEL 4: FILE HANDLING IN ROBOT
...                 Demonstrating how to read files using BuiltIn, OperatingSystem, and Python.
Library             OperatingSystem
Library             Collections
# We can import our Python file as a library to handle complex logic!
Library             ../../curriculum/1_python/file_handling_mastery.py    WITH NAME    FileLib

*** Test Cases ***
TestCase 01: Read Text File (Built-In)
    [Documentation]    Using OperatingSystem library to read logs.
    # Create valid file first
    Create File    robot_test.txt    content=Hello Robot
    
    # Read it
    ${content}=    Get File    robot_test.txt
    Log To Console    \nFile Content: ${content}
    Should Contain    ${content}    Hello

TestCase 02: Read CSV using Python (Hybrid)
    [Documentation]    Robot is bad at parsing CSV natively. We call Python.
    # Create dummy csv
    Create File    robot_data.csv    content=id,user\n1,Admin\n2,Guest

    # Call the python method 'read_csv_native' from our custom library
    # Note: Snake_case in Python becomes Title Case in Robot
    ${data_list}=    FileLib.Read Csv Native    robot_data.csv
    
    Log To Console    \nParsed CSV Data: ${data_list}
    
    # Accessing the first dictionary in the list
    ${first_row}=     Set Variable    ${data_list}[0]
    Log To Console    First User: ${first_row}[user]

TestCase 03: Read JSON Config
    [Documentation]    Reading JSON is essential for API testing.
    Create File    robot_config.json    content={"env": "QA", "timeout": 30}
    
    ${json_data}=     FileLib.Read Json Safe    robot_config.json
    Log To Console    \nEnvironment: ${json_data}[env]
    Should Be Equal   ${json_data}[env]    QA
