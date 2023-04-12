*** Settings ***
Documentation  Automated case for shopping cart funcionality
Library        SeleniumLibrary
Test Setup     Maximize Browser Window
Suite Setup    Prepare Env

*** Variables ***
${ACCEPT_POLICY}             //*[@id="onetrust-accept-btn-handler"]
${CATALOG_VIEW}              //a[normalize-space()='Elektronika']
${PRODUCT_VIEW}              //body[1]/div[1]/main[1]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/picture[2]
${ADD_PROCUCT}               //form[contains(@data-action-field,'pdp')]//span[contains(text(),'DODAJ DO KOSZYKA')]
${SHOW_CART}                 (//a[@title='pokaż koszyk'])[1]
${CART_ITEMS_AMOUNT}         //h3[@class='cart-primary__title hidden-mobile hidden-tablet']

*** Test Cases ***
Adding Shopping Product Should Increase Amount
    [Setup]   Open Shop Webpage
    Accept Privacy Policy
    Go To Catalog View
    Product View
    Add Product To Cart
    Show Cart
    Check If Shopping Cart Has 1 Products




*** Keywords ***
Prepare Env
    Set Selenium Speed          1

Open Shop Webpage
    Open Browser    https://www.biedronka.pl/pl     chrome

Accept Privacy Policy
    Click Button               ${ACCEPT_POLICY}

Go To Catalog View
    Click Element              ${CATALOG_VIEW}

Product View
    Click Element              ${PRODUCT_VIEW}

Add Product To Cart
    Click Element              ${ADD_PROCUCT}

Show Cart
    Click Element              ${SHOW_CART}

Check If Shopping Cart Has 1 Products
    Element Text Should Be     ${CART_ITEMS_AMOUNT}        TWÓJ KOSZYK (1 PRODUKT)