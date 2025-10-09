class Order:
    def __init__(self, order_id, customer_id, order_date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "order_date": self.order_date,
        }