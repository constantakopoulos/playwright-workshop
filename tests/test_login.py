from playwright.sync_api import sync_playwright


def test_login_successful():
    with sync_playwright() as page:
        browser = page.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.locator("#username").fill("student")
        page.locator("#password").fill("Password123")
        page.locator("#submit").click()
        assert page.locator("text=Logged In Successfully").is_visible()


def test_login_wrong_username():
    """Write your test here"""
    pass


def test_login_wrong_password():
    """Write your test here"""
    pass