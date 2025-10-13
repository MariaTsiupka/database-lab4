from ..models.order import Order  # Імпортуємо клас Order
from datetime import datetime

class OrderDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_orders(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `order`")
        rows = cur.fetchall()
        cur.close()
        return [Order(order_id=row[0], customer_id=row[1], order_date=row[2]) for row in rows]

    def get_orders_by_customer_id(self, customer_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT o.order_id, o.customer_id, o.order_date, 
                   c.customer_name, c.customer_surname, c.customer_email, c.customer_phone
            FROM `order` o
            JOIN customer c ON o.customer_id = c.customer_id
            WHERE o.customer_id = %s
        """, (customer_id,))
        rows = cur.fetchall()
        cur.close()
        return [
            {
                "order_id": row[0],
                "customer_id": row[1],
                "order_date": row[2],
                "customer_name": row[3],
                "customer_surname": row[4],
                "customer_email": row[5],
                "customer_phone": row[6]
            }
            for row in rows
        ]

    def insert_order(self, order_data):
        cur = self.mysql.connection.cursor()

        # Перетворюємо дату в правильний формат
        order_date = datetime.strptime(order_data["order_date"], '%a, %d %b %Y %H:%M:%S GMT')
        formatted_date = order_date.strftime('%Y-%m-%d %H:%M:%S')  # Форматуємо у формат MySQL

        cur.execute(
            "INSERT INTO `order` (customer_id, order_date) VALUES (%s, %s)",
            (order_data["customer_id"], formatted_date)
        )
        self.mysql.connection.commit()
        cur.close()

    def update_order(self, order_id, order_data):
        cur = self.mysql.connection.cursor()

        # Перетворюємо дату в правильний формат
        order_date = datetime.strptime(order_data["order_date"], '%a, %d %b %Y %H:%M:%S GMT')
        formatted_date = order_date.strftime('%Y-%m-%d %H:%M:%S')

        cur.execute(
            "UPDATE `order` SET customer_id = %s, order_date = %s WHERE order_id = %s",
            (order_data["customer_id"], formatted_date, order_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_order(self, order_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `order` WHERE order_id = %s", (order_id,))
        self.mysql.connection.commit()
        cur.close()
