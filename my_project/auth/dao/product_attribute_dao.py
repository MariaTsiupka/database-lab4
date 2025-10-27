from my_project.auth.models.product_attribute import ProductAttribute

class ProductAttributeDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_attributes(self, product_id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `product_attribute` WHERE product_id = %s", (product_id,))
        rows = cur.fetchall()
        cur.close()
        return [ProductAttribute(*row) for row in rows]

    def insert_attribute(self, attribute_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `product_attribute` (product_id, attribute_name, attribute_value) VALUES (%s, %s, %s)",
            (attribute_data["product_id"], attribute_data["attribute_name"], attribute_data["attribute_value"])
        )
        self.mysql.connection.commit()
        cur.close()

    def update_attribute(self, attribute_id, attribute_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE `product_attribute` SET attribute_name = %s, attribute_value = %s WHERE attribute_id = %s",
            (attribute_data["attribute_name"], attribute_data["attribute_value"], attribute_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_attribute(self, attribute_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `product_attribute` WHERE attribute_id = %s", (attribute_id,))
        self.mysql.connection.commit()
        cur.close()
