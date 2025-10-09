class Review:
    def __init__(self, review_id, product_id, customer_id, review_text, rating):
        self.review_id = review_id
        self.product_id = product_id
        self.customer_id = customer_id
        self.review_text = review_text
        self.rating = rating

    def to_dict(self):
        return {
            "review_id": self.review_id,
            "product_id": self.product_id,
            "customer_id": self.customer_id,
            "review_text": self.review_text,
            "rating": self.rating,
        }