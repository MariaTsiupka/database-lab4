from flask import Blueprint, request, jsonify
from my_project.auth.services.order_service import OrderService

def create_order_controller(mysql):
    order_controller = Blueprint('order', __name__)
    service = OrderService(mysql)

    @order_controller.route('/orders', methods=['GET'])
    def get_orders():
        orders = service.get_orders()
        return jsonify([order.to_dict() for order in orders])


    @order_controller.route('/customer/<int:customer_id>/orders', methods=['GET'])
    def get_orders_by_customer(customer_id):
        try:
            orders = service.get_orders_by_customer(customer_id)
            if not orders:
                return jsonify({"message": "No orders found for this customer"}), 404
            return jsonify(orders)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @order_controller.route('/orders', methods=['POST'])
    def create_order():
        data = request.json
        if not data or 'customer_id' not in data or 'order_date' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_order(data)
            return jsonify({"message": "Order created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @order_controller.route('/orders/<int:order_id>', methods=['PUT'])
    def update_order(order_id):
        data = request.json
        if not data or 'customer_id' not in data or 'order_date' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_order(order_id, data)
            return jsonify({"message": "Order updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @order_controller.route('/orders/<int:order_id>', methods=['DELETE'])
    def delete_order(order_id):
        try:
            service.remove_order(order_id)
            return jsonify({"message": "Order deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        


    return order_controller
