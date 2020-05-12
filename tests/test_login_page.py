from locators.login_page import LoginPage


class TestLoginPage:

    def test_account_login_by_id(self, browser):
        div_account_login = browser.find_element_by_id(id_=LoginPage.ID_ACCOUNT_LOGIN)
        assert div_account_login
    #

    def test_button_login_by_css(self, browser):
        button_login = browser.find_element_by_css_selector(css_selector=LoginPage.CSS_BUTTON_LOGIN)
        assert button_login
    #

    def test_continue_button_by_xpath(self, browser):
        button_continue = browser.find_element_by_xpath(xpath=LoginPage.XPATH_CONTINUE_BUTTON)
        assert button_continue
    #

    def test_list_group_by_class_name(self, browser):
        div_list_group = browser.find_element_by_class_name(name=LoginPage.CLASS_LIST_GROUP)
        assert div_list_group
    #

    def test_forgotten_password_by_link_text(self, browser):
        a_forgotten_password = browser.find_element_by_link_text(link_text=LoginPage.LINK_TEXT_FORGOTTEN_PASSWORD)
        assert a_forgotten_password
    #
#
