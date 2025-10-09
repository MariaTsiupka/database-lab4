class ProductType:
    def __init__(self, product_type_id, type_name, type_description):
        self.product_type_id = product_type_id
        self.type_name = type_name
        self.type_description = type_description

    def to_dict(self):
        return {
            "product_type_id": self.product_type_id,
            "type_name": self.type_name,
            "type_description": self.type_description,
        }
    
