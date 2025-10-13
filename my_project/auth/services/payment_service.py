from ..dao.payment_dao import PaymentDAO

class PaymentService:
    def __init__(self, mysql):
        self.dao = PaymentDAO(mysql)

    def get_payments(self):
        return self.dao.get_all_payments()

    def add_payment(self, payment_data):
        return self.dao.insert_payment(payment_data)

    def modify_payment(self, payment_id, payment_data):
        return self.dao.update_payment(payment_id, payment_data)

    def remove_payment(self, payment_id):
        return self.dao.delete_payment(payment_id)
