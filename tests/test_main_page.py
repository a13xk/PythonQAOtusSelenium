from locators import MainPage


class TestMainPage:

    def test_slideshow_by_id(self, browser):
        div_slideshow = browser.find_element_by_id(id_=MainPage.ID_SLIDESHOW)
        assert div_slideshow
    #

    def test_slideshow_by_css(self, browser):
        div_slideshow = browser.find_element_by_css_selector(css_selector=MainPage.CSS_SLIDESHOW)
        assert div_slideshow
    #

    def test_slideshow_by_xpath(self, browser):
        div_slideshow = browser.find_element_by_xpath(xpath=MainPage.XPATH_SLIDESHOW)
        assert div_slideshow
    #

    def test_slideshow_by_class_name(self, browser):
        div_slideshow = browser.find_element_by_class_name(name=MainPage.CLASS_SLIDESHOW)
        assert div_slideshow
    #

    def test_slideshow(self, browser):
        h1_your_store = browser.find_element_by_link_text(link_text=MainPage.LINK_TEXT_YOUR_STORE)
        assert h1_your_store
    #
#
