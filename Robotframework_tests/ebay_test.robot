*** Settings ***
Documentation  Automated case for shopping cart funcionality
Library  SeleniumLibrary
Test Setup   Maximize Browser Window

*** Variables ***

${CATALOG_VIEW}              //div[@id='destinations_list1']//li[5]//a[1]//div[2]
${PRODUCT_VIEW}              (//*[@class='s-item__title'])[1]
${ADD_PRODUCT}               //span[contains(text(),'Dodaj do koszyka')]
${CART_ITEMS_AMOUNT}         //i[@id='gh-cart-n']

*** Test Cases ***
Adding Shopping Product Should Increase Amount
    [Setup]   Open Shop Webpage
    Go To Product Catalog
    Go To Product
    Add Product To Cart
    Check If Shopping Cart Has 1 Products




*** Keywords ***

Open Shop Webpage
    Open Browser        https://www.ebay.pl/    chrome

Go To Product Catalog
    Click Element              ${CATALOG_VIEW}

Go To Product
    Click Element              ${PRODUCT_VIEW}

Add Product To Cart
    Click Element               ${ADD_PRODUCT}

Check If Shopping Cart Has 1 Products
    Element Text Should Be    ${CART_ITEMS_AMOUNT}        1