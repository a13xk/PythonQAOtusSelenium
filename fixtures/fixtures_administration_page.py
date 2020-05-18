import pytest
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import OpenCartConfiguration
from locators import AdminLoginPage, AddProductPage
from locators.administration_page import AdministrationPage


@pytest.fixture(scope="function")
def login_to_administration_page(browser):
    wait = WebDriverWait(driver=browser, timeout=15)
    browser.get(url="https://localhost/admin/")
    input_username = browser.find_element_by_id(id_=AdminLoginPage.ID_INPUT_USERNAME)
    input_username.click()
    input_username.send_keys(OpenCartConfiguration.ADMIN_USERNAME)

    input_password = browser.find_element_by_id(id_=AdminLoginPage.ID_INPUT_PASSWORD)
    input_password.click()
    input_password.send_keys(OpenCartConfiguration.ADMIN_PASSWORD)

    login_button = browser.find_element_by_xpath(xpath=AdminLoginPage.XPATH_LOGIN_BUTTON)
    login_button.click()
    wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdministrationPage.XPATH_DASHBOARD_HEADING)))

    yield browser

    logout_button = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_LOGOUT_BUTTON)
    logout_button.click()

    wait.until(EC.visibility_of_element_located(locator=(By.ID, AdminLoginPage.ID_INPUT_PASSWORD)))
#


@pytest.fixture(scope="function")
def browse_to_catalog_products_table(login_to_administration_page):
    browser = login_to_administration_page
    wait = WebDriverWait(driver=browser, timeout=5)

    catalog = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_MENU_CATALOG)
    catalog.click()

    catalog_products = wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdministrationPage.XPATH_CATALOG_PRODUCTS_LINK)))
    catalog_products.click()
    wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdministrationPage.XPATH_PRODUCTS_TABLE)))
    yield browser
#


@pytest.fixture(scope="function")
def add_new_product(browse_to_catalog_products_table, new_product_name):
    browser = browse_to_catalog_products_table
    wait = WebDriverWait(driver=browser, timeout=5)

    add_new_button = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_ADD_NEW_BUTTON)
    add_new_button.click()
    wait.until(EC.presence_of_element_located(locator=(By.ID, AddProductPage.ID_PRODUCT_FORM)))

    product_name = browser.find_element_by_id(id_=AddProductPage.ID_INPUT_PRODUCT_NAME)
    product_name.clear()
    product_name.send_keys(new_product_name)

    meta_tag_title = browser.find_element_by_id(id_=AddProductPage.ID_INPUT_META_TAG_TITLE)
    meta_tag_title.clear()
    meta_tag_title.send_keys("metatag")

    data_tab = browser.find_element_by_xpath(xpath=AddProductPage.XPATH_DATA_TAB)
    data_tab.click()
    wait.until(EC.visibility_of_element_located(locator=(By.ID, AddProductPage.ID_DATA_TAB)))

    model = browser.find_element_by_id(id_=AddProductPage.ID_INPUT_MODEL)
    model.clear()
    model.send_keys("New model")

    save_button = browser.find_element_by_xpath(xpath=AddProductPage.XPATH_SAVE_BUTTON)
    save_button.click()

    wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, AddProductPage.CSS_DIV_ALERT_SUCCESS)))
    dismiss_alert = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_DISMISS_ALERT)
    dismiss_alert.click()

    yield browser
#


@pytest.fixture(scope="function")
def product_table(browse_to_catalog_products_table) -> BeautifulSoup:
    page_html = browse_to_catalog_products_table.page_source
    soup = BeautifulSoup(markup=page_html, features='html.parser')
    return soup.find(name="table")
#


@pytest.fixture(scope="function")
def new_product_name() -> str:
    return "New product"
#
