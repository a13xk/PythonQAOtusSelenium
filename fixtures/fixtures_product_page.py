import pytest
from selenium import webdriver

from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def product_page(browser: webdriver, base_class_logging: bool) -> ProductPage:
    product_page = ProductPage(driver=browser, logging_enabled=base_class_logging)
    product_page.open_page()
    return product_page
#
