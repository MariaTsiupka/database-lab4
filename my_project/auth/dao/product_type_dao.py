from models.product_type import ProductType
class ProductTypeDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_product_types(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `product_type`")
        rows = cur.fetchall()
        cur.close()
        return [ProductType(*row) for row in rows]

    def insert_product_type(self, product_type_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `product_type` (type_name, type_description) VALUES (%s, %s)",
            (product_type_data["type_name"], product_type_data["type_description"])
        )
        self.mysql.connection.commit()
        cur.close()

    def update_product_type(self, product_type_id, product_type_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE `product_type` SET type_name = %s, type_description = %s WHERE product_type_id = %s",
            (product_type_data["type_name"], product_type_data["type_description"], product_type_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_product_type(self, product_type_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `product_type` WHERE product_type_id = %s", (product_type_id,))
        self.mysql.connection.commit()
        cur.close()
