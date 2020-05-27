import pytest

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page(browser) -> LoginPage:
    login_page = LoginPage(driver=browser)
    login_page.open_page()
    return login_page
#
