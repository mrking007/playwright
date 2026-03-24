def test_childwindowOpen(BrowserLogin):
    BrowserLogin.goto("https://automationteststore.com/")
    with BrowserLogin.expect_popup() as newPageOpen:
        BrowserLogin.locator(".header_block").click()
        childWindowOpen = newPageOpen.value
        childWindowOpen.locator("https://www.facebook.com/")
def test_textContext(BrowserLogin):
    BrowserLogin.goto("https://automationteststore.com/")
    Text=BrowserLogin.locator(".contact").text_content()
    print(Text)
    spiltValue = Text.strip().split("@")[0]
    print(spiltValue)
    assert "admin" in spiltValue