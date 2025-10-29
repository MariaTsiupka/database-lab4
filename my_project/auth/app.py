from flask import Flask, jsonify
from flask_mysqldb import MySQL
from my_project.auth.config import Config
from flasgger import Swagger

from my_project.auth.controller.customer_controller import create_customer_controller  
from my_project.auth.controller.customer_card_controller import create_customer_card_controller 
from my_project.auth.controller.product_controller import create_product_controller 
from my_project.auth.controller.company_controller import create_company_controller
from my_project.auth.controller.order_controller import create_order_controller
from my_project.auth.controller.order_item_controller import create_order_item_controller
from my_project.auth.controller.city_controller import create_city_controller
from my_project.auth.controller.delivery_controller import create_delivery_controller 
from my_project.auth.controller.payment_controller import create_payment_controller 
from my_project.auth.controller.review_controller import create_review_controller 
from my_project.auth.controller.wishlist_controller import create_wishlist_controller
from my_project.auth.controller.product_type_controller import create_product_type_controller
from my_project.auth.controller.product_attribute_controller import create_product_attribute_controller
from my_project.auth.controller.order_feedback_controller import create_order_feedback_controller

import os

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
swagger = Swagger(app)

# Реєстрація Blueprints
app.register_blueprint(create_customer_controller(mysql))
app.register_blueprint(create_customer_card_controller(mysql))
app.register_blueprint(create_product_controller(mysql))
app.register_blueprint(create_company_controller(mysql))
app.register_blueprint(create_order_controller(mysql))
app.register_blueprint(create_order_item_controller(mysql))
app.register_blueprint(create_city_controller(mysql))
app.register_blueprint(create_delivery_controller(mysql))
app.register_blueprint(create_payment_controller(mysql))
app.register_blueprint(create_review_controller(mysql))
app.register_blueprint(create_wishlist_controller(mysql))
app.register_blueprint(create_product_type_controller(mysql))
app.register_blueprint(create_product_attribute_controller(mysql))
app.register_blueprint(create_order_feedback_controller(mysql))

# Для перевірки всіх маршрутів
print("Доступні маршрути:")
print(app.url_map)

@app.route('/')
def index():
    return "API працює!"

# Тестовий endpoint для Azure
@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
