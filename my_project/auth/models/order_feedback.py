class OrderFeedback:
    def __init__(self, feedback_id, order_id, feedback_text, rating, feedback_date):
        self.feedback_id = feedback_id
        self.order_id = order_id
        self.feedback_text = feedback_text
        self.rating = rating
        self.feedback_date = feedback_date

    def to_dict(self):
        return {
            "feedback_id": self.feedback_id,
            "order_id": self.order_id,
            "feedback_text": self.feedback_text,
            "rating": self.rating,
            "feedback_date": self.feedback_date,
        }
