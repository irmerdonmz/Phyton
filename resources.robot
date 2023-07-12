
*** Settings ***
Library SeleniumLibrary


*** Variables ***
${url}      https://www.demoblaze.com/
${browser}  chrome
${userName}  iremerd
${password}  010203

*** Test Cases ***
TC1
    Open Browser To Login Page
    ${PageTitle} =  launchBrowser    ${url}     ${browser}
    log to console  ${pageTitle}
    log   ${PageTitle}
    input text  name: userName    iremerd
    input text  password: password    010203
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${url}    ${browser}

Submit Credentials
    Click Button    login_button

Welcome Page Should Be Open
    Title Should Be    Welcome iremerd