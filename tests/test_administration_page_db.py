import pytest
from selenium.webdriver.common.by import By


class TestAdministrationPageDB:

    @pytest.mark.usefixtures("db_delete_product")
    def test_db_add_new_product(self, catalog_products_page, product_data, db):
        catalog_products_page.add_product(
            product_name=product_data.get("name"),
            meta_tag_title=product_data.get("meta_tag_title"),
            model=product_data.get("model")
        )
        div_alert_success = catalog_products_page.find_element(locator=catalog_products_page.DIV_ALERT_SUCCESS)
        assert "Success: You have modified products!" in div_alert_success.get_property(name="innerHTML")

        # Check product added in database
        db.check_product_added(product_name=product_data.get("name"))
    #

    @pytest.mark.usefixtures("db_add_new_product")
    def test_db_delete_product(self, catalog_products_page, product_data, db):
        deleted_product_id = catalog_products_page.delete_product(product_name=product_data.get("name"))
        all_input_checkboxes = catalog_products_page.find_elements(locator=catalog_products_page.INPUT_CHECKBOX)
        assert all(checkbox.get_attribute("value") != deleted_product_id for checkbox in all_input_checkboxes)

        # Check product deleted from database
        db.check_product_deleted(product_id=deleted_product_id)
    #

    @pytest.mark.usefixtures("db_add_new_product")
    def test_db_edit_product(self, catalog_products_page, product_data, db):
        old_product_name = product_data.get("name")
        modified_product_name = product_data.get("modified_name")
        modified_product_id = catalog_products_page.edit_product(
            product_name=old_product_name,
            modified_product_name=modified_product_name
        )
        all_input_checkboxes = catalog_products_page.find_elements(locator=catalog_products_page.INPUT_CHECKBOX)
        assert any(checkbox.get_attribute("value") == modified_product_id for checkbox in all_input_checkboxes)
        assert catalog_products_page.find_element(locator=(By.XPATH, f"//td[contains(text(), '{modified_product_name}')]"))

        # Check product modified in database
        db.check_product_name_changed(old_product_name=old_product_name, modified_product_name=modified_product_name)
    #
#
