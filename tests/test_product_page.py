from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.product_page import ProductPage


class TestProductPage:

    def test_product_product_by_id(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.ID, ProductPage.ID_PRODUCT_PRODUCT)))
    #

    def test_a_thumbnail_by_css(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CSS_SELECTOR, ProductPage.CSS_A_THUMBNAIL)))
    #

    def test_add_to_wish_list_button_by_xpath(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.XPATH, ProductPage.XPATH_ADD_TO_WISHLIST_BUTTON)))
    #

    def test_add_to_cart_button_by_class_name(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.CLASS_NAME, ProductPage.CLASS_ADD_TO_CART_BUTTON)))
    #

    def test_reviews_by_partial_link_text(self, browser):
        wait = WebDriverWait(driver=browser, timeout=5)
        wait.until(EC.visibility_of_element_located(locator=(By.PARTIAL_LINK_TEXT, ProductPage.PARTIAL_LINK_TEXT_REVIEWS)))
    #
#

