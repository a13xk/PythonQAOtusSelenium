class TestRemoteBrowserstackMainPage:

    def test_remote_slideshow_by_id(self, remote_browserstack_main_page):
        assert remote_browserstack_main_page.find_element(locator=remote_browserstack_main_page.DIV_ID_SLIDESHOW)
    #

    def test_slideshow_by_css(self, remote_browserstack_main_page):
        assert remote_browserstack_main_page.find_element(locator=remote_browserstack_main_page.DIV_CSS_SLIDESHOW)
    #

    def test_slideshow_by_xpath(self, remote_browserstack_main_page):
        assert remote_browserstack_main_page.find_element(locator=remote_browserstack_main_page.DIV_XPATH_SLIDESHOW)
    #

    def test_slideshow_by_class_name(self, remote_browserstack_main_page):
        assert remote_browserstack_main_page.find_element(locator=remote_browserstack_main_page.DIV_CLASS_SLIDESHOW)
    #

    def test_slideshow_by_link_text(self, remote_browserstack_main_page):
        assert remote_browserstack_main_page.find_element(locator=remote_browserstack_main_page.A_YOUR_STORE)
    #
#
