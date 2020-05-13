class AdminLoginPage:
    ID_HEADER_LOGO = "header-logo"
    ID_INPUT_USERNAME = "input-username"
    ID_INPUT_PASSWORD = "input-password"
    CSS_USERNAME = "label[for='input-username']"
    XPATH_FORGOTTEN_PASSWORD = "//div[@class='form-group']/span/a"
    XPATH_LOGIN_BUTTON = "//button[@type='submit' and contains(text(), 'Login')]"
    XPATH_DASHBOARD_HEADING = "//div[@id='content']//h1[contains(text(), 'Dashboard')]"
    XPATH_LOGOUT_BUTTON = "//a[contains(@href, 'logout')]"
    CLASS_PANEL_HEADING = "panel-heading"
    LINK_TEXT_OPENCART = "OpenCart"
#
