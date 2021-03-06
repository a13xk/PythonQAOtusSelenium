import datetime

import mysql.connector

from configuration import BitnamiDatabase


class DBHelper:

    """
    Class encapsulating functionality to interact with Bitnami database
    """

    def __init__(self):
        self.host = BitnamiDatabase.HOST
        self.database = BitnamiDatabase.DB_NAME
        self.port = BitnamiDatabase.PORT
        self.user = BitnamiDatabase.DB_USER
        self.connection = None
        self.cursor = None
    #

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            port=self.port,
            user=self.user
        )
        self.cursor = self.connection.cursor()
    #

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
    #

    def add_new_product(self, product_info: dict):

        # 1. Insert into 'oc_product' table
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        model = product_info.get("model")
        status = product_info.get("status")
        price = product_info.get("price")
        location = product_info.get("location")
        data_oc_product = (
            model, status, price,
            "", "", "", "", "", "",
            location,
            "6", "10", "9",
            current_datetime, current_datetime, current_datetime
        )
        insert_into_oc_product = f"INSERT INTO oc_product (" \
                                 f"model,status,price," \
                                 f"sku,upc,ean,jan,isbn,mpn," \
                                 f"location," \
                                 f"stock_status_id,manufacturer_id,tax_class_id," \
                                 f"date_available,date_added,date_modified) " \
                                 f"VALUES {data_oc_product}"
        self.cursor.execute(insert_into_oc_product)
        self.connection.commit()

        # 2. Get 'product_id' from previous operation
        query_last_oc_product = f"SELECT product_id FROM oc_product WHERE model LIKE'%{model}%'"
        self.cursor.execute(query_last_oc_product)
        product_ids = [product_id[0] for product_id in self.cursor.fetchall()]
        last_id = max(product_ids)

        # 3. Insert into 'oc_product_description' table
        name = product_info.get("name")
        description = product_info.get("description")
        meta_tag_title = product_info.get("meta_tag_title")
        data_oc_product_description = (
            last_id, "1",
            name, description, meta_tag_title,
            "", "", ""
        )
        insert_into_oc_product_description = f"INSERT INTO oc_product_description (" \
                                             f"product_id,language_id," \
                                             f"name,description,meta_title," \
                                             f"tag,meta_description,meta_keyword) " \
                                             f"VALUES {data_oc_product_description}"
        self.cursor.execute(insert_into_oc_product_description)
        self.connection.commit()
    #

    def delete_product(self, product_name: str):
        query_by_product_name = f'SELECT product_id FROM oc_product_description WHERE name = "{product_name}"'
        self.cursor.execute(query_by_product_name)
        product_ids = tuple([product_id[0] for product_id in self.cursor.fetchall()])

        if product_ids:
            # Remove trailing comma if tuple contains only 1 element
            product_ids_str = str(product_ids)
            if len(product_ids) == 1:
                product_ids_str = product_ids_str.replace(",)", ")")
            delete_in_oc_product = f"DELETE FROM oc_product WHERE product_id in {product_ids_str}"
            delete_in_oc_product_description = f"DELETE FROM oc_product_description WHERE product_id in {product_ids_str}"

            self.cursor.execute(delete_in_oc_product)
            self.connection.commit()

            self.cursor.execute(delete_in_oc_product_description)
            self.connection.commit()
    #

    def check_product_added(self, product_name: str):
        # 1. Check oc_product_description table
        query_by_product_name_oc_product_description = f'SELECT product_id FROM oc_product_description WHERE name = "{product_name}"'
        self.cursor.execute(query_by_product_name_oc_product_description)
        product_ids = tuple([product_id[0] for product_id in self.cursor.fetchall()])
        assert len(product_ids) == 1

        # 2. Check oc_product table
        query_by_product_name_oc_product = f'SELECT product_id FROM oc_product WHERE product_id = "{product_ids[0]}"'
        self.cursor.execute(query_by_product_name_oc_product)
        product_ids_oc_product = tuple([product_id[0] for product_id in self.cursor.fetchall()])
        assert len(product_ids_oc_product) == 1
    #

    def check_product_deleted(self, product_id: int):
        query_oc_product_by_product_id = f"SELECT product_id FROM oc_product WHERE product_id = {product_id}"
        query_oc_product_description_by_product_id = f"SELECT product_id FROM oc_product_description WHERE product_id = {product_id}"
        self.cursor.execute(query_oc_product_by_product_id)
        assert not self.cursor.fetchall()
        self.cursor.execute(query_oc_product_description_by_product_id)
        assert not self.cursor.fetchall()
    #

    def check_product_name_changed(self, old_product_name: str, modified_product_name: str):
        # 1. Check old name is no longer available oc_product_description table
        query_old_name = f'SELECT product_id FROM oc_product_description WHERE name = "{old_product_name}"'
        self.cursor.execute(query_old_name)
        assert not self.cursor.fetchall()

        # 2. Check product is available by modified name
        query_modified_name_oc_product_description = f'SELECT product_id FROM oc_product_description WHERE name = "{modified_product_name}"'
        self.cursor.execute(query_modified_name_oc_product_description)
        product_ids = tuple([product_id[0] for product_id in self.cursor.fetchall()])
        assert len(product_ids) == 1

        query_modified_name_oc_product = f'SELECT product_id FROM oc_product WHERE product_id = "{product_ids[0]}"'
        self.cursor.execute(query_modified_name_oc_product)
        product_ids_oc_product = tuple([product_id[0] for product_id in self.cursor.fetchall()])
        assert len(product_ids_oc_product) == 1
    #
#
