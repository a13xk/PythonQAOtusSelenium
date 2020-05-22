from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class AdministrationPage(BasePage):

    """Locators: Common """
    A_LOGOUT = (By.XPATH, "//a[contains(@href, 'logout')]")
    DIV_DASHBOARD = (By.XPATH, "//div[@id='content']//h1[contains(text(), 'Dashboard')]")

    """ Locators: Catalog pane"""
    A_MENU_CATALOG = (By.XPATH, "//li[@id='menu-catalog']//a[@href='#collapse1']")
    A_MENU_CATALOG_PRODUCTS = (By.XPATH, "//a[contains(@href, 'catalog/product') and contains(text(), 'Products')]")
    A_ADD_NEW = (By.XPATH, "//a[@data-original-title='Add New']")

    """ Locators: Products table """
    TABLE_PRODUCTS = (By.XPATH, "//form[@id='form-product']//table")
    FORM_PRODUCT = (By.ID, "form-product")
    INPUT_PRODUCT_NAME = (By.ID, "input-name1")
    INPUT_META_TAG_TITLE = (By.ID, "input-meta-title1")
    A_DATA_TAB = (By.XPATH, "//a[@href='#tab-data']")
    DIV_DATA_TAB = (By.ID, "tab-data")
    INPUT_MODEL = (By.ID, "input-model")
    BUTTON_SAVE = (By.XPATH, "//button[@data-original-title='Save']")
    BUTTON_DELETE = (By.XPATH, "//button[@data-original-title='Delete']")
    DIV_ALERT_SUCCESS = (By.CSS_SELECTOR, "div.alert.alert-success")
    BUTTON_DISMISS_ALERT = (By.XPATH, "//button[@data-dismiss='alert']")
    INPUT_CHECKBOX = (By.XPATH, "//tbody//tr/td[1]/input")

    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://localhost/admin/index.php?route=common/dashboard"
        super().__init__(driver=self.driver, url=self.URL)
    #

    def log_out(self):
        self.find_element(locator=self.A_LOGOUT).click()
    #

    def open_catalog(self):
        self.find_element(locator=self.A_MENU_CATALOG).click()
    #

    def open_catalog_products(self):
        self.open_catalog()
        self.find_element(locator=self.A_MENU_CATALOG_PRODUCTS).click()
    #

    def add_product(self, product_name: str, meta_tag_title: str, model: str):
        self.find_element(locator=self.A_ADD_NEW).click()
        self.find_element(locator=self.FORM_PRODUCT)

        input_product_name = self.find_element(locator=self.INPUT_PRODUCT_NAME)
        input_product_name.clear()
        input_product_name.send_keys(product_name)

        input_meta_tag_title = self.find_element(locator=self.INPUT_META_TAG_TITLE)
        input_meta_tag_title.clear()
        input_meta_tag_title.send_keys(meta_tag_title)

        self.find_element(locator=self.A_DATA_TAB).click()
        self.find_element(locator=self.DIV_DATA_TAB)

        input_model = self.find_element(locator=self.INPUT_MODEL)
        input_model.clear()
        input_model.send_keys(model)

        self.find_element(locator=self.BUTTON_SAVE).click()
    #

    @property
    def soup(self) -> BeautifulSoup:
        page_html = self.driver.page_source
        return BeautifulSoup(markup=page_html, features='html.parser')
    #

    def _get_product_id_by_name(self, product_name: str) -> str:
        product_table_soup = self.soup.find(name="table")
        product_id = ""
        rows = product_table_soup.find_all(name="tr")
        for row in rows:
            tds = row.find_all(name="td")
            if tds[2].text == product_name:
                product_id = tds[0].find(name="input").get("value")
                break
        return product_id
    #

    def delete_product(self, product_name: str) -> str:
        """
        Delete product by specified name and return its id
        """
        product_id = self._get_product_id_by_name(product_name=product_name)
        if product_id:
            self.find_element(locator=(By.XPATH, f"//input[@value='{product_id}']")).click()

            self.find_element(locator=self.BUTTON_DELETE).click()
            wait = WebDriverWait(driver=self.driver, timeout=5)
            wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()

        return product_id
    #

    def edit_product(self, product_name: str, modified_product_name: str) -> str:
        """
        Edit product name and return its id
        """
        product_id = self._get_product_id_by_name(product_name=product_name)
        if product_id:
            self.find_element(locator=(By.XPATH, f"//a[contains(@href, 'product_id={product_id}')]")).click()

            self.find_element(locator=self.FORM_PRODUCT)
            input_product_name = self.find_element(locator=self.INPUT_PRODUCT_NAME)
            input_product_name.clear()
            input_product_name.send_keys(modified_product_name)

            self.find_element(locator=self.BUTTON_SAVE).click()
            self.find_element(locator=self.BUTTON_DISMISS_ALERT).click()
        return product_id
    #
#
