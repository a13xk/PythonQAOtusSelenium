import pytest
from selenium import webdriver

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def main_page(browser: webdriver, base_class_logging: bool) -> MainPage:
    main_page = MainPage(driver=browser, logging_enabled=base_class_logging)
    main_page.open_page()
    return main_page
#


@pytest.fixture(scope="function")
def remote_main_page(remote_browser: webdriver, opencart_url: str, base_class_logging: bool) -> MainPage:
    main_page = MainPage(driver=remote_browser, url=opencart_url, logging_enabled=base_class_logging)
    main_page.open_page()
    return main_page
#


@pytest.fixture(scope="function")
def remote_browserstack_main_page(remote_browserstack: webdriver, opencart_url: str, base_class_logging: bool) -> MainPage:
    main_page = MainPage(driver=remote_browserstack, url=opencart_url, logging_enabled=base_class_logging)
    main_page.open_page()
    return main_page
#


@pytest.fixture(scope="function")
def selenoid_main_page(selenoid_browser: webdriver, opencart_url: str, base_class_logging: bool) -> MainPage:
    main_page = MainPage(driver=selenoid_browser, url=opencart_url, logging_enabled=base_class_logging)
    main_page.open_page()
    return main_page
#
