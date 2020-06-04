from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,
                 driver: webdriver,
                 url: str = "",
                 timeout: int = 10):
        self.driver: webdriver = driver
        if not url:
            self.url: str = "https://localhost"
        else:
            self.url: str = url
        self.timeout: int = timeout
    #

    def find_element(self, locator):
        return WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            method=EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
    #

    def find_elements(self, locator):
        return WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            method=EC.visibility_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )
    #

    def open_page(self):
        return self.driver.get(url=self.url)
    #
#
