from dao.company_dao import CompanyDAO

class CompanyService:
    def __init__(self, mysql):
        self.dao = CompanyDAO(mysql)

    def get_companies(self):
        return self.dao.get_all_companies()

    def add_company(self, company_data):
        return self.dao.insert_company(company_data)

    def modify_company(self, company_id, company_data):
        return self.dao.update_company(company_id, company_data)

    def remove_company(self, company_id):
        return self.dao.delete_company(company_id)
