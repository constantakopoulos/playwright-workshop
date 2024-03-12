from pytest_bdd import given, scenarios, then, when

scenarios("../features/login.feature")


@given("user navigates to Login Page")
def step_navigate_to_login(login_page, app_env_settings):
    login_page.go_to_url(app_env_settings.client_url)


@when("enters the correct credentials")
def step_enter_correct_credentials(login_page, app_env_settings):
    login_page.fill_username(app_env_settings.login_user)
    login_page.fill_password(app_env_settings.login_password)
    login_page.click_submit()


@then("user is successfully logged in")
def step_successful_login(login_page):
    assert login_page.element_is_visible(login_page.SUCCESSFUL_LOGIN_TEXT)
