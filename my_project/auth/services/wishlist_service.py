from dao.wishlist_dao import WishlistDAO

class WishlistService:
    def __init__(self, mysql):
        self.dao = WishlistDAO(mysql)

    def get_wishlists(self):
        return self.dao.get_all_wishlists()
    def get_products_for_customer(self, customer_id):
        return self.dao.get_products_for_customer(customer_id)

    def get_customers_for_product(self, product_id):
        return self.dao.get_customers_for_product(product_id)

    def add_wishlist(self, wishlist_data):
        return self.dao.insert_wishlist(wishlist_data)

    def remove_wishlist(self, wishlist_id):
        return self.dao.delete_wishlist(wishlist_id)

    def modify_wishlist(self, wishlist_id, wishlist_data):
        return self.dao.update_wishlist(wishlist_id, wishlist_data)

    def add_wishlist_by_name_and_product_name(self, customer_name, customer_surname, product_name):
        return self.dao.insert_wishlist_by_name_and_product_name(customer_name, customer_surname, product_name)
