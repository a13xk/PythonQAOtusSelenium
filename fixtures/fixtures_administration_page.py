import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import OpenCartConfiguration
from locators import AdminLoginPage
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