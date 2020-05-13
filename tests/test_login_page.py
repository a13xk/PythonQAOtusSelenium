from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page import LoginPage


class TestLoginPage:

    def test_account_login_by_id(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.ID, LoginPage.ID_ACCOUNT_LOGIN)))
    #

    def test_button_login_by_css(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, LoginPage.CSS_BUTTON_LOGIN)))
    #

    def test_continue_button_by_xpath(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, LoginPage.XPATH_CONTINUE_BUTTON)))
    #

    def test_list_group_by_class_name(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CLASS_NAME, LoginPage.CLASS_LIST_GROUP)))
    #

    def test_forgotten_password_by_link_text(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.LINK_TEXT, LoginPage.LINK_TEXT_FORGOTTEN_PASSWORD)))
    #
#
