import allure

from configuration import OpenCart
from pages.administration_page import AdministrationPage


class TestAdminLoginPage:

    @allure.title("Check logo image")
    def test_header_logo(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.IMG_LOGO)
    #

    @allure.title("Check username input label")
    def test_username_label(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.LABEL_FOR_USERNAME)
    #

    @allure.title("Check restore forgotten password link by XPath")
    def test_forgotten_password_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_FORGOTTEN_PASSWORD)
    #

    @allure.title('Check "Please enter your login details." heading')
    def test_panel_heading(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.DIV_PANEL_HEADING)
    #

    @allure.title("Check OpenCart hyperlink")
    def test_opencart_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_OPENCART)
    #

    @allure.title("Log in to administration page and then log out")
    def test_login_logout(self, admin_login_page, browser, base_class_logging):
        admin_login_page.log_in(
            username=OpenCart.ADMIN_USERNAME,
            password=OpenCart.ADMIN_PASSWORD
        )
        administration_page = AdministrationPage(driver=browser, logging_enabled=base_class_logging)
        assert administration_page.find_element(locator=administration_page.DIV_DASHBOARD)
        administration_page.log_out()
    #
#
