from models.review import Review

class ReviewDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_reviews(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `reviews`")
        rows = cur.fetchall()
        cur.close()
        return [Review(*row) for row in rows]

    def insert_review(self, review_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `reviews` (product_id, customer_id, review_text, rating) VALUES (%s, %s, %s, %s)",
            (review_data["product_id"], review_data["customer_id"], review_data["review_text"], review_data["rating"])
        )
        self.mysql.connection.commit()
        cur.close()

    def update_review(self, review_id, review_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE `reviews` SET product_id = %s, customer_id = %s, review_text = %s, rating = %s WHERE review_id = %s",
            (review_data["product_id"], review_data["customer_id"], review_data["review_text"], review_data["rating"], review_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_review(self, review_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `reviews` WHERE review_id = %s", (review_id,))
        self.mysql.connection.commit()
        cur.close()
