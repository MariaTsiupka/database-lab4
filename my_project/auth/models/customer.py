class Customer:
    def __init__(self, customer_id, customer_name, customer_surname, customer_email, customer_phone):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_email = customer_email
        self.customer_phone = customer_phone

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "customer_surname": self.customer_surname,
            "customer_email": self.customer_email,
            "customer_phone": self.customer_phone,
        }
