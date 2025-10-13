from ..models.wishlist import Wishlist

class WishlistDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_wishlists(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM `wishlist`")
        rows = cur.fetchall()
        cur.close()
        return [Wishlist(*row) for row in rows]


    def get_products_for_customer(self, customer_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT p.product_id, p.product_name, p.product_description, p.price
            FROM wishlist w
            JOIN product p ON w.product_id = p.product_id
            WHERE w.customer_id = %s
        """, (customer_id,))
        rows = cur.fetchall()
        cur.close()
        return [{
        "product_id": row[0],
        "product_name": row[1],
        "product_description": row[2],
        "price": row[3]
    } for row in rows]

    def get_customers_for_product(self, product_id):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT c.customer_id, c.customer_name, c.customer_email
            FROM wishlist w
            JOIN customer c ON w.customer_id = c.customer_id
            WHERE w.product_id = %s
        """, (product_id,))
        rows = cur.fetchall()
        cur.close()
        return [{
        "customer_id": row[0],
        "customer_name": row[1],
        "customer_email": row[2]
    } for row in rows]


    def insert_wishlist(self, wishlist_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `wishlist` (customer_id, product_id) VALUES (%s, %s)",
            (wishlist_data["customer_id"], wishlist_data["product_id"])
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_wishlist(self, wishlist_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM `wishlist` WHERE wishlist_id = %s", (wishlist_id,))
        self.mysql.connection.commit()
        cur.close()

    def update_wishlist(self, wishlist_id, wishlist_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE `wishlist` SET customer_id = %s, product_id = %s WHERE wishlist_id = %s",
            (wishlist_data["customer_id"], wishlist_data["product_id"], wishlist_id)
        )
        self.mysql.connection.commit()
        cur.close()
    def insert_wishlist_by_name_and_product_name(self, customer_name, customer_surname, product_name):
        cur = self.mysql.connection.cursor()
    
        # Отримати customer_id за customer_name та customer_surname
        cur.execute("SELECT customer_id FROM customer WHERE customer_name = %s AND customer_surname = %s", 
                (customer_name, customer_surname))
        customer = cur.fetchone()
    
    # Отримати product_id за product_name
        cur.execute("SELECT product_id FROM product WHERE product_name = %s", (product_name,))
        product = cur.fetchone()
    
        if customer and product:
        # Вставка в таблицю wishlist
            cur.execute("INSERT INTO wishlist (customer_id, product_id) VALUES (%s, %s)",
                    (customer[0], product[0]))  # customer[0] - це customer_id, product[0] - це product_id
            self.mysql.connection.commit()
            cur.close()
            return {"message": "Wishlist item added successfully"}
        else:
            cur.close()
            return {"error": "Customer or product not found"}
