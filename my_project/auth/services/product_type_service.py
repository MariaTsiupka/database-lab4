from ..dao.product_type_dao import ProductTypeDAO

class ProductTypeService:
    def __init__(self, mysql):
        self.dao = ProductTypeDAO(mysql)

    def get_product_types(self):
        return self.dao.get_all_product_types()

    def add_product_type(self, product_type_data):
        return self.dao.insert_product_type(product_type_data)

    def modify_product_type(self, product_type_id, product_type_data):
        return self.dao.update_product_type(product_type_id, product_type_data)

    def remove_product_type(self, product_type_id):
        return self.dao.delete_product_type(product_type_id)
