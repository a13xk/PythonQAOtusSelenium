import pytest
from selenium import webdriver

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def main_page(browser: webdriver) -> MainPage:
    main_page = MainPage(driver=browser)
    main_page.open_page()
    return main_page
#
