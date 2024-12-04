from flask import Blueprint, request, jsonify
from models import db, Customer, Product, Subscription
from datetime import datetime, date

subscription_bp = Blueprint('subscriptions', __name__)
customer_bp = Blueprint('customers', __name__)
product_bp = Blueprint('products', __name__)

# Customers Route
@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in customers]), 200

# Products Route
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'name': p.name, 'description': p.description} for p in products]), 200

# Subscriptions Routes
@subscription_bp.route('/subscriptions', methods=['POST'])
def add_subscription():
    data = request.json
    customer_id = data.get('customer_id')
    product_name = data.get('product_name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    users_subscribed = data.get('users_subscribed')

    # Validate customer and product existence
    if not Customer.query.get(customer_id):
        return jsonify({'error': 'Customer does not exist'}), 400
    if not Product.query.get(product_name):
        return jsonify({'error': 'Product does not exist'}), 400

    # Check for active subscription
    active_subscription = Subscription.query.filter_by(
        customer_id=customer_id, product_name=product_name
    ).filter(Subscription.end_date >= date.today()).first()
    if active_subscription:
        return jsonify({'error': 'Active subscription already exists for this customer and product'}), 400

    # Add the subscription
    subscription = Subscription(
        customer_id=customer_id,
        product_name=product_name,
        start_date=datetime.strptime(start_date, '%Y-%m-%d').date(),
        end_date=datetime.strptime(end_date, '%Y-%m-%d').date(),
        users_subscribed=users_subscribed
    )
    db.session.add(subscription)
    db.session.commit()

    return jsonify({'message': 'Subscription added successfully'}), 201

@subscription_bp.route('/subscriptions/<int:id>', methods=['PATCH'])
def extend_subscription(id):
    data = request.json
    new_end_date = data.get('end_date')

    subscription = Subscription.query.get(id)
    if not subscription:
        return jsonify({'error': 'Subscription not found'}), 404

    subscription.end_date = datetime.strptime(new_end_date, '%Y-%m-%d').date()
    db.session.commit()

    return jsonify({'message': 'Subscription extended successfully'}), 200

@subscription_bp.route('/subscriptions/<int:id>', methods=['DELETE'])
def end_subscription(id):
    subscription = Subscription.query.get(id)
    if not subscription:
        return jsonify({'error': 'Subscription not found'}), 404

    subscription.end_date = date.today()
    db.session.commit()

    return jsonify({'message': 'Subscription ended successfully'}), 200

@subscription_bp.route('/revenue', methods=['GET'])
def revenue_report():
    subscriptions = Subscription.query.all()
    total_revenue = 0.0

    for subscription in subscriptions:
        product = Product.query.get(subscription.product_name)
        duration_in_years = (subscription.end_date - subscription.start_date).days / 365
        revenue = product.cost_per_user * subscription.users_subscribed * duration_in_years
        total_revenue += revenue

    return jsonify({'total_revenue': total_revenue}), 200
