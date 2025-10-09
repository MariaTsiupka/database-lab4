from dao.customer_dao import CustomerDAO

class CustomerService:
    def __init__(self, mysql):
        self.dao = CustomerDAO(mysql)

    def get_customers(self):
        return self.dao.get_all_customers()

    def get_customer_with_card(self, customer_id):
        return self.dao.get_customer_with_card(customer_id)
    
    def get_customer(self, customer_id):
        return self.dao.get_customer_by_id(customer_id)

    def add_customer(self, customer):
        self.dao.insert_customer(customer)

    def modify_customer(self, customer_id, customer):
        self.dao.update_customer(customer_id, customer)

    def remove_customer(self, customer_id):
        self.dao.delete_customer(customer_id)
