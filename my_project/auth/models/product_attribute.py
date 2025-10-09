class ProductAttribute:
    def __init__(self, attribute_id, product_id, attribute_name, attribute_value):
        self.attribute_id = attribute_id
        self.product_id = product_id
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value

    def to_dict(self):
        return {
            "attribute_id": self.attribute_id,
            "product_id": self.product_id,
            "attribute_name": self.attribute_name,
            "attribute_value": self.attribute_value,
        }
