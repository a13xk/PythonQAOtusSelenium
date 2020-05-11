from locators.product_page import ProductPage


class TestProductPage:

    def test_product_product_by_id(self, browser):
        div_product_product = browser.find_element_by_id(id_=ProductPage.ID_PRODUCT_PRODUCT)
        assert div_product_product
    #

    def test_a_thumbnail_by_css(self, browser):
        a_thumbnail = browser.find_element_by_css_selector(css_selector=ProductPage.CSS_A_THUMBNAIL)
        assert a_thumbnail
    #

    def test_add_to_wish_list_button_by_xpath(self, browser):
        button_add_to_wish_list = browser.find_element_by_xpath(xpath=ProductPage.XPATH_ADD_TO_WISHLIST_BUTTON)
        assert button_add_to_wish_list
    #

    def test_add_to_cart_button_by_class_name(self, browser):
        button_add_to_cart = browser.find_element_by_class_name(name=ProductPage.CLASS_ADD_TO_CART_BUTTON)
        assert button_add_to_cart
    #

    def test_reviews_by_partial_link_text(self, browser):
        a_reviews = browser.find_element_by_partial_link_text(link_text=ProductPage.PARTIAL_LINK_TEXT_REVIEWS)
        assert a_reviews
    #
#

