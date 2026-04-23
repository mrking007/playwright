def test_LoginFunction(BrowserSetUp):
    BrowserSetUp.goto("https://rahulshettyacademy.com/client")
    BrowserSetUp.get_by_placeholder("email@example.com").fill("mathankumar9488@gmail.com")
    BrowserSetUp.get_by_placeholder("enter your passsword").fill("Mathan9488@1")
    BrowserSetUp.get_by_role("button",name="login").click()