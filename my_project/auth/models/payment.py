class Payment:
    def __init__(self, payment_id, order_id, payment_method, payment_status):
        self.payment_id = payment_id
        self.order_id = order_id
        self.payment_method = payment_method
        self.payment_status = payment_status

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "order_id": self.order_id,
            "payment_method": self.payment_method,
            "payment_status": self.payment_status,
        }
