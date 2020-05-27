class TestMainPage:

    def test_slideshow_by_id(self, main_page):
        assert main_page.find_element(locator=main_page.DIV_ID_SLIDESHOW)
    #

    def test_slideshow_by_css(self, main_page):
        assert main_page.find_element(locator=main_page.DIV_CSS_SLIDESHOW)
    #

    def test_slideshow_by_xpath(self, main_page):
        assert main_page.find_element(locator=main_page.DIV_XPATH_SLIDESHOW)
    #

    def test_slideshow_by_class_name(self, main_page):
        assert main_page.find_element(locator=main_page.DIV_CLASS_SLIDESHOW)
    #

    def test_slideshow_by_link_text(self, main_page):
        assert main_page.find_element(locator=main_page.A_YOUR_STORE)
    #
#
