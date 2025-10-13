from ..models.company import Company

class CompanyDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_companies(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM company")
        rows = cur.fetchall()
        cur.close()
        return [
            Company(
                company_id=row[0],
                company_name=row[1]
            )
            for row in rows
        ]

    def insert_company(self, company_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "INSERT INTO company (company_name) VALUES (%s)",
            (company_data["company_name"],)
        )
        self.mysql.connection.commit()
        cur.close()

    def update_company(self, company_id, company_data):
        cur = self.mysql.connection.cursor()
        cur.execute(
            "UPDATE company SET company_name = %s WHERE company_id = %s",
            (company_data["company_name"], company_id)
        )
        self.mysql.connection.commit()
        cur.close()

    def delete_company(self, company_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM company WHERE company_id = %s", (company_id,))
        self.mysql.connection.commit()
        cur.close()
