import time
from time import sleep

from playwright.sync_api import expect


def testProductAddToCart(BrowserLogin):
    BrowserLogin.goto("https://automationteststore.com/")
    BrowserLogin.goto("https://automationteststore.com/index.php?rt=product/category&path=43")
    AddTocartSkinProduct= BrowserLogin.locator(".productcart").nth(2)
    AddTocartSkinProduct.click()

def testShoppingCart(BrowserLogin):
    BrowserLogin.goto("https://automationteststore.com/index.php?rt=checkout/cart")
    BrowserLogin.locator("#cart_checkout2").click()
    BrowserLogin.goto("https://automationteststore.com/index.php?rt=account/login")
    BrowserLogin.locator('#loginFrm_loginname').fill("Mathankumar")
    BrowserLogin.locator('#loginFrm_password').fill("9488@1")
    BrowserLogin.get_by_role("button", name="Login").click()
    BrowserLogin.goto("https://automationteststore.com/index.php?rt=checkout/confirm")
    BrowserLogin.get_by_role("button", name="Confirm Order").click()
    sleep(2)