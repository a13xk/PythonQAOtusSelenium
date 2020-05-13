from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
#
