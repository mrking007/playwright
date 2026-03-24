import time

from playwright.sync_api import expect


def test_incorrectUserName(playwright):
    browser =playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("username").fill("studentt")
    page.get_by_label("password").fill("Password123")
    page.get_by_role("button").click()
    expect(page.get_by_text("Your username is invalid!")).to_be_visible()