# Django Cart System

A simple Cart System built using Django and Django REST Framework.

## Tech Stack

- Python 3.11.4  
- Django 5.2.1  
- Django REST Framework 3.16.0  
- JWT Authentication (`djangorestframework-simplejwt`)

---

## Setup Instructions

1. Clone the repository  
2. Create and activate virtual environment  
3. Install dependencies  
4. Apply migrations  
5. Create a superuser  
6. Run the server


git clone https://github.com/vasu1511/django-cart-system.git
cd django-cart-system
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



## Authentication (JWT)

| Method | Endpoint              | Description                 |
|--------|-----------------------|-----------------------------|
| POST   | `/api/token/register/` | Register user               |
| POST   | `/api/token/`          | Get access & refresh tokens |
| POST   | `/api/token/refresh/`  | Refresh access token        |

Use token in headers:  
`Authorization: Bearer <access_token>`

---

## Cart API Endpoints

| Method | Endpoint                  | Description               |
|--------|---------------------------|---------------------------|
| GET    | `/api/cart/`              | List all cart items       |
| POST   | `/api/cart/`              | Add item to cart          |
| PUT    | `/api/cart/<id>/`         | Update item quantity      |
| DELETE | `/api/cart/<id>/`         | Remove item from cart     |
| DELETE | `/api/cart/clear/`        | Clear all cart items      |
| GET    | `/api/cart/total/`        | Get total cart price      |
