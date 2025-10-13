from ..models.customer_card import CustomerCard


class CustomerCardDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_cards(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM customer_card")
        rows = cur.fetchall()
        cur.close()
        return [
            CustomerCard(
                card_id=row[0],
                customer_id=row[1],
                card_number=row[2],
                bonus_num=row[3]
            )
            for row in rows
        ]

    def insert_card(self, card_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
        "INSERT INTO customer_card (customer_id, card_number, bonus_num) VALUES (%s, %s, %s)",
        (card_data["customer_id"], card_data["card_number"], card_data.get("bonus_num", 0)),
    )
        self.mysql.connection.commit()
        cur.close()

    def update_card(self, card_id, card_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
        "UPDATE customer_card SET customer_id = %s, card_number = %s, bonus_num = %s WHERE card_id = %s",
        (card_data["customer_id"], card_data["card_number"], card_data["bonus_num"], card_id),
    )
        self.mysql.connection.commit()
        cur.close()


    def delete_card(self, card_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM customer_card WHERE card_id = %s", (card_id,))
        self.mysql.connection.commit()
        cur.close()
