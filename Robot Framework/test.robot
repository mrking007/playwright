*** Settings ***
Library    Browser




*** Variables ***
${url}    https://practicetestautomation.com/practice-test-login/
${userName}    //*[@name="username"]
${password}    //*[@id="password"]
${submit}    //*[@id="submit"]


*** Test Cases ***
Correct_cred_with_Login
     LoginWIthcorrectcred
Incorrect_cred_with_login
    LoginWithincorrectusername
*** Keywords ***
LoginWIthcorrectcred
    New Browser    chromium     headless=False
    Set Browser Timeout    30s
    browser.New Page    ${url}
    Sleep    5s
    browser.Fill Text    ${userName}    student
    browser.Fill Text    ${password}    Password123
    browser.Click    ${submit}
LoginWithincorrectusername
        New Browser    chromium     headless=False
    Set Browser Timeout    30s
    browser.New Page    ${url}
    Sleep    5s
    browser.Fill Text    ${userName}    incorrectUser
    browser.Fill Text    ${password}    Password123
    browser.Click    ${submit}