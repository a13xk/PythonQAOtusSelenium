from typing import Union

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.opera.webdriver import WebDriver as OperaWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,
                 driver: Union[ChromeWebDriver, FirefoxWebDriver, OperaWebDriver],
                 url: str = "",
                 timeout: int = 10):
        self.driver: Union[ChromeWebDriver, FirefoxWebDriver, OperaWebDriver] = driver
        if not url:
            self.url: str = "https://localhost"
        else:
            self.url = url
        self.timeout = timeout
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
