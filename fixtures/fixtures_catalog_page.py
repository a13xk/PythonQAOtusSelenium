import pytest
from selenium import webdriver

from pages.catalog_page import CatalogPage


@pytest.fixture(scope="function")
def catalog_page(browser: webdriver, base_class_logging: bool) -> CatalogPage:
    catalog_page = CatalogPage(driver=browser, logging_enabled=base_class_logging)
    catalog_page.open_page()
    return catalog_page
#
