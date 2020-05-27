class TestLoginPage:

    def test_account_login_by_id(self, login_page):
        assert login_page.find_element(locator=login_page.DIV_ACCOUNT_LOGIN)
    #

    def test_button_login_by_css(self, login_page):
        assert login_page.find_element(locator=login_page.INPUT_LOGIN_BUTTON)
    #

    def test_continue_button_by_xpath(self, login_page):
        assert login_page.find_element(locator=login_page.A_CONTINUE_BUTTON)
    #

    def test_list_group_by_class_name(self, login_page):
        assert login_page.find_element(locator=login_page.DIV_LIST_GROUP)
    #

    def test_forgotten_password_by_link_text(self, login_page):
        assert login_page.find_element(locator=login_page.A_FORGOTTEN_PASSWORD)
    #
#
