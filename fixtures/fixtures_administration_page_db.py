import pytest
from db.db_helper import DBHelper


@pytest.fixture(scope="function")
def product_data() -> dict:
    """
    Product data for SQL queries
    """
    return {
        "name": "A New Product",
        "modified_name": "A Modified Product",
        "meta_tag_title": "New meta tag",
        "model": "Test model DB",
        "status": 1,
        "price": 123.456,
        "location": "Kazan",
        "description": "New product created using SQL query from Python code"
    }
#


@pytest.fixture(scope="function")
def db():
    db = DBHelper()
    db.connect()
    yield db
    db.disconnect()
#


@pytest.fixture(scope="function")
def db_delete_product(db, product_data):
    db.delete_product(product_name=product_data.get("name"))
#


@pytest.fixture(scope="function")
def db_add_new_product(db, product_data):
    db.delete_product(product_name=product_data.get("name"))
    db.delete_product(product_name=product_data.get("modified_name"))
    db.add_new_product(product_info=product_data)
#
