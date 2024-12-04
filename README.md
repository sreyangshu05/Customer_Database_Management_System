# Customer Database Management System

XYZ Enterprises is a SaaS product company offering subscription-based products to its customers. This system manages customer subscriptions, providing functionality to add, extend, or end subscriptions, and generate revenue reports.

## Features

### 1. Add Product Subscription
- **Functionality**:
  - Allows the user to:
    - Select a customer from a dropdown.
    - Select a product.
    - Enter start date, end date, and number of users.
- **Validation**:
  - Ensures no active subscription exists for the same customer-product combination.
  - Alerts the user if such a subscription exists.

### 2. Extend Subscription
- **Functionality**:
  - Enables the user to:
    - Edit an existing subscription.
    - Extend the subscription end date.

### 3. End Subscription
- **Functionality**:
  - Allows the user to:
    - Select an existing subscription.
    - Set the subscription end date to today.

### 4. Revenue Report
- **Functionality**:
  - Generates a report showing the total revenue earned till date from all subscriptions.

## Installation and Usage

1. **Setup**:
   ```bash
   cd backend
   python Flask Flask-Cors Flask-SQLAlchemy
   cd subscription-module
   npm install

2. **Run the Application**:
   ```bash
   cd backend
   python app.py
   cd subscription-module
   npm start

3. **Validation**:
   - The application performs strict validation on all user inputs to maintain data integrity.

## Future Enhancements
- Add support for monthly subscriptions.
- Implement automated email notifications for subscription renewals.
- Provide analytical dashboards for detailed customer insights.

## Tech - Stack
- Frontend: ReactJS
- Backend: Flask
- Database: SQLite
