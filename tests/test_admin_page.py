from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import OpenCartConfiguration
from locators.admin_login_page import AdminLoginPage
from locators.administration_page import AdministrationPage


class TestAdminPage:

    def test_header_logo_by_id(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.ID, AdminLoginPage.ID_HEADER_LOGO)))
    #

    def test_username_by_css(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, AdminLoginPage.CSS_USERNAME)))
    #

    def test_forgotten_password_by_xpath(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdminLoginPage.XPATH_FORGOTTEN_PASSWORD)))
    #

    def test_panel_heading_by_class_name(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CLASS_NAME, AdminLoginPage.CLASS_PANEL_HEADING)))
    #

    def test_opencart_by_link_text(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.LINK_TEXT, AdminLoginPage.LINK_TEXT_OPENCART)))
    #

    def test_login_logout(self, browser):
        wait = WebDriverWait(driver=browser, timeout=15)
        input_username = browser.find_element_by_id(id_=AdminLoginPage.ID_INPUT_USERNAME)
        input_username.click()
        input_username.send_keys(OpenCartConfiguration.ADMIN_USERNAME)

        input_password = browser.find_element_by_id(id_=AdminLoginPage.ID_INPUT_PASSWORD)
        input_password.click()
        input_password.send_keys(OpenCartConfiguration.ADMIN_PASSWORD)

        login_button = browser.find_element_by_xpath(xpath=AdminLoginPage.XPATH_LOGIN_BUTTON)
        login_button.click()
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdministrationPage.XPATH_DASHBOARD_HEADING)))

        logout_button = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_LOGOUT_BUTTON)
        logout_button.click()

        wait.until(EC.visibility_of_element_located(locator=(By.ID, AdminLoginPage.ID_INPUT_PASSWORD)))
    #

    def test_browse_to_catalog_products_table(self, login_to_administration_page):
        browser = login_to_administration_page
        wait = WebDriverWait(driver=browser, timeout=5)

        catalog = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_MENU_CATALOG)
        catalog.click()

        catalog_products = wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdministrationPage.XPATH_CATALOG_PRODUCTS_LINK)))
        catalog_products.click()
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdministrationPage.XPATH_PRODUCTS_TABLE)))
    #
#
