from flask import Flask
from flask_mysqldb import MySQL
from .config import Config
from flasgger import Swagger
from .controller.customer_controller import create_customer_controller  
from .controller.customer_card_controller import create_customer_card_controller 
from .controller.product_controller import create_product_controller 
from .controller.company_controller import create_company_controller
from .controller.order_controller import create_order_controller
from .controller.order_item_controller import create_order_item_controller
from .controller.city_controller import create_city_controller
from .controller.delivery_controller import create_delivery_controller 
from .controller.payment_controller import create_payment_controller 
from .controller.review_controller import create_review_controller 
from .controller.wishlist_controller import create_wishlist_controller 
from .controller.product_type_controller import create_product_type_controller 
from .controller.product_attribute_controller import create_product_attribute_controller 
from .controller.order_feedback_controller import create_order_feedback_controller

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
swagger = Swagger(app)

customer_controller = create_customer_controller(mysql)
app.register_blueprint(customer_controller)

customer_card_controller = create_customer_card_controller(mysql)
app.register_blueprint(customer_card_controller)

product_controller = create_product_controller(mysql)
app.register_blueprint(product_controller)

company_controller = create_company_controller(mysql)
app.register_blueprint(company_controller)

order_controller = create_order_controller(mysql)
app.register_blueprint(order_controller) 

order_item_controller = create_order_item_controller(mysql)
app.register_blueprint(order_item_controller)

city_controller = create_city_controller(mysql)
app.register_blueprint(city_controller) 

delivery_controller = create_delivery_controller(mysql)
app.register_blueprint(delivery_controller) 

payment_controller = create_payment_controller(mysql)
app.register_blueprint(payment_controller) 

review_controller = create_review_controller(mysql)
app.register_blueprint(review_controller) 

wishlist_controller = create_wishlist_controller(mysql)
app.register_blueprint(wishlist_controller)

product_type_controller = create_product_type_controller(mysql)
app.register_blueprint(product_type_controller)


product_attribute_controller = create_product_attribute_controller(mysql)
app.register_blueprint(product_attribute_controller)

order_feedback_controller = create_order_feedback_controller(mysql)
app.register_blueprint(order_feedback_controller)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)

