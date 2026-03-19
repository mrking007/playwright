import time

from pytest_playwright.pytest_playwright import browser,context,page

# def test_playwrightBasicsForFireForAnotherMethod(page:page):
#     page.goto("https://practicetestautomation.com/practice-test-login/")

# def test_playwrightBasics(playwright,browser,context):
#     browser =playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://practicetestautomation.com/practice-test-login/")

def test_playwrightBasicsForFireFox(playwright,browser,context,page):
    browser =playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("username").fill("student")
    page.get_by_label("password").fill("Password123")
    time.sleep(5)
    page.get_by_role("button").click()