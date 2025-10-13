from flask import Blueprint, request, jsonify
from ..services.order_item_service import OrderItemService

def create_order_item_controller(mysql):
    order_item_controller = Blueprint('order_item', __name__)
    service = OrderItemService(mysql)

    @order_item_controller.route('/order_items', methods=['GET'])
    def get_order_items():
        order_items = service.get_order_items()
        return jsonify([order_item.to_dict() for order_item in order_items])

    @order_item_controller.route('/order_items', methods=['POST'])
    def create_order_item():
        data = request.json
        if not data or 'order_id' not in data or 'product_id' not in data or 'quantity' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_order_item(data)
            return jsonify({"message": "Order Item created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @order_item_controller.route('/order_items/<int:order_item_id>', methods=['PUT'])
    def update_order_item(order_item_id):
        data = request.json
        if not data or 'order_id' not in data or 'product_id' not in data or 'quantity' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_order_item(order_item_id, data)
            return jsonify({"message": "Order Item updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @order_item_controller.route('/order_items/<int:order_item_id>', methods=['DELETE'])
    def delete_order_item(order_item_id):
        try:
            service.remove_order_item(order_item_id)
            return jsonify({"message": "Order Item deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return order_item_controller
