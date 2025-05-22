# Ecommerce Django Project

## Project Description
This is a full-featured Ecommerce web application built using Django framework. The project leverages MongoDB as the primary database for storing product and order information, while using SQLite for user authentication and session management. It supports user registration, login (including Google social login), product browsing, shopping cart management, and order checkout.

## Features
- User authentication with Django's built-in system and social login via Google (using django-allauth).
- Product listing and browsing with details fetched from MongoDB.
- Shopping cart functionality with add, remove, and view cart features.
- Order checkout process that saves orders to MongoDB.
- User session management with persistent cart storage.
- Contact page for user inquiries.
- Responsive and user-friendly UI using Django templates and static assets.

## Technologies Used
- Python 3.x
- Django Web Framework
- MongoDB (via pymongo) for product and order data
- SQLite for authentication and session data
- django-allauth for social authentication (Google)
- HTML, CSS, JavaScript for frontend templates and static files

## Installation and Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Ecommerce-django-NEMO-
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Update MongoDB connection string in `LA1/views.py` or use environment variables as preferred.
   - Ensure Django `SECRET_KEY` and other sensitive settings are set securely.

5. Run database migrations for Django's auth and sessions:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000/`

## Usage

- Visit the home page to browse products.
- Register or login using email or Google social login.
- Add products to your cart and manage quantities.
- Proceed to checkout to place your order.
- Use the contact page to send inquiries.

## Project Structure

```
Ecommerce-django-NEMO-/
│
├── LA1/                      # Main Django app
│   ├── templates/LA1/        # HTML templates for views
│   ├── views.py              # View functions handling requests
│   ├── urls.py               # URL routing for the app
│   ├── models.py             # (Empty - MongoDB used for data)
│   └── static/               # Static assets (CSS, JS)
│
├── NEMO/                     # Django project settings
│   ├── settings.py           # Project settings and configurations
│   ├── urls.py               # Project-level URL routing
│   └── wsgi.py               # WSGI application entry point
│
├── db.sqlite3                # SQLite database for auth and sessions
├── manage.py                 # Django management script
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

## Authentication

- Uses Django's built-in authentication system.
- Supports social login with Google via django-allauth.
- Login redirects to home page; logout redirects to home.

## Database

- MongoDB is used to store product and order data, accessed via pymongo in views.
- SQLite is used for user authentication and session management.

## Contact

For any questions or support, please use the Contact page in the application.

---

This project is currently under active development and may receive further updates and improvements.
