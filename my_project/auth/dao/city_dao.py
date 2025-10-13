from ..models.city import City

class CityDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_cities(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM city")
        rows = cur.fetchall()
        cur.close()
        return [City(city_id=row[0], city_name=row[1]) for row in rows]

    def insert_city(self, city_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO city (city_name) VALUES (%s)",
            (city_data["city_name"],)
        )
        self.mysql.connection.commit()
        cur.close()

    def update_city(self, city_id, city_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE city SET city_name = %s WHERE city_id = %s",
            (city_data["city_name"], city_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_city(self, city_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM city WHERE city_id = %s", (city_id,))
        self.mysql.connection.commit()
        cur.close()
