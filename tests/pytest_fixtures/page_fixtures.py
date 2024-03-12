import pytest
from tests.page_objects.login_page import LoginPage


@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page
