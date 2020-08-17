import allure

from configuration import OpenCart
from pages.administration_page import AdministrationPage


class TestAdminLoginPage:
    @allure.title("Check logo image")
    @allure.feature("Check elements before logging in")
    @allure.story("Logo")
    def test_header_logo(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.IMG_LOGO)

    #

    @allure.title("Check username input label")
    @allure.feature("Check elements before logging in")
    @allure.story("Labels")
    def test_username_label(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.LABEL_FOR_USERNAME)
    #

    @allure.title("Check restore forgotten password link by XPath")
    @allure.feature("Check elements before logging in")
    @allure.story("Links")
    def test_forgotten_password_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_FORGOTTEN_PASSWORD)
    #

    @allure.title('Check "Please enter your login details." heading')
    @allure.feature("Check elements before logging in")
    @allure.story("Labels")
    def test_panel_heading(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.DIV_PANEL_HEADING)
    #

    @allure.title("Check OpenCart hyperlink")
    @allure.feature("Check elements before logging in")
    @allure.story("Links")
    def test_opencart_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_OPENCART)
    #

    @allure.title("Log in to administration page and then log out")
    @allure.feature("Check elements after logging in")
    @allure.story("Links")
    def test_login_logout(self, admin_login_page, browser, base_class_logging):

        @allure.step("Log in to administration page")
        def log_in(_admin_login_page):
            _admin_login_page.log_in(
                username=OpenCart.ADMIN_USERNAME,
                password=OpenCart.ADMIN_PASSWORD
            )

        @allure.step("Check administration page")
        def check_administration_page(_browser, _logging):
            _administration_page = AdministrationPage(driver=_browser, logging_enabled=_logging)
            assert _administration_page.find_element(locator=_administration_page.DIV_DASHBOARD)
            return _administration_page

        @allure.step("Log out")
        def log_out(_ap):
            _ap.log_out()

        log_in(admin_login_page)
        administration_page = check_administration_page(browser, base_class_logging)
        log_out(administration_page)

    #
#
