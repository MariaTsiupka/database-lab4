from flask import Blueprint, request, jsonify
from my_project.auth.services.wishlist_service import WishlistService

def create_wishlist_controller(mysql):
    wishlist_controller = Blueprint('wishlist', __name__)
    service = WishlistService(mysql)


    @wishlist_controller.route('/wishlist', methods=['GET'])
    def get_wishlists():
        wishlists = service.get_wishlists()
        return jsonify([wishlist.to_dict() for wishlist in wishlists])


    @wishlist_controller.route('/wishlist/customer/<int:customer_id>', methods=['GET'])
    def get_products_for_customer(customer_id):
        try:
            products = service.get_products_for_customer(customer_id)
            return jsonify(products)  # повертаємо деталі продуктів
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @wishlist_controller.route('/wishlist/product/<int:product_id>', methods=['GET'])
    def get_customers_for_product(product_id):
        try:
            customers = service.get_customers_for_product(product_id)
            return jsonify(customers)  # повертаємо деталі клієнтів
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @wishlist_controller.route('/wishlist', methods=['POST'])
    def create_wishlist():
        data = request.json
        if not data or 'customer_id' not in data or 'product_id' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.add_wishlist(data)
            return jsonify({"message": "Wishlist item added"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @wishlist_controller.route('/wishlist/<int:wishlist_id>', methods=['PUT'])
    def update_wishlist(wishlist_id):
        data = request.json
        if not data or 'customer_id' not in data or 'product_id' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_wishlist(wishlist_id, data)
            return jsonify({"message": "Wishlist item updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @wishlist_controller.route('/wishlist/<int:wishlist_id>', methods=['DELETE'])
    def delete_wishlist(wishlist_id):
        try:
            service.remove_wishlist(wishlist_id)
            return jsonify({"message": "Wishlist item deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @wishlist_controller.route('/wishlist/add_by_names', methods=['POST'])
    def add_wishlist_by_names():
        data = request.json
        if not data or not all(key in data for key in ("customer_name", "customer_surname", "product_name")):
            return jsonify({"error": "Invalid data"}), 400

        try:
            result = service.insert_wishlist_by_name_and_product_name(data["customer_name"], data["customer_surname"], data["product_name"])
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    # Маршрут для додавання елемента до wishlist за іменем клієнта та назвою продукту
    @wishlist_controller.route('/wishlist/by_name_and_product', methods=['POST'])
    def add_wishlist_by_name_and_product():
        data = request.json
        customer_name = data.get('customer_name')
        customer_surname = data.get('customer_surname')
        product_name = data.get('product_name')
        
        if not customer_name or not customer_surname or not product_name:
            return jsonify({"error": "Missing required parameters"}), 400
        
        result = service.add_wishlist_by_name_and_product_name(customer_name, customer_surname, product_name)
        return jsonify(result)

    return wishlist_controller
