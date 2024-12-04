from flask_sqlalchemy import SQLAlchemy  # type: ignore

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    pan = db.Column(db.String, nullable=True)

class Product(db.Model):
    name = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
    cost_per_user = db.Column(db.Float, nullable=False)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.String, db.ForeignKey('customer.id'), nullable=False)
    product_name = db.Column(db.String, db.ForeignKey('product.name'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    users_subscribed = db.Column(db.Integer, nullable=False)
