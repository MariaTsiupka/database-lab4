from flask import Blueprint, request, jsonify
from services.product_type_service import ProductTypeService

def create_product_type_controller(mysql):
    product_type_controller = Blueprint('product_type', __name__)
    service = ProductTypeService(mysql)

    @product_type_controller.route('/product_type', methods=['GET'])
    def get_product_types():
        product_types = service.get_product_types()
        return jsonify([product_type.to_dict() for product_type in product_types])


    @product_type_controller.route('/product_type', methods=['POST'])
    def create_product_type():
        data = request.json
        if not data or 'type_name' not in data or 'type_description' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.add_product_type(data)
            return jsonify({"message": "Product type added"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @product_type_controller.route('/product_type/<int:product_type_id>', methods=['PUT'])
    def update_product_type(product_type_id):
        data = request.json
        if not data or 'type_name' not in data or 'type_description' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_product_type(product_type_id, data)
            return jsonify({"message": "Product type updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @product_type_controller.route('/product_type/<int:product_type_id>', methods=['DELETE'])
    def delete_product_type(product_type_id):
        try:
            service.remove_product_type(product_type_id)
            return jsonify({"message": "Product type deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return product_type_controller
