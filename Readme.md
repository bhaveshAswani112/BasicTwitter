# Basic Twitter

Basic Twitter is a simplified version of Twitter built with Django. It allows users to create, view, search, and manage tweets. Users can also register, log in, and log out of the application.

## Features

- User authentication (registration, login, logout)
- Create, edit, and delete tweets
- View all tweets
- Search for tweets by content
- Responsive design with Bootstrap

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- pip (Python package installer)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/basic-twitter.git
   cd basic-twitter
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`

3. **Install the required packages:**

   ```bash
    pip install -r requirements.txt

4. **Apply the migrations:**

   ```bash
    python manage.py migrate

5. **Create a superuser:**
   ```bash
    python manage.py createsuperuser

6. **Run the development server:**

   ```bash
    python manage.py runserver

7. **Open your browser and visit:**

   ```bash
    http://127.0.0.1:8000
