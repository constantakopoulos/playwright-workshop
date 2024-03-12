from typing import Optional

from playwright.sync_api import ElementHandle, Locator, Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Navigation methods
    def go_to_url(self, url):
        self.page.goto(url)

    # Element retrieval methods
    def find_element(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def get_by_text(self, text):
        return self.page.get_by_text(text=text)

    def get_by_placeholder(self, placeholder_text):
        return self.page.get_by_placeholder(placeholder_text)

    def get_by_label(self, label_text):
        return self.page.get_by_label(label_text)

    def get_by_role(self, role, name=None):
        return self.page.get_by_role(role, name=name)

    # Element interaction methods
    def click_on(self, selector: str) -> None:
        self.page.locator(selector).click()

    def keyboard_press(self, key):
        self.page.keyboard.press(key)

    def select_option(self, option):
        self.page.select_option(option)

    def type(self, selector, text):
        return self.page.type(selector, text)

    def fill(self, selector, value):
        return self.page.fill(selector, value)

    # Element state methods
    def element_is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def is_enabled(self, selector):
        return self.page.is_enabled(selector)

    def is_visible(self, selector):
        return self.page.is_visible(selector)

    # Waiting methods
    def wait_for_timeout(self, timeout) -> None:
        self.page.wait_for_timeout(timeout=timeout)

    def wait_until_element_visible(self, selector: str, timeout: int = 15000) -> Optional[ElementHandle]:
        return self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    def page_loaded(self):
        self.page.wait_for_load_state()

    # Inner text methods
    def get_element_inner_text(self, selector: str) -> str:
        self.wait_for_timeout(2000)
        return self.page.inner_text(selector=selector)
