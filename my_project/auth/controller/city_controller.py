from flask import Blueprint, request, jsonify
from ..services.city_service import CityService

def create_city_controller(mysql):
    city_controller = Blueprint('city', __name__)
    service = CityService(mysql)

    @city_controller.route('/cities', methods=['GET'])
    def get_cities():
        cities = service.get_cities()
        return jsonify([city.to_dict() for city in cities])

    @city_controller.route('/cities', methods=['POST'])
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
    def delete_city(city_id):
        try:
            service.remove_city(city_id)
            return jsonify({"message": "City deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return city_controller
