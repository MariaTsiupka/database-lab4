from ..dao.order_item_dao import OrderItemDAO

class OrderItemService:
    def __init__(self, mysql):
        self.dao = OrderItemDAO(mysql)

    def get_order_items(self):
        return self.dao.get_all_order_items()

    def add_order_item(self, order_item_data):
        return self.dao.insert_order_item(order_item_data)

    def modify_order_item(self, order_item_id, order_item_data):
        return self.dao.update_order_item(order_item_id, order_item_data)

    def remove_order_item(self, order_item_id):
        return self.dao.delete_order_item(order_item_id)
