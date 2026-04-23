import page
from playwright.sync_api import expect


def test_Subscribe_to_Newsletter(BrowserLogin):
    BrowserLogin.goto("https://automationteststore.com/")
    expect(BrowserLogin.get_by_placeholder("Subscribe to Newsletter")).to_be_visible()
    BrowserLogin.get_by_text("Subscribe").click()

def test_AlertBox(rahulShettyCode):
    rahulShettyCode.goto("https://rahulshettyacademy.com/AutomationPractice/")
    rahulShettyCode.on("dialog",lambda dialog:dialog.accept())
    rahulShettyCode.locator("#confirmbtn").click()

def test_frameHandling(rahulShettyCode):
    rahulShettyCode.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frameHanding=rahulShettyCode.frame_locator("#courses-iframe")
    frameHanding.get_by_role("link",name="All Access plan").click()
    expect(rahulShettyCode.locator("body")).to_contain_text(" Leaders in market?!")

def test_checkTable(rahulShettyCode):
    rahulShettyCode.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range (rahulShettyCode.locator("th").count()):
        if rahulShettyCode.locator("th").filter(has_text="Price").count()>0:
            priceCoulum =i
            break
    riceRow = rahulShettyCode.locator("tr").filter(has_text="price")
    print(riceRow)
    expect(riceRow.locator("tr").nth(priceCoulum)).to_have_text("37")
    assert priceCoulum == "37"
def test_MouserHover(rahulShettyCode):
    rahulShettyCode.goto("https://rahulshettyacademy.com/AutomationPractice/")
    rahulShettyCode.locator("#mousehover").hover()
    rahulShettyCode.get_by_role("link",name="Reload").click()