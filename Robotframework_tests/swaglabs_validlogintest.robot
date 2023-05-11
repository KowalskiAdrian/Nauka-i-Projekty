*** Settings ***
Documentation    A test suite with a single test for a valid login.
Library  SeleniumLibrary
Test Setup   Maximize Browser Window
Suite Setup     Prepare Env

*** Variables ***
${LOGIN URL}      https://www.saucedemo.com/
${username_field}   //input[@id='user-name']
${password_field}   //input[@id='password']
${LOGIN_BUTTON}     //input[@id='login-button']
${APP_LOGO}        //div[@class='app_logo']

*** Test Cases ***
Valid Login
    [Setup]   Open Browser To Login Page
    Input Username
    Input Password
    Click Login Button
    Welcome Page Should Be Open
    [teardown]

*** Keywords ***
Prepare Env
    Set Selenium Speed          3
Open Browser To Login Page
    Open Browser    ${LOGIN URL}        chrome
Input Username
    Input Text      ${username_field}                standard_user
Input Password
    Input Text      ${password_field}                secret_sauce
Click Login Button
    Click Button    ${LOGIN_BUTTON}
Welcome Page Should Be Open
    Element Text Should Be     ${APP_LOGO}        Swag Labs