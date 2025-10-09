from flask import Blueprint, request, jsonify
from services.customer_service import CustomerService

def create_customer_controller(mysql):
    customer_controller = Blueprint('customer', __name__)
    service = CustomerService(mysql)

    @customer_controller.route('/customers', methods=['GET'])
    def get_customers():
        customers = service.get_customers()
        return jsonify([customer.to_dict() for customer in customers])
    
    # Маршрут для отримання одного клієнта разом із його карткою
    @customer_controller.route('/customers/<int:customer_id>/card', methods=['GET'])
    def get_customer_with_card(customer_id):
        result = service.get_customer_with_card(customer_id)
        if result:
            return jsonify(result)
        return jsonify({"error": "Customer not found"}), 404


    @customer_controller.route('/customers/<int:customer_id>', methods=['GET'])
    def get_customer(customer_id):
        customer = service.get_customer(customer_id)
        if customer:
            return jsonify(customer.to_dict())
        return jsonify({"error": "Customer not found"}), 404
    
    @customer_controller.route('/customers', methods=['POST'])
    def create_customer():
        data = request.json
        if not data or not all(key in data for key in ("customer_name", "customer_surname", "customer_email", "customer_phone")):
            return jsonify({"error": "Invalid data"}), 400
        service.add_customer(data)
        return jsonify({"message": "Customer created"}), 201
    
    @customer_controller.route('/customers/<int:customer_id>', methods=['PUT'])
    def update_customer(customer_id):
        data = request.json
        if not data or not all(key in data for key in ("customer_name", "customer_surname", "customer_email", "customer_phone")):
            return jsonify({"error": "Invalid data"}), 400
        service.modify_customer(customer_id, data)
        return jsonify({"message": "Customer updated"})
    
    @customer_controller.route('/customers/<int:customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        service.remove_customer(customer_id)
        return jsonify({"message": "Customer deleted"})
    
    return customer_controller
