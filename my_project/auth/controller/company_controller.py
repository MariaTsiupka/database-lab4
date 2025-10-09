from flask import Blueprint, request, jsonify
from services.company_service import CompanyService

def create_company_controller(mysql):
    company_controller = Blueprint('company', __name__)
    service = CompanyService(mysql)

    @company_controller.route('/companies', methods=['GET'])
    def get_companies():
        companies = service.get_companies()
        return jsonify([company.to_dict() for company in companies])

    @company_controller.route('/companies', methods=['POST'])
    def create_company():
        data = request.json
        if not data or 'company_name' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.add_company(data)
            return jsonify({"message": "Company created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @company_controller.route('/companies/<int:company_id>', methods=['PUT'])
    def update_company(company_id):
        data = request.json
        if not data or 'company_name' not in data:
            return jsonify({"error": "Invalid data"}), 400
        try:
            service.modify_company(company_id, data)
            return jsonify({"message": "Company updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @company_controller.route('/companies/<int:company_id>', methods=['DELETE'])
    def delete_company(company_id):
        try:
            service.remove_company(company_id)
            return jsonify({"message": "Company deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return company_controller
