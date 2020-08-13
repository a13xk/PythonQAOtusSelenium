import time


class TestSelenoidMainPage:

    def test_remote_slideshow_by_id(self, selenoid_main_page):
        time.sleep(4)
        assert selenoid_main_page.find_element(locator=selenoid_main_page.DIV_ID_SLIDESHOW)
    #
    
    def test_slideshow_by_css(self, selenoid_main_page):
        time.sleep(4)
        assert selenoid_main_page.find_element(locator=selenoid_main_page.DIV_CSS_SLIDESHOW)
    #

    def test_slideshow_by_xpath(self, selenoid_main_page):
        time.sleep(4)
        assert selenoid_main_page.find_element(locator=selenoid_main_page.DIV_XPATH_SLIDESHOW)
    #

    def test_slideshow_by_class_name(self, selenoid_main_page):
        time.sleep(4)
        assert selenoid_main_page.find_element(locator=selenoid_main_page.DIV_CLASS_SLIDESHOW)
    #

    def test_slideshow_by_link_text(self, selenoid_main_page):
        time.sleep(4)
        assert selenoid_main_page.find_element(locator=selenoid_main_page.A_YOUR_STORE)
    #
#
