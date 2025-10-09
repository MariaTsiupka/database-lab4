from models.delivery import Delivery

class DeliveryDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_deliveries(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `delivery`")
        rows = cur.fetchall()
        cur.close()
        return [Delivery(*row) for row in rows]

    def insert_delivery(self, delivery_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `delivery` (order_id, city_id, delivery_method, delivery_address) VALUES (%s, %s, %s, %s)",
            (delivery_data["order_id"], delivery_data["city_id"], delivery_data["delivery_method"], delivery_data["delivery_address"])
        )
        self.mysql.connection.commit()
        cur.close()

    def update_delivery(self, delivery_id, delivery_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE `delivery` SET order_id = %s, city_id = %s, delivery_method = %s, delivery_address = %s WHERE delivery_id = %s",
            (delivery_data["order_id"], delivery_data["city_id"], delivery_data["delivery_method"], delivery_data["delivery_address"], delivery_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_delivery(self, delivery_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `delivery` WHERE delivery_id = %s", (delivery_id,))
        self.mysql.connection.commit()
        cur.close()
