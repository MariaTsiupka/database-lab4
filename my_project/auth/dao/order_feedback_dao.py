class OrderFeedbackDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_feedbacks(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM order_feedback")
        rows = cur.fetchall()
        cur.close()
        return [
            {
                "feedback_id": row[0],
                "order_id": row[1],
                "feedback_text": row[2],
                "rating": row[3],
                "feedback_date": row[4]
            }
            for row in rows
        ]

    def get_feedback_by_order_id(self, order_id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM order_feedback WHERE order_id = %s", (order_id,))
        row = cur.fetchone()
        cur.close()
        return {
            "feedback_id": row[0],
            "order_id": row[1],
            "feedback_text": row[2],
            "rating": row[3],
            "feedback_date": row[4]
        } if row else None

    def insert_feedback(self, feedback_data):
        cur = self.mysql.connection.cursor()
        try:
            # Виклик збереженої процедури для вставки
            cur.execute(
                "CALL insert_into_order_feedback(%s, %s, %s)",
                (feedback_data["order_id"], feedback_data["feedback_text"], feedback_data["rating"])
            )
            self.mysql.connection.commit()
        except Exception as e:
            self.mysql.connection.rollback()
            raise e
        finally:
            cur.close()

    def update_feedback(self, feedback_id, feedback_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE order_feedback SET feedback_text = %s, rating = %s WHERE feedback_id = %s",
            (feedback_data["feedback_text"], feedback_data["rating"], feedback_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_feedback(self, feedback_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM order_feedback WHERE feedback_id = %s", (feedback_id,))
        self.mysql.connection.commit()
        cur.close()
