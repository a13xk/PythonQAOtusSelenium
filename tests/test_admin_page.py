from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import OpenCartConfiguration
from locators.add_product_page import AddProductPage
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

    def test_add_new_product(self, browse_to_catalog_products_table):
        browser = browse_to_catalog_products_table
        wait = WebDriverWait(driver=browser, timeout=5)

        add_new_button = browser.find_element_by_xpath(xpath=AdministrationPage.XPATH_ADD_NEW_BUTTON)
        add_new_button.click()
        wait.until(EC.presence_of_element_located(locator=(By.ID, AddProductPage.ID_PRODUCT_FORM)))

        product_name = browser.find_element_by_id(id_=AddProductPage.ID_INPUT_PRODUCT_NAME)
        product_name.clear()
        product_name.send_keys("New product")

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

        div_alert_success = wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, AddProductPage.CSS_DIV_ALERT_SUCCESS)))
        assert "Success: You have modified products!" in div_alert_success.get_property(name="innerHTML")
    #
#
