from models import db, Customer, Product, Subscription
from app import app
from datetime import date

with app.app_context():
    # Customers
    customers = [
        Customer(id="C001", name="John Doe", pan="AAOPM5555T"),
        Customer(id="C002", name="Jane Smith", pan="AAQPM1234R"),
        Customer(id="C003", name="Robert Brown", pan="AAGPM9876K"),
        Customer(id="C004", name="Alice Johnson", pan="AANPM6543J"),
        Customer(id="C005", name="Charlie Wilson", pan="AACPM3210Z"),
    ]

    # Products
    products = [
        Product(name="ProductA", description="Cloud Storage Service", cost_per_user=50.0),
        Product(name="ProductB", description="AI Analytics Tool", cost_per_user=100.0),
        Product(name="ProductC", description="Project Management App", cost_per_user=75.0),
        Product(name="ProductD", description="CRM Software", cost_per_user=120.0),
    ]

    # Subscriptions
    subscriptions = [
        Subscription(customer_id="C001", product_name="ProductA", start_date=date(2024, 1, 1), end_date=date(2024, 12, 31), users_subscribed=5),
        Subscription(customer_id="C002", product_name="ProductB", start_date=date(2024, 2, 1), end_date=date(2025, 1, 31), users_subscribed=3),
        Subscription(customer_id="C003", product_name="ProductC", start_date=date(2024, 3, 1), end_date=date(2024, 8, 31), users_subscribed=10),
        Subscription(customer_id="C004", product_name="ProductD", start_date=date(2024, 4, 1), end_date=date(2024, 12, 31), users_subscribed=8),
        Subscription(customer_id="C005", product_name="ProductA", start_date=date(2024, 5, 1), end_date=date(2024, 11, 30), users_subscribed=2),
        Subscription(customer_id="C001", product_name="ProductB", start_date=date(2024, 6, 1), end_date=date(2024, 12, 31), users_subscribed=4),
        Subscription(customer_id="C002", product_name="ProductC", start_date=date(2024, 7, 1), end_date=date(2025, 6, 30), users_subscribed=6),
        Subscription(customer_id="C003", product_name="ProductD", start_date=date(2024, 8, 1), end_date=date(2024, 12, 31), users_subscribed=7),
        Subscription(customer_id="C004", product_name="ProductA", start_date=date(2024, 9, 1), end_date=date(2024, 11, 30), users_subscribed=9),
        Subscription(customer_id="C005", product_name="ProductB", start_date=date(2024, 10, 1), end_date=date(2025, 9, 30), users_subscribed=3),
    ]

    # Add to database
    db.session.add_all(customers + products + subscriptions)
    db.session.commit()
