class AdministrationPage:
    XPATH_DASHBOARD_HEADING = "//div[@id='content']//h1[contains(text(), 'Dashboard')]"
    XPATH_LOGOUT_BUTTON = "//a[contains(@href, 'logout')]"
    XPATH_MENU_CATALOG = "//li[@id='menu-catalog']//a[@href='#collapse1']"
    XPATH_CATALOG_PRODUCTS_LINK = "//a[contains(@href, 'catalog/product') and contains(text(), 'Products')]"
    XPATH_PRODUCTS_TABLE = "//form[@id='form-product']//table"
    XPATH_ADD_NEW_BUTTON = "//a[@data-original-title='Add New']"
    XPATH_DELETE_BUTTON = "//button[@data-original-title='Delete']"
    XPATH_DISMISS_ALERT = "//button[@data-dismiss='alert']"
#
