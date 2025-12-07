*** Settings ***
Documentation     Sample Data Validation Test Suite
...               Demonstrates how Robot Framework can be used for data quality checks.
Library           OperatingSystem
Library           Collections
Resource          ../resources/common.resource

*** Test Cases ***
Validate Daily Transaction File
    [Documentation]    Checks if the transaction file exists and has content.
    [Tags]             smoke    validation
    File Should Exist    ${DATA_DIR}/transactions.csv
    File Should Not Be Empty    ${DATA_DIR}/transactions.csv

Compare Database Record Count With File
    [Documentation]    Simulates a count check between DB and File.
    [Tags]             regression
    ${db_count}=    Get Database Record Count    SELECT count(*) FROM transactions
    ${file_count}=  Get File Line Count    ${DATA_DIR}/transactions.csv
    Should Be Equal As Integers    ${db_count}    ${file_count}    msg=Record counts do not match!

*** Variables ***
${DATA_DIR}       ./data
