from dao.order_feedback_dao import OrderFeedbackDAO

class OrderFeedbackService:
    def __init__(self, mysql):
        self.dao = OrderFeedbackDAO(mysql)

    def get_feedbacks(self):
        return self.dao.get_all_feedbacks()

    def get_feedback_by_order(self, order_id):
        return self.dao.get_feedback_by_order_id(order_id)

    def add_feedback(self, feedback_data):
        self.dao.insert_feedback(feedback_data)

    def modify_feedback(self, feedback_id, feedback_data):
        self.dao.update_feedback(feedback_id, feedback_data)

    def remove_feedback(self, feedback_id):
        self.dao.delete_feedback(feedback_id)

    def call_insert_procedure(self, order_id, feedback_text, rating):
        feedback_data = {
            "order_id": order_id,
            "feedback_text": feedback_text,
            "rating": rating
        }
        self.dao.insert_feedback(feedback_data)
