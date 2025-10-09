from dao.product_attribute_dao import ProductAttributeDAO

class ProductAttributeService:
    def __init__(self, mysql):
        self.dao = ProductAttributeDAO(mysql)

    def get_attributes(self, product_id):
        return self.dao.get_all_attributes(product_id)

    def add_attribute(self, attribute_data):
        return self.dao.insert_attribute(attribute_data)

    def update_attribute(self, attribute_id, attribute_data):
        return self.dao.update_attribute(attribute_id, attribute_data)

    def remove_attribute(self, attribute_id):
        return self.dao.delete_attribute(attribute_id)
