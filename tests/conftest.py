import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from tests.settings.config import AppEnvSettings

load_dotenv()

pytest_plugins = ["tests.pytest_fixtures.page_fixtures"]


@pytest.fixture(scope="session")
def app_env_settings() -> AppEnvSettings:
    app_env_settings = AppEnvSettings()
    print(f"\nTests started against the {app_env_settings.environment} environment")
    return app_env_settings


@pytest.fixture()
def page(request, app_env_settings):
    headless = True
    if request.config.getoption("--headed"):
        headless = False
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        context.set_default_timeout(timeout=15000)
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
