from flask import Blueprint, request, jsonify
from my_project.auth.services.payment_service import PaymentService
import pymysql

def create_payment_controller(mysql):
    payment_controller = Blueprint('payment', __name__)
    service = PaymentService(mysql)

    @payment_controller.route('/payments', methods=['GET'])
    def get_payments():
        payments = service.get_payments()
        return jsonify([payment.to_dict() for payment in payments])

    @payment_controller.route('/payments', methods=['POST'])
    def create_payment():
        data = request.json
        if not data or 'order_id' not in data or 'payment_method' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_payment(data)
            return jsonify({"message": "Payment created"}), 201
        except pymysql.MySQLError as e:
            # Перевірка на повідомлення про помилку від тригера
            if "Payment method cannot end with two zeros (INSERT)" in str(e):
                return jsonify({"error": "Payment method cannot end with two zeros (INSERT)"}), 400
            return jsonify({"error": "Database error occurred during payment insertion"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @payment_controller.route('/payments/<int:payment_id>', methods=['PUT'])
    def update_payment(payment_id):
        data = request.json
        if not data or 'order_id' not in data or 'payment_method' not in data:
            return jsonify({"error": "Invalid data"}), 400
        
        # Перевіряємо, чи нове значення payment_method закінчується на два нулі
        if data['payment_method'].endswith('00'):
            return jsonify({"error": "Payment method cannot end with two zeros (UPDATE)"}), 400
        
        try:
            service.modify_payment(payment_id, data)
            return jsonify({"message": "Payment updated"})
        except pymysql.MySQLError as e:
            # Перевірка на повідомлення про помилку від тригера
            if "Payment method cannot end with two zeros (UPDATE)" in str(e):
                return jsonify({"error": "Payment method cannot end with two zeros (UPDATE)"}), 400
            return jsonify({"error": "Database error occurred during payment update"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @payment_controller.route('/payments/<int:payment_id>', methods=['DELETE'])
    def delete_payment(payment_id):
        try:
        # Спроба видалити запис через сервіс
            service.remove_payment(payment_id)
            return jsonify({"message": "Payment deleted"})
        except pymysql.MySQLError as e:
        # Перевірка, чи виникла помилка через тригер
            if "Deletion of payment records is not allowed" in str(e):
                return jsonify({"error": "Deletion of payment records is not allowed"}), 400
            return jsonify({"error": "Database error occurred during payment deletion"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    return payment_controller
