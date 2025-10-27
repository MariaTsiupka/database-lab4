from my_project.auth.dao.city_dao import CityDAO

class CityService:
    def __init__(self, mysql):
        self.dao = CityDAO(mysql)

    def get_cities(self):
        return self.dao.get_all_cities()

    def add_city(self, city_data):
        return self.dao.insert_city(city_data)

    def modify_city(self, city_id, city_data):
        return self.dao.update_city(city_id, city_data)

    def remove_city(self, city_id):
        return self.dao.delete_city(city_id)
