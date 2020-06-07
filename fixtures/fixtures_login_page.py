import pytest
from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page(browser: webdriver, base_class_logging: bool) -> LoginPage:
    login_page = LoginPage(driver=browser, logging_enabled=base_class_logging)
    login_page.open_page()
    return login_page
#
