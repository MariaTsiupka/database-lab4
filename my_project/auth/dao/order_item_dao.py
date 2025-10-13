from ..models.order_item import OrderItem

class OrderItemDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_order_items(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `order_item`")
        rows = cur.fetchall()
        cur.close()
        return [OrderItem(order_item_id=row[0], order_id=row[1], product_id=row[2], quantity=row[3]) for row in rows]

    def insert_order_item(self, order_item_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `order_item` (order_id, product_id, quantity) VALUES (%s, %s, %s)",
            (order_item_data["order_id"], order_item_data["product_id"], order_item_data["quantity"])
        )
        self.mysql.connection.commit()
        cur.close()

    def update_order_item(self, order_item_id, order_item_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE `order_item` SET order_id = %s, product_id = %s, quantity = %s WHERE order_item_id = %s",
            (order_item_data["order_id"], order_item_data["product_id"], order_item_data["quantity"], order_item_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_order_item(self, order_item_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `order_item` WHERE order_item_id = %s", (order_item_id,))
        self.mysql.connection.commit()
        cur.close()
