from flask import Blueprint, request, jsonify
from ..services.customer_card_service import CustomerCardService

def create_customer_card_controller(mysql):
    customer_card_controller = Blueprint('customer_card', __name__)
    service = CustomerCardService(mysql)

    @customer_card_controller.route('/cards', methods=['GET'])
    def get_cards():
        cards = service.get_cards()
        return jsonify([card.to_dict() for card in cards])

    @customer_card_controller.route('/cards', methods=['POST'])
    def create_card():
        data = request.json
        if not data or 'customer_id' not in data or 'card_number' not in data or 'bonus_num' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_card(data)
            return jsonify({"message": "Card created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @customer_card_controller.route('/cards/<int:card_id>', methods=['PUT'])
    def update_card(card_id):
        data = request.json
        if not data or 'customer_id' not in data or 'card_number' not in data or 'bonus_num' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_card(card_id, data)
            return jsonify({"message": "Card updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @customer_card_controller.route('/cards/<int:card_id>', methods=['DELETE'])
    def delete_card(card_id):
        try:
            service.remove_card(card_id)
            return jsonify({"message": "Card deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return customer_card_controller
