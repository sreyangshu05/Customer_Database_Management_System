from flask import Flask  # type: ignore
from flask_cors import CORS  # type: ignore
from models import db, Customer, Product, Subscription
from routes import subscription_bp, customer_bp, product_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)
app.register_blueprint(subscription_bp)
app.register_blueprint(customer_bp)  # Register customers route
app.register_blueprint(product_bp)   # Register products route

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)