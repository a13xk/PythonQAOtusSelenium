from selenium import webdriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):

    DIV_ACCOUNT_LOGIN = (By.ID, "account-login")
    INPUT_LOGIN_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")
    A_CONTINUE_BUTTON = (By.XPATH, "//div[@class='well']/a[contains(@class, 'btn')]")
    DIV_LIST_GROUP = (By.CLASS_NAME, "list-group")
    A_FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")

    def __init__(self, driver: webdriver, logging_enabled: bool, url: str = ""):
        self.driver: webdriver = driver
        if not url:
            self.url: str = "https://localhost/index.php?route=account/login"
        else:
            self.url: str = url
        super().__init__(
            driver=self.driver,
            url=self.url,
            logging_enabled=logging_enabled
        )
    #
#
