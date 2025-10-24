# Django eCommerce Website

A fully-functional eCommerce website built with Django.

## Features

- User authentication
- Product catalog
- Shopping cart
- Secure checkout with Stripe
- Order management
- Product categories
- Product search
- Responsive design

## Setup Instructions

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create .env file and add your Stripe keys:
   
   STRIPE_PUBLIC_KEY=your_stripe_public_key
   STRIPE_SECRET_KEY=your_stripe_secret_key
   
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`

## Usage

- Access admin panel at `/admin`
- Browse products at homepage
- Add products to cart
- Proceed to checkout

## License

MIT License