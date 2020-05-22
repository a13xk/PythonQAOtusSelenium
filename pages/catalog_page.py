from selenium.webdriver.common.by import By

from .base_page import BasePage


class CatalogPage(BasePage):

    DIV_PRODUCT_CATEGORY = (By.ID, "product-category")
    IMG_THUMBNAIL = (By.CSS_SELECTOR, ".img-thumbnail")
    LABEL_SORT_BY = (By.XPATH, "//div[contains(@class, 'form-group') and contains(@class, 'input-group')]/label[@for='input-sort']")
    UL_BREADCRUMB = (By.CLASS_NAME, "breadcrumb")
    A_PRODUCT_COMPARE = (By.PARTIAL_LINK_TEXT, "Product Compare")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://localhost/index.php?route=product/category&path=20"
        super().__init__(driver=self.driver, url=self.url)
    #
#
