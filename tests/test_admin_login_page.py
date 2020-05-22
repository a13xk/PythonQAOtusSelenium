from configuration import OpenCart
from pages.administration_page import AdministrationPage


class TestAdminLoginPage:

    def test_header_logo(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.IMG_LOGO)
    #

    def test_username_label(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.LABEL_FOR_USERNAME)
    #

    def test_forgotten_password_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_FORGOTTEN_PASSWORD)
    #

    def test_panel_heading(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.DIV_PANEL_HEADING)
    #

    def test_opencart_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_OPENCART)
    #

    def test_login_logout(self, admin_login_page, browser):
        admin_login_page.log_in(
            username=OpenCart.ADMIN_USERNAME,
            password=OpenCart.ADMIN_PASSWORD
        )
        administration_page = AdministrationPage(driver=browser)
        assert administration_page.find_element(locator=administration_page.DIV_DASHBOARD)
        administration_page.log_out()
    #
#
