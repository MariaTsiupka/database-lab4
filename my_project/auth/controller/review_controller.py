from flask import Blueprint, request, jsonify
from my_project.auth.services.review_service import ReviewService

def create_review_controller(mysql):
    review_controller = Blueprint('review', __name__)
    service = ReviewService(mysql)

    @review_controller.route('/reviews', methods=['GET'])
    def get_reviews():
        reviews = service.get_reviews()
        return jsonify([review.to_dict() for review in reviews])


    @review_controller.route('/reviews', methods=['POST'])
    def create_review():
        data = request.json
        if not data or 'product_id' not in data or 'customer_id' not in data or 'review_text' not in data or 'rating' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.add_review(data)
            return jsonify({"message": "Review created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @review_controller.route('/reviews/<int:review_id>', methods=['PUT'])
    def update_review(review_id):
        data = request.json
        if not data or 'product_id' not in data or 'customer_id' not in data or 'review_text' not in data or 'rating' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_review(review_id, data)
            return jsonify({"message": "Review updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @review_controller.route('/reviews/<int:review_id>', methods=['DELETE'])
    def delete_review(review_id):
        try:
            service.remove_review(review_id)
            return jsonify({"message": "Review deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return review_controller
