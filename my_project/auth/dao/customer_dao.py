from ..models.customer import Customer

class CustomerDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_customers(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM customer")
        customers = cur.fetchall()
        cur.close()
        return [Customer(customer_id=row[0], customer_name=row[1], customer_surname=row[2], 
                         customer_email=row[3], customer_phone=row[4]) for row in customers]
    #Звязок 1:1
    def get_customer_with_card(self, customer_id):
        cur = self.mysql.connection.cursor()
        query = """
            SELECT c.customer_id, c.customer_name, c.customer_surname, c.customer_email, c.customer_phone,
                   cc.card_id, cc.card_number, cc.bonus_num
            FROM customer c
            LEFT JOIN customer_card cc ON c.customer_id = cc.customer_id
            WHERE c.customer_id = %s
        """
        cur.execute(query, (customer_id,))
        row = cur.fetchone()
        cur.close()

        if row:
            customer = {
                "customer_id": row[0],
                "customer_name": row[1],
                "customer_surname": row[2],
                "customer_email": row[3],
                "customer_phone": row[4]
            }
            card = {
                "card_id": row[5],
                "card_number": row[6],
                "bonus_num": row[7]
            } if row[5] else None
            return {"customer": customer, "card": card}
        return None

    def get_customer_by_id(self, customer_id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))
        row = cur.fetchone()
        cur.close()
        return Customer(customer_id=row[0], customer_name=row[1], customer_surname=row[2], 
                        customer_email=row[3], customer_phone=row[4]) if row else None

    def insert_customer(self, customer):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO customer (customer_name, customer_surname, customer_email, customer_phone) VALUES (%s, %s, %s, %s)",
            (customer['customer_name'], customer['customer_surname'], customer['customer_email'], customer['customer_phone'])
        )
        self.mysql.connection.commit()
        cur.close()

    def update_customer(self, customer_id, customer):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE customer SET customer_name = %s, customer_surname = %s, customer_email = %s, customer_phone = %s WHERE customer_id = %s",
            (customer['customer_name'], customer['customer_surname'], customer['customer_email'], customer['customer_phone'], customer_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_customer(self, customer_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
        self.mysql.connection.commit()
        cur.close()
