class Wishlist:
    def __init__(self, wishlist_id, customer_id, product_id):
        self.wishlist_id = wishlist_id
        self.customer_id = customer_id
        self.product_id = product_id

    def to_dict(self):
        return {
            "wishlist_id": self.wishlist_id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
        }
