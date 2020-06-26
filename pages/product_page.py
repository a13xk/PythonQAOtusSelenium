from selenium import webdriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class ProductPage(BasePage):

    DIV_PRODUCT_PRODUCT = (By.ID, "product-product")
    A_THUMBNAIL = (By.CSS_SELECTOR, ".thumbnail")
    BUTTON_ADD_TO_WISH_LIST = (By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-default') and contains(@data-original-title, 'Add to Wish List')]")
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn.btn-primary.btn-lg.btn-block")
    A_REVIEWS = (By.PARTIAL_LINK_TEXT, "Reviews ")

    def __init__(self, driver: webdriver, url: str, logging_enabled: bool):
        self.driver: webdriver = driver
        if not url:
            self.url: str = "https://localhost/index.php?route=product/product&path=57&product_id=49"
        else:
            self.url = url
        super().__init__(
            driver=self.driver,
            url=self.url,
            logging_enabled=logging_enabled
        )
    #
#
