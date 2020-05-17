from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.catalog_page import CatalogPage


class TestCatalogPage:

    def test_product_category_by_id(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.ID, CatalogPage.ID_PRODUCT_CATEGORY)))
    #

    def test_img_thumbnail_by_css(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, CatalogPage.CSS_IMG_THUMBNAIL)))
    #

    def test_sort_by_label_by_xpath(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, CatalogPage.XPATH_SORT_BY_LABEL)))
    #

    def test_breadcrumb_by_class_name(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CLASS_NAME, CatalogPage.CLASS_BREADCRUMB)))
    #

    def test_product_compare_by_partial_link_text(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.PARTIAL_LINK_TEXT, CatalogPage.PARTIAL_LINK_TEXT_PRODUCT_COMPARE)))
    #
#
