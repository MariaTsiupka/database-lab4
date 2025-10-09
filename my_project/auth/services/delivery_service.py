from dao.delivery_dao import DeliveryDAO

class DeliveryService:
    def __init__(self, mysql):
        self.dao = DeliveryDAO(mysql)

    def get_deliveries(self):
        return self.dao.get_all_deliveries()

    def add_delivery(self, delivery_data):
        return self.dao.insert_delivery(delivery_data)

    def modify_delivery(self, delivery_id, delivery_data):
        return self.dao.update_delivery(delivery_id, delivery_data)

    def remove_delivery(self, delivery_id):
        return self.dao.delete_delivery(delivery_id)
