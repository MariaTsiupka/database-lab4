from flask import Blueprint, request, jsonify
from ..services.delivery_service import DeliveryService

def create_delivery_controller(mysql):
    delivery_controller = Blueprint('delivery', __name__)
    service = DeliveryService(mysql)


    @delivery_controller.route('/deliveries', methods=['GET'])
    def get_deliveries():
        deliveries = service.get_deliveries()
        return jsonify([delivery.to_dict() for delivery in deliveries])


    @delivery_controller.route('/deliveries', methods=['POST'])
    def create_delivery():
        data = request.json
        if not data or 'order_id' not in data or 'city_id' not in data or 'delivery_method' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.add_delivery(data)
            return jsonify({"message": "Delivery created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @delivery_controller.route('/deliveries/<int:delivery_id>', methods=['PUT'])
    def update_delivery(delivery_id):
        data = request.json
        if not data or 'order_id' not in data or 'city_id' not in data or 'delivery_method' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_delivery(delivery_id, data)
            return jsonify({"message": "Delivery updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @delivery_controller.route('/deliveries/<int:delivery_id>', methods=['DELETE'])
    def delete_delivery(delivery_id):
        try:
            service.remove_delivery(delivery_id)
            return jsonify({"message": "Delivery deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return delivery_controller
