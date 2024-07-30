# Online_Shopping_Platform

## Overview
The Online Shopping Platform is a demonstration of an e-commerce system, allowing users to browse, select, and purchase products online. It covers various aspects of an e-commerce system, including product categorization, shopping cart management, order processing, and payment integration.

## Features
- **Product Categories:** Electronics, Clothing, and more.
- **Shopping Cart:** Add, remove, and update items.
- **Order Processing:** Create and manage orders.
- **Payment Integration:** Supports multiple payment methods.
- **Design Patterns:** Implemented using several design patterns for maintainability and scalability.

## Project Structure
- `abstract_order.py`: Defines the abstract base class for orders.
- `abstract_payment.py`: Defines the abstract base class for payment methods.
- `abstract_products.py`: Abstract base class for products.
- `clothing_products.py`: Contains classes related to clothing items.
- `electronic_product.py`: Contains classes related to electronic items.
- `item.py`: Represents an individual item in the platform.
- `main.py`: Entry point of the application.
- `order.py`: Manages order creation and processing.
- `payment_factory.py`: Factory pattern for creating payment method instances.
- `shopping_cart.py`: Manages the shopping cart and its items.
