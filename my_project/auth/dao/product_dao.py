from my_project.auth.models.product import Product

class ProductDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_products(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM product")
        products = cur.fetchall()
        cur.close()
        return [Product(product_id=row[0], company_id=row[1], product_type_id=row[2],
                        product_name=row[3], product_description=row[4], price=row[5]) for row in products]

    def get_products_by_company(self, company_id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM product WHERE company_id = %s", (company_id,))
        products = cur.fetchall()
        cur.close()
        return [Product(product_id=row[0], company_id=row[1], product_type_id=row[2],
                        product_name=row[3], product_description=row[4], price=row[5]) for row in products]

    def insert_product(self, product):
        # Вставляємо новий продукт без вказівки product_id
        cur = self.mysql.connection.cursor()
        cur.execute("""
            INSERT INTO product (company_id, product_type_id, product_name, product_description, price)
            VALUES (%s, %s, %s, %s, %s)
        """, (product['company_id'], product['product_type_id'], product['product_name'],
              product['product_description'], product['price']))  # product_id не вказуємо
        self.mysql.connection.commit()
        cur.close()

    def update_product(self, product_id, product):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            UPDATE product SET company_id = %s, product_type_id = %s, product_name = %s,
            product_description = %s, price = %s WHERE product_id = %s
        """, (product['company_id'], product['product_type_id'], product['product_name'],
              product['product_description'], product['price'], product_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_product(self, product_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM product WHERE product_id = %s", (product_id,))
        self.mysql.connection.commit()
        cur.close()

     # Отримати продукти разом із назвою компанії (за допомогою JOIN)
    def get_products_with_company(self):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT p.product_id, p.company_id, p.product_type_id, p.product_name,
                   p.product_description, p.price, c.company_name
            FROM product p
            JOIN company c ON p.company_id = c.company_id
        """)
        products = cur.fetchall()
        cur.close()
        return [
            {
                "product_id": row[0],
                "company_id": row[1],
                "product_type_id": row[2],
                "product_name": row[3],
                "product_description": row[4],
                "price": row[5],
                "company_name": row[6]
            }
            for row in products
        ]
    def insert_product(self, product):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            INSERT INTO product (company_id, product_type_id, product_name, product_description, price)
            VALUES (%s, %s, %s, %s, %s)
        """, (product['company_id'], product['product_type_id'], product['product_name'],
              product['product_description'], product['price']))
        self.mysql.connection.commit()
        cur.close()
