import pytest
from selenium import webdriver

from pages.catalog_page import CatalogPage


@pytest.fixture(scope="function")
def catalog_page(browser: webdriver) -> CatalogPage:
    catalog_page = CatalogPage(driver=browser)
    catalog_page.open_page()
    return catalog_page
#
