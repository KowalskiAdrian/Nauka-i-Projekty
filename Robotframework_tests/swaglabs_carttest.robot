*** Settings ***
Documentation    Automated case for shopping cart funcionality
Library  SeleniumLibrary
Test Setup   Maximize Browser Window
Suite Setup     Prepare Env

*** Variables ***
${LOGIN URL}        https://www.saucedemo.com/
${username_field}   //input[@id='user-name']
${password_field}   //input[@id='password']
${LOGIN_BUTTON}     //input[@id='login-button']
${APP_LOGO}         //div[@class='app_logo']
${ADD_PRODUCT}      //button[@id='add-to-cart-sauce-labs-backpack']
${SHOW_CART}        //a[@class='shopping_cart_link']
${CART_ITEMS_AMOUNT}    //div[@class='cart_quantity']

*** Test Cases ***
Valid Login
    [Setup]   Open Browser To Login Page
    Input Username
    Input Password
    Click Login Button
    Welcome Page Should Be Open
    Add Product To Cart
    Show Cart
    Check If Shopping Cart Has 1 Products

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
Add Product To Cart
    Click Element           ${ADD_PRODUCT}
Show Cart
    Click Element              ${SHOW_CART}
Check If Shopping Cart Has 1 Products
    Element Text Should Be     ${CART_ITEMS_AMOUNT}            1