from playwright.sync_api import Playwright


def e2e_web_Ecom(self,playwright:Playwright):
    browser = playwright.chromium.Context("")
