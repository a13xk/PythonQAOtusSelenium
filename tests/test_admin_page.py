from locators.admin_page import AdminPage


class TestAdminPage:

    def test_header_logo_by_id(self, browser):
        div_header_logo = browser.find_element_by_id(id_=AdminPage.ID_HEADER_LOGO)
        assert div_header_logo
    #

    def test_username_by_css(self, browser):
        label_username = browser.find_element_by_css_selector(css_selector=AdminPage.CSS_USERNAME)
        assert label_username
    #

    def test_forgotten_password_by_xpath(self, browser):
        a_forgotten_password = browser.find_element_by_xpath(xpath=AdminPage.XPATH_FORGOTTEN_PASSWORD)
        assert a_forgotten_password
    #

    def test_panel_heading_by_class_name(self, browser):
        div_panel_heading = browser.find_element_by_class_name(name=AdminPage.CLASS_PANEL_HEADING)
        assert div_panel_heading
    #

    def test_opencart_by_link_text(self, browser):
        a_opencart = browser.find_element_by_link_text(link_text=AdminPage.LINK_TEXT_OPENCART)
        assert a_opencart
    #
#
