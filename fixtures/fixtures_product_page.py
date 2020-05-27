import pytest

from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def product_page(browser) -> ProductPage:
    product_page = ProductPage(driver=browser)
    product_page.open_page()
    return product_page
#
