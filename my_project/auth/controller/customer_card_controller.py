from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ..services.customer_card_service import CustomerCardService

def create_customer_card_controller(mysql):
    customer_card_controller = Blueprint('customer_card', __name__)
    service = CustomerCardService(mysql)

    @customer_card_controller.route('/cards', methods=['GET'])
    @swag_from({
        'tags': ['Customer Cards'],
        'summary': 'Отримати всі картки клієнтів',
        'responses': {
            200: {
                'description': 'Список карток',
                'content': {
                    'application/json': {
                        'example': [
                            {"id": 1, "customer_id": 2, "card_number": "12345", "bonus_num": 150}
                        ]
                    }
                }
            }
        }
    })
    def get_cards():
        """Отримати всі картки клієнтів"""
        cards = service.get_cards()
        return jsonify([card.to_dict() for card in cards])

    @customer_card_controller.route('/cards', methods=['POST'])
    @swag_from({
        'tags': ['Customer Cards'],
        'summary': 'Створити нову картку клієнта',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        'customer_id': 1,
                        'card_number': '987654321',
                        'bonus_num': 200
                    }
                }
            }
        },
        'responses': {
            201: {'description': 'Картка створена успішно'},
            400: {'description': 'Некоректні дані'}
        }
    })
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
    @swag_from({
        'tags': ['Customer Cards'],
        'summary': 'Оновити дані картки',
        'parameters': [
            {'name': 'card_id', 'in': 'path', 'required': True, 'schema': {'type': 'integer'}}
        ],
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {
                        'customer_id': 1,
                        'card_number': '99999',
                        'bonus_num': 250
                    }
                }
            }
        },
        'responses': {
            200: {'description': 'Картку оновлено'},
            400: {'description': 'Некоректні дані'}
        }
    })
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
    @swag_from({
        'tags': ['Customer Cards'],
        'summary': 'Видалити картку',
        'parameters': [
            {'name': 'card_id', 'in': 'path', 'required': True, 'schema': {'type': 'integer'}}
        ],
        'responses': {
            200: {'description': 'Картку видалено'},
            404: {'description': 'Картку не знайдено'}
        }
    })
    def delete_card(card_id):
        try:
            service.remove_card(card_id)
            return jsonify({"message": "Card deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return customer_card_controller

