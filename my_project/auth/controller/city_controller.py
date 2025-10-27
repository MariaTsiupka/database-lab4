from flask import Blueprint, request, jsonify
from flasgger import swag_from
from my_project.auth.services.city_service import CityService

def create_city_controller(mysql):
    city_controller = Blueprint('city', __name__)
    service = CityService(mysql)

    @city_controller.route('/cities', methods=['GET'])
    @swag_from({
        'tags': ['Cities'],
        'summary': 'Отримати всі міста',
        'responses': {
            200: {
                'description': 'Список міст',
                'content': {
                    'application/json': {
                        'example': [
                            {"id": 1, "city_name": "Kyiv"},
                            {"id": 2, "city_name": "Lviv"}
                        ]
                    }
                }
            }
        }
    })
    def get_cities():
        cities = service.get_cities()
        return jsonify([city.to_dict() for city in cities])

    @city_controller.route('/cities', methods=['POST'])
    @swag_from({
        'tags': ['Cities'],
        'summary': 'Створити нове місто',
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {"city_name": "Odessa"}
                }
            }
        },
        'responses': {
            201: {'description': 'Місто створено'},
            400: {'description': 'Некоректні дані'},
            500: {'description': 'Помилка сервера'}
        }
    })
    def create_city():
        data = request.json
        if not data or 'city_name' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.add_city(data)
            return jsonify({"message": "City created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @city_controller.route('/cities/<int:city_id>', methods=['PUT'])
    @swag_from({
        'tags': ['Cities'],
        'summary': 'Оновити дані міста',
        'parameters': [
            {'name': 'city_id', 'in': 'path', 'required': True, 'schema': {'type': 'integer'}}
        ],
        'requestBody': {
            'required': True,
            'content': {
                'application/json': {
                    'example': {"city_name": "Dnipro"}
                }
            }
        },
        'responses': {
            200: {'description': 'Місто оновлено'},
            400: {'description': 'Некоректні дані'},
            500: {'description': 'Помилка сервера'}
        }
    })
    def update_city(city_id):
        data = request.json
        if not data or 'city_name' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_city(city_id, data)
            return jsonify({"message": "City updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @city_controller.route('/cities/<int:city_id>', methods=['DELETE'])
    @swag_from({
        'tags': ['Cities'],
        'summary': 'Видалити місто',
        'parameters': [
            {'name': 'city_id', 'in': 'path', 'required': True, 'schema': {'type': 'integer'}}
        ],
        'responses': {
            200: {'description': 'Місто видалено'},
            500: {'description': 'Помилка сервера'}
        }
    })
    def delete_city(city_id):
        try:
            service.remove_city(city_id)
            return jsonify({"message": "City deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return city_controller
