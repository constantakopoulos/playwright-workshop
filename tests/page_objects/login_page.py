from tests.page_objects.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    SUBMIT_BUTTON = "#submit"
    SUCCESSFUL_LOGIN_TEXT = "text=Logged In Successfully"

    def fill_username(self, username):
        self.fill(self.USERNAME_FIELD, username)

    def fill_password(self, password):
        self.fill(self.PASSWORD_FIELD, password)

    def click_submit(self):
        self.click_on(self.SUBMIT_BUTTON)
