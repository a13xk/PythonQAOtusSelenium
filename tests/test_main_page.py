from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPage


class TestMainPage:

    def test_slideshow_by_id(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.ID, MainPage.ID_SLIDESHOW)))
    #

    def test_slideshow_by_css(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, MainPage.CSS_SLIDESHOW)))
    #

    def test_slideshow_by_xpath(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, MainPage.XPATH_SLIDESHOW)))
    #

    def test_slideshow_by_class_name(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CLASS_NAME, MainPage.CLASS_SLIDESHOW)))
    #

    def test_slideshow(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.LINK_TEXT, MainPage.LINK_TEXT_YOUR_STORE)))
    #
#
