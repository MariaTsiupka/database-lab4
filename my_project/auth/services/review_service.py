from dao.review_dao import ReviewDAO

class ReviewService:
    def __init__(self, mysql):
        self.dao = ReviewDAO(mysql)

    def get_reviews(self):
        return self.dao.get_all_reviews()

    def add_review(self, review_data):
        return self.dao.insert_review(review_data)

    def modify_review(self, review_id, review_data):
        return self.dao.update_review(review_id, review_data)

    def remove_review(self, review_id):
        return self.dao.delete_review(review_id)
