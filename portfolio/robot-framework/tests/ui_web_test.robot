*** Settings ***
Documentation     UI Automation Suite with Data Driven Testing.
...               Demonstrates usage of SeleniumLibrary for web interactions.
Library           SeleniumLibrary
Test Teardown     Close Browser

*** Variables ***
${LOGIN URL}      https://the-internet.herokuapp.com/login
${BROWSER}        Chrome

*** Test Cases ***    USERNAME        PASSWORD        EXPECTED_MSG
Invalid Login 1       tomsmith        wrongpass       Your username is invalid!
Invalid Login 2       inavliduser     SuperSecret!    Your username is invalid!
Valid Login           tomsmith        SuperSecret!    You logged into a secure area!

*** Keywords ***
Login With Credentials
    [Arguments]    ${username}    ${password}    ${expected_message}
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Input Text      id:username    ${username}
    Input Text      id:password    ${password}
    Click Button    css:button[type='submit']
    Page Should Contain    ${expected_message}
