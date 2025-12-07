*** Settings ***
Documentation     Integration Suite: API Testing and AWS/ETL pipelines.
...               Uses RequestsLibrary for API and Custom Python Library for AWS.
Library           RequestsLibrary
Library           ../../python-frameworks/utils/aws_handler.py    WITH NAME    AWS
Resource          ../resources/common.resource

*** Variables ***
${API_BASE_URL}   http://localhost:5000
${BUCKET_NAME}    test-automation-bucket
${TEST_FILE}      etl_config.json

*** Test Cases ***
Verify API User Data
    [Documentation]    
    ...    **SCENARIO: REST API Validation**
    ...    
    ...    *Goal*: Verify that the backend API returns the correct data for User ID 1.
    ...    *Steps*:
    ...    1. Create a session (like opening a browser tab but for code).
    ...    2. Send a GET request to /users/1.
    ...    3. Check if status code is 200 (OK).
    ...    4. Parse the JSON and check key specific fields ('role').
    [Tags]             api
    Create Session    mock_api    ${API_BASE_URL}
    ${response}=      GET On Session    mock_api    /users/1
    Should Be Equal As Strings    ${response.status_code}    200
    ${json}=          Set Variable    ${response.json()}
    Should Be Equal   ${json['role']}    Automation Engineer

Verify AWS S3 Upload For ETL
    [Documentation]    
    ...    **SCENARIO: Cloud ETL Pipeline**
    ...    
    ...    *Goal*: Ensure our Python framework can communicate with AWS S3.
    ...    *Why?*: Data Engineers often trigger jobs by dropping a file into S3. We must test that trigger.
    ...    *Method*: We use a Custom Python Library (AWSHandler) because Robot doesn't do S3 natively.
    [Tags]             aws    etl
    # Create a dummy file
    Create File       ${TEST_FILE}    {"etl_mode": "incremental"}
    
    # Use Custom Python Library
    ${status}=        AWS.Upload File To S3    ${TEST_FILE}    ${BUCKET_NAME}    configs/${TEST_FILE}
    Should Be True    ${status}    Upload failed or skipped (check credentials)
    
    ${exists}=        AWS.Check File Exists In S3    ${BUCKET_NAME}    configs/${TEST_FILE}
    Log               File check status: ${exists}

*** Keywords ***
Create File
    [Arguments]    ${path}    ${content}
    Create File    ${path}    ${content}
