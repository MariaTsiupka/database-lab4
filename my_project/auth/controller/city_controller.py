from flask import Blueprint, request, jsonify
from my_project.auth.services.city_service import CityService

def create_city_controller(mysql):
    city_controller = Blueprint('city', __name__)
    service = CityService(mysql)

    @city_controller.route('/cities', methods=['GET'])
    def get_cities():
        """
        Get all cities
        ---
        responses:
          200:
            description: List of all cities
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                      city_name:
                        type: string
        """
        cities = service.get_cities()
        return jsonify([city.to_dict() for city in cities])

    @city_controller.route('/cities', methods=['POST'])
    def create_city():
        """
        Create a new city
        ---
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  city_name:
                    type: string
        responses:
          201:
            description: City created successfully
          400:
            description: Invalid data provided
          500:
            description: Server error
        """
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
        """
        Update existing city
        ---
        parameters:
          - name: city_id
            in: path
            required: true
            schema:
              type: integer
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  city_name:
                    type: string
        responses:
          200:
            description: City updated successfully
          400:
            description: Invalid data
          500:
            description: Server error
        """
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
        """
        Delete a city
        ---
        parameters:
          - name: city_id
            in: path
            required: true
            schema:
              type: integer
        responses:
          200:
            description: City deleted successfully
          500:
            description: Server error
        """
        try:
            service.remove_city(city_id)
            return jsonify({"message": "City deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return city_controller

