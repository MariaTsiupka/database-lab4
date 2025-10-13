from ..dao.product_dao import ProductDAO

class ProductService:
    def __init__(self, mysql):
        self.dao = ProductDAO(mysql)

    def get_products(self):
        return self.dao.get_all_products()

    # Отримати продукти разом із компанією
    def get_products_by_company(self, company_id):
        return self.dao.get_products_by_company(company_id)
    
    def add_product(self, product):
        return self.dao.insert_product(product)

    def modify_product(self, product_id, product):
        return self.dao.update_product(product_id, product)

    def remove_product(self, product_id):
        return self.dao.delete_product(product_id)

    def add_products_batch(self, products):
        # products має бути списком словників із даними продуктів
        for product in products:
            self.dao.insert_product(product)
