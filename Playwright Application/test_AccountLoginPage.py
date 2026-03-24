import time

from playwright.sync_api import expect


def test_AccountLoginPage(BrowserLogin):
    BrowserLogin.goto("https://automationteststore.com/index.php?rt=account/login")
    BrowserLogin.get_by_role("radio", name="account").check()
    BrowserLogin.get_by_role("button",name="Continue").click()

def test_CreateAccount(BrowserLogin):
    BrowserLogin.goto("https://automationteststore.com/index.php?rt=account/create")
    BrowserLogin.locator("#AccountFrm_firstname").fill("Mathan")
    BrowserLogin.locator("#AccountFrm_lastname").fill("kumar")
    BrowserLogin.locator("#AccountFrm_email").fill("Mathankumar9488@gmail.com")
    BrowserLogin.locator("#AccountFrm_telephone").fill("9488235067")
    BrowserLogin.locator("#AccountFrm_fax").fill("+1-408-555-0100")
    BrowserLogin.locator("#AccountFrm_company").fill("Tecnotree")
    BrowserLogin.locator("#AccountFrm_address_1").fill("6/550/9.5")
    BrowserLogin.locator("#AccountFrm_address_2").fill("Lakshmi nagar,Pethanatchi nagar")
    BrowserLogin.locator("#AccountFrm_city").fill("Virudhunagar")
    BrowserLogin.locator('#AccountFrm_zone_id').select_option(value="3522")
    BrowserLogin.locator('#AccountFrm_postcode').fill("626001")
    BrowserLogin.locator('#AccountFrm_country_id').select_option(value="99")
    BrowserLogin.locator('#AccountFrm_loginname').fill("Mathankumar")
    BrowserLogin.locator('#AccountFrm_password').fill("9488@1")
    BrowserLogin.locator('#AccountFrm_confirm').fill("9488@1")
    BrowserLogin.locator('#AccountFrm_newsletter0').click()
    BrowserLogin.locator('#AccountFrm_agree').click()
    BrowserLogin.get_by_role("button", name="Continue").click()
    BrowserLogin.goto("https://automationteststore.com/index.php?rt=account/success")
    # BrowserLogin.get_by_role('nav a[href="https://automationteststore.com/index.php?rt=account/account"]').click()
    # time.sleep(5)