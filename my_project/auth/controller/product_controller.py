from flask import Blueprint, request, jsonify
from my_project.auth.services.product_service import ProductService

def create_product_controller(mysql):
    product_controller = Blueprint('products', __name__)
    service = ProductService(mysql)

    @product_controller.route('/products', methods=['GET'])
    def get_products():
        products = service.get_products()
        return jsonify([product.to_dict() for product in products])

    @product_controller.route('/company/<int:company_id>/products', methods=['GET'])
    def get_products_by_company(company_id):
        try:
            products = service.get_products_by_company(company_id)
            if not products:
                return jsonify({"message": "No products found for this company"}), 404
            return jsonify([product.to_dict() for product in products])
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @product_controller.route('/products', methods=['POST'])
    def create_product():
        data = request.json
        if not data or 'company_id' not in data or 'product_type_id' not in data or \
           'product_name' not in data or 'product_description' not in data or 'price' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_product(data)
            return jsonify({"message": "Product created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @product_controller.route('/products/<int:product_id>', methods=['PUT'])
    def update_product(product_id):
        data = request.json
        if not data or 'company_id' not in data or 'product_type_id' not in data or \
           'product_name' not in data or 'product_description' not in data or 'price' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            # Використовуємо метод modify_product замість update_product
            service.modify_product(product_id, data)
            return jsonify({"message": "Product updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @product_controller.route('/products/<int:product_id>', methods=['DELETE'])
    def delete_product(product_id):
        try:
            service.remove_product(product_id)
            return jsonify({"message": "Product deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @product_controller.route('/insert_products_batch', methods=['POST'])
    def insert_products_batch():
        data = request.json  # отримаємо JSON із тіла запиту

        if not data or 'products' not in data:
            return jsonify({"error": "Invalid data, 'products' key missing."}), 400
        
        try:
            # Передаємо список продуктів для вставки у сервіс
            service.add_products_batch(data['products'])
            return jsonify({"message": "Products batch inserted successfully."}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500 
    return product_controller

   
