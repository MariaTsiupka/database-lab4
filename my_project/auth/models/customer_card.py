class CustomerCard:
    def __init__(self, card_id, customer_id, card_number, bonus_num):
        self.card_id = card_id
        self.customer_id = customer_id
        self.card_number = card_number
        self.bonus_num = bonus_num  

    def to_dict(self):
        return {
            "card_id": self.card_id,
            "customer_id": self.customer_id,
            "card_number": self.card_number,
            "bonus_num": self.bonus_num,  
        }
