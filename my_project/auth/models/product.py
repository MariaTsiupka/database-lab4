class Product:
    def __init__(self, product_id, company_id, product_type_id, product_name, product_description, price):
        self.product_id = product_id
        self.company_id = company_id
        self.product_type_id = product_type_id
        self.product_name = product_name
        self.product_description = product_description
        self.price = price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "company_id": self.company_id,
            "product_type_id": self.product_type_id,
            "product_name": self.product_name,
            "product_description": self.product_description,
            "price": self.price,
        }