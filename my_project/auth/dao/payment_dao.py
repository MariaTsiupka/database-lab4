from my_project.auth.models.payment import Payment

class PaymentDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_payments(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `payment`")
        rows = cur.fetchall()
        cur.close()
        return [Payment(*row) for row in rows]

    def insert_payment(self, payment_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `payment` (order_id, payment_method, payment_status) VALUES (%s, %s, %s)",
            (payment_data["order_id"], payment_data["payment_method"], payment_data["payment_status"])
        )
        self.mysql.connection.commit()
        cur.close()

    def update_payment(self, payment_id, payment_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE `payment` SET order_id = %s, payment_method = %s, payment_status = %s WHERE payment_id = %s",
            (payment_data["order_id"], payment_data["payment_method"], payment_data["payment_status"], payment_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_payment(self, payment_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `payment` WHERE payment_id = %s", (payment_id,))
        self.mysql.connection.commit()
        cur.close()
