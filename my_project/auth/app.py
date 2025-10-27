from flask import Flask
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

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
swagger = Swagger(app)

@app.route('/')
def index():
    return "API працює!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
