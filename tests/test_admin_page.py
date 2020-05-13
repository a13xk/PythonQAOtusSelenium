from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import OpenCartConfiguration
from locators.admin_page import AdminPage


class TestAdminPage:

    def test_header_logo_by_id(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.ID, AdminPage.ID_HEADER_LOGO)))
    #

    def test_username_by_css(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, AdminPage.CSS_USERNAME)))
    #

    def test_forgotten_password_by_xpath(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdminPage.XPATH_FORGOTTEN_PASSWORD)))
    #

    def test_panel_heading_by_class_name(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CLASS_NAME, AdminPage.CLASS_PANEL_HEADING)))
    #

    def test_opencart_by_link_text(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.LINK_TEXT, AdminPage.LINK_TEXT_OPENCART)))
    #

    def test_login_logout(self, browser):
        wait = WebDriverWait(driver=browser, timeout=15)
        input_username = browser.find_element_by_id(id_=AdminPage.ID_INPUT_USERNAME)
        input_username.click()
        input_username.send_keys(OpenCartConfiguration.ADMIN_USERNAME)

        input_password = browser.find_element_by_id(id_=AdminPage.ID_INPUT_PASSWORD)
        input_password.click()
        input_password.send_keys(OpenCartConfiguration.ADMIN_PASSWORD)

        login_button = browser.find_element_by_xpath(xpath=AdminPage.XPATH_LOGIN_BUTTON)
        login_button.click()
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, AdminPage.XPATH_DASHBOARD_HEADING)))

        logout_button = browser.find_element_by_xpath(xpath=AdminPage.XPATH_LOGOUT_BUTTON)
        logout_button.click()

        wait.until(EC.visibility_of_element_located(locator=(By.ID, AdminPage.ID_INPUT_PASSWORD)))
#
