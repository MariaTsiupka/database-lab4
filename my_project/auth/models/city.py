class City:
    def __init__(self, city_id, city_name):
        self.city_id = city_id
        self.city_name = city_name

    def to_dict(self):
        return {
            "city_id": self.city_id,
            "city_name": self.city_name,
        }
