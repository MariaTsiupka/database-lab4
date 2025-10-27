# controllers/order_feedback_controller.py
from flask import Blueprint, request, jsonify
from my_project.auth.services.order_feedback_service import OrderFeedbackService

def create_order_feedback_controller(mysql):
    feedback_controller = Blueprint('order_feedback', __name__)
    service = OrderFeedbackService(mysql)

    @feedback_controller.route('/order_feedbacks', methods=['GET'])
    def get_feedbacks():
        feedbacks = service.get_feedbacks()
        return jsonify(feedbacks)

    @feedback_controller.route('/order/<int:order_id>/feedback', methods=['GET'])
    def get_feedback_by_order(order_id):
        feedback = service.get_feedback_by_order(order_id)
        if not feedback:
            return jsonify({"message": "No feedback found for this order"}), 404
        return jsonify(feedback)


    @feedback_controller.route('/order_feedbacks', methods=['POST'])
    def create_feedback():
        data = request.json
        if not data or 'order_id' not in data or 'feedback_text' not in data or 'rating' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_feedback(data)
            return jsonify({"message": "Feedback created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @feedback_controller.route('/order_feedbacks/<int:feedback_id>', methods=['PUT'])
    def update_feedback(feedback_id):
        data = request.json
        if not data or 'feedback_text' not in data or 'rating' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_feedback(feedback_id, data)
            return jsonify({"message": "Feedback updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @feedback_controller.route('/order_feedbacks/<int:feedback_id>', methods=['DELETE'])
    def delete_feedback(feedback_id):
        try:
            service.remove_feedback(feedback_id)
            return jsonify({"message": "Feedback deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @feedback_controller.route('/order_feedbacks/procedure', methods=['POST'])
    def create_feedback_using_procedure():
        data = request.json
        if not data or 'order_id' not in data or 'feedback_text' not in data or 'rating' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
        # Виклик збереженої процедури
            service.call_insert_procedure(data['order_id'], data['feedback_text'], data['rating'])
            return jsonify({"message": "Feedback created using procedure"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @feedback_controller.route('/order_feedbacks/stats', methods=['GET'])
    def get_feedback_stats():
        operation = request.args.get('operation', default='MAX', type=str)
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT calculate_order_feedback_stat(%s)", (operation,))
            result = cur.fetchone()
            cur.close()
            return jsonify({"result": result[0]})
        except Exception as e:
            return jsonify({"error": str(e)}), 500



    return feedback_controller

    
