import pytest


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
#
