import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def BrowserSetUp():
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            BrowserLogin = context.new_page()
            yield BrowserLogin
            browser.close()