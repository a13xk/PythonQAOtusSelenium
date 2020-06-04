import pytest
from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page(browser: webdriver) -> LoginPage:
    login_page = LoginPage(driver=browser)
    login_page.open_page()
    return login_page
#
