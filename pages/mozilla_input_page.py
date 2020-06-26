from selenium import webdriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class MozillaInputPage(BasePage):

    FRAME_BASIC_EXAMPLE = (By.ID, "frame_A_basic_example")
    INPUT_ID_FILE = (By.XPATH, "//input[@id='file']")
    BUTTON_SUBMIT = (By.XPATH, "//input[@id='file']/parent::div/parent::form/div/button")

    def __init__(self, driver: webdriver, url: str):
        self.driver: webdriver = driver
        if not url:
            self.url: str = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input/file"
        else:
            self.url: str = url
        super().__init__(driver=self.driver, url=self.url)
    #
#
