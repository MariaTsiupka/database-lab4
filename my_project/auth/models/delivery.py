class Delivery:
    def __init__(self, delivery_id, order_id, city_id, delivery_method, delivery_address):
        self.delivery_id = delivery_id
        self.order_id = order_id
        self.city_id = city_id
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address

    def to_dict(self):
        return {
            "delivery_id": self.delivery_id,
            "order_id": self.order_id,
            "city_id": self.city_id,
            "delivery_method": self.delivery_method,
            "delivery_address": self.delivery_address,
        }