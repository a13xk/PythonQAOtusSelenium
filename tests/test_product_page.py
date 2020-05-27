class TestProductPage:

    def test_product_product_by_id(self, product_page):
        assert product_page.find_element(locator=product_page.DIV_PRODUCT_PRODUCT)
    #

    def test_a_thumbnail_by_css(self, product_page):
        assert product_page.find_element(locator=product_page.A_THUMBNAIL)
    #

    def test_add_to_wish_list_button_by_xpath(self, product_page):
        assert product_page.find_element(locator=product_page.BUTTON_ADD_TO_WISH_LIST)
    #

    def test_add_to_cart_button_by_class_name(self, product_page):
        assert product_page.find_element(locator=product_page.BUTTON_ADD_TO_CART)
    #

    def test_reviews_by_partial_link_text(self, product_page):
        assert product_page.find_element(locator=product_page.A_REVIEWS)
    #
#

