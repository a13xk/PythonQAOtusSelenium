import pytest

from configuration import OpenCart
from pages.administration_page import AdministrationPage


@pytest.fixture(scope="function")
def administration_page(admin_login_page, browser):
    admin_login_page.log_in(
        username=OpenCart.ADMIN_USERNAME,
        password=OpenCart.ADMIN_PASSWORD
    )
    administration_page = AdministrationPage(driver=browser)
    yield administration_page
    administration_page.log_out()
#


@pytest.fixture(scope="function")
def catalog_products_page(administration_page) -> AdministrationPage:
    administration_page.open_catalog_products()
    return administration_page
#


@pytest.fixture(scope="function")
def product_info() -> dict:
    return {
        "product_name": "New product",
        "meta_tag_title": "metatag",
        "model": "New model",
        "modified_product_name": "Modified product"
    }
#


@pytest.fixture(scope="function")
def add_new_product(catalog_products_page, product_info):
    catalog_products_page.add_product(
        product_name=product_info.get("product_name"),
        meta_tag_title=product_info.get("meta_tag_title"),
        model=product_info.get("model")
    )
    catalog_products_page.find_element(locator=catalog_products_page.DIV_ALERT_SUCCESS)
    catalog_products_page.find_element(locator=catalog_products_page.BUTTON_DISMISS_ALERT).click()
    return catalog_products_page
#
