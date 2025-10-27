from my_project.auth.dao.order_dao import OrderDAO

class OrderService:
    def __init__(self, mysql):
        self.dao = OrderDAO(mysql)

    def get_orders(self):
        return self.dao.get_all_orders()

    def get_orders_by_customer(self, customer_id):
        return self.dao.get_orders_by_customer_id(customer_id)

    def add_order(self, order_data):
        return self.dao.insert_order(order_data)

    def modify_order(self, order_id, order_data):
        return self.dao.update_order(order_id, order_data)

    def remove_order(self, order_id):
        return self.dao.delete_order(order_id)
