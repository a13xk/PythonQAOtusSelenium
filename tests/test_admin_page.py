import pytest
from selenium.webdriver.common.by import By


class TestAdministrationPage:

    def test_browse_to_catalog_products_table(self, administration_page):
        administration_page.open_catalog()
        administration_page.find_element(locator=administration_page.A_MENU_CATALOG_PRODUCTS).click()
        assert administration_page.find_element(locator=administration_page.TABLE_PRODUCTS)
    #

    def test_add_new_product(self, catalog_products_page, product_info):
        catalog_products_page.add_product(
            product_name=product_info.get("product_name"),
            meta_tag_title=product_info.get("meta_tag_title"),
            model=product_info.get("model")
        )
        div_alert_success = catalog_products_page.find_element(locator=catalog_products_page.DIV_ALERT_SUCCESS)
        assert "Success: You have modified products!" in div_alert_success.get_property(name="innerHTML")
    #

    @pytest.mark.usefixtures("add_new_product")
    def test_delete_product(self, catalog_products_page, product_info):
        deleted_product_id = catalog_products_page.delete_product(product_name=product_info.get("product_name"))
        all_input_checkboxes = catalog_products_page.find_elements(locator=catalog_products_page.INPUT_CHECKBOX)
        assert all(checkbox.get_attribute("value") != deleted_product_id for checkbox in all_input_checkboxes)
    #

    @pytest.mark.usefixtures("add_new_product")
    def test_edit_product(self, catalog_products_page, product_info):
        old_product_name = product_info.get("product_name")
        modified_product_name = product_info.get("modified_product_name")
        modified_product_id = catalog_products_page.edit_product(
            product_name=old_product_name,
            modified_product_name=modified_product_name
        )
        all_input_checkboxes = catalog_products_page.find_elements(locator=catalog_products_page.INPUT_CHECKBOX)
        assert any(checkbox.get_attribute("value") == modified_product_id for checkbox in all_input_checkboxes)
        assert catalog_products_page.find_element(locator=(By.XPATH, f"//td[contains(text(), '{modified_product_name}')]"))
    #
#
