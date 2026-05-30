*** Settings ***
Documentation     Sample test suite demonstrating Robot Framework syntax
Library           Collections
Library           String

*** Variables ***
${BROWSER}        Chrome
${URL}            https://example.com
${USERNAME}       testuser
${PASSWORD}       testpass123

*** Test Cases ***
Login Test
    [Documentation]    Test user login functionality
    [Tags]    login    smoke
    Log    Starting login test
    Log    Username: ${USERNAME}
    Should Be Equal    ${USERNAME}    testuser

Addition Test
    [Documentation]    Test basic addition operation
    [Tags]    math
    ${result}=    Evaluate    2 + 2
    Should Be Equal    ${result}    4
    Log    Addition result: ${result}

List Operations Test
    [Documentation]    Test list manipulation
    [Tags]    collections
    @{list}=    Create List    apple    banana    orange
    Length Should Be    ${list}    3
    Should Contain    ${list}    banana
    Log    List items: ${list}

String Operations Test
    [Documentation]    Test string manipulation
    [Tags]    string
    ${text}=    Set Variable    Robot Framework
    ${length}=    Get Length    ${text}
    Should Be Equal    ${length}    17
    Log    Text: ${text}, Length: ${length}

*** Keywords ***
Custom Keyword Example
    [Arguments]    ${arg1}    ${arg2}
    [Documentation]    Example custom keyword
    Log    Argument 1: ${arg1}
    Log    Argument 2: ${arg2}
    Should Be Equal    ${arg1}    ${arg2}
