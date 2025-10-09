from dao.customer_card_dao import CustomerCardDAO

class CustomerCardService:
    def __init__(self, mysql):
        self.dao = CustomerCardDAO(mysql)

    def get_cards(self):
        return self.dao.get_all_cards()

    def add_card(self, card_data):
        return self.dao.insert_card(card_data)

    def modify_card(self, card_id, card_data):
        return self.dao.update_card(card_id, card_data)

    def remove_card(self, card_id):
        return self.dao.delete_card(card_id)
