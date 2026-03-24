import pytest
from Browser import playwright
from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def page():
#     browser = playwright.firefox.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     browser.close()

from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="session")
def BrowserLogin():
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            BrowserLogin = context.new_page()
            yield BrowserLogin
            browser.close()