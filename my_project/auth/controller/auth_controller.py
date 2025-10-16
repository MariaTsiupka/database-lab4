from http import HTTPStatus
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, Response, make_response, jsonify
from werkzeug.security import check_password_hash
from app import mysql  # імпорт об'єкта MySQL з app.py

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post("/login")
def login() -> Response:
    """
        Login
        ---
        parameters:
        - name: body
          in: body
          required: true
          schema:
            type: object
            properties:
              email:
                type: string
                example: "example@email.com"
              password:
                type: string
                example: "password123"
        responses:
          200:
            description: Login successful
            schema:
              type: object
              properties:
                access_token:
                  type: string
                  example: "<access_token>"
          404:
            description: Not found or bad password
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT customer_id, password FROM customer WHERE customer_email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if user and check_password_hash(user[1], password):
        access_token = create_access_token(identity=str(user[0]))
        return make_response(jsonify({'access_token': access_token}), HTTPStatus.OK)

    return make_response(jsonify({"message": f"Not found customer {email} or bad password"}), HTTPStatus.NOT_FOUND)
