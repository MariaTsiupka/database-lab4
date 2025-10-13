from flask import Blueprint, request, jsonify
from ..services.product_attribute_service import ProductAttributeService

def create_product_attribute_controller(mysql):
    product_attribute_controller = Blueprint('product_attribute', __name__)
    service = ProductAttributeService(mysql)


    @product_attribute_controller.route('/product_attributes/<int:product_id>', methods=['GET'])
    def get_attributes_for_product(product_id):
        attributes = service.get_attributes(product_id)
        return jsonify([attribute.to_dict() for attribute in attributes])



    @product_attribute_controller.route('/product/<int:product_id>/attributes', methods=['POST'])
    def add_product_attribute(product_id):
        data = request.json
        if not data or 'attribute_name' not in data or 'attribute_value' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            attribute_data = {
                "product_id": product_id,
                "attribute_name": data["attribute_name"],
                "attribute_value": data["attribute_value"]
            }
            service.add_attribute(attribute_data)
            return jsonify({"message": "Product attribute added"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @product_attribute_controller.route('/product/attributes/<int:attribute_id>', methods=['PUT'])
    def update_product_attribute(attribute_id):
        data = request.json
        if not data or 'attribute_name' not in data or 'attribute_value' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            attribute_data = {
                "attribute_name": data["attribute_name"],
                "attribute_value": data["attribute_value"]
            }
            service.update_attribute(attribute_id, attribute_data)
            return jsonify({"message": "Product attribute updated"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @product_attribute_controller.route('/product/attributes/<int:attribute_id>', methods=['DELETE'])
    def delete_product_attribute(attribute_id):
        try:
            service.remove_attribute(attribute_id)
            return jsonify({"message": "Product attribute deleted"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return product_attribute_controller
