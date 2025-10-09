class Company:
    def __init__(self, company_id, company_name):
        self.company_id = company_id
        self.company_name = company_name

    def to_dict(self):
        return {
            "company_id": self.company_id,
            "company_name": self.company_name,
        }