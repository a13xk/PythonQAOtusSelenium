from selenium import webdriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class AdminLoginPage(BasePage):

    IMG_LOGO = (By.ID, "header-logo")
    INPUT_USERNAME = (By.ID, "input-username")
    INPUT_PASSWORD = (By.ID, "input-password")
    A_FORGOTTEN_PASSWORD = (By.XPATH, "//div[@class='form-group']/span/a")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit' and contains(text(), 'Login')]")
    LABEL_FOR_USERNAME = (By.CSS_SELECTOR, "label[for='input-username']")
    DIV_PANEL_HEADING = (By.CLASS_NAME, "panel-heading")
    A_OPENCART = (By.LINK_TEXT, "OpenCart")

    def __init__(self, driver: webdriver, url: str, logging_enabled: bool):
        self.driver: webdriver = driver
        if not url:
            self.url: str = "https://localhost/admin"
        else:
            self.url: str = url
        self.timeout: int = 15
        super().__init__(
            driver=self.driver,
            url=self.url,
            timeout=self.timeout,
            logging_enabled=logging_enabled
        )
    #

    def _set_username_(self, username: str):
        self.find_element(locator=self.INPUT_USERNAME).clear()
        self.find_element(locator=self.INPUT_USERNAME).send_keys(username)
    #

    def _set_password_(self, password: str):
        self.find_element(locator=self.INPUT_PASSWORD).clear()
        self.find_element(locator=self.INPUT_PASSWORD).send_keys(password)
    #

    def log_in(self, username: str, password: str):
        self._set_username_(username=username)
        self._set_password_(password=password)
        self.find_element(locator=self.BUTTON_LOGIN).click()
    #
#
