# Smart Clinic

A web-based clinic management system built with **Django**. Patients can register, log in and book appointments, and doctors get their own dashboard to manage them.

## Features

- Patient sign up and login
- Role-based login (patient / doctor)
- Patient dashboard
- Doctor dashboard
- Book an appointment
- Django admin panel for managing data

## Tech Stack

- Python
- Django 5.2
- SQLite
- HTML and CSS

## Screenshots

> Add your screenshots to a `screenshots` folder, then update the paths below.

| Home | Login |
|---|---|
| ![Home](screenshots/home.png) | ![Login](screenshots/login.png) |

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ber22751-cmd/smart_clinic_1.git
   cd smart_clinic_1
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Create the database:
   ```bash
   python manage.py migrate
   ```
5. (Optional) Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```
7. Open http://127.0.0.1:8000 in your browser.

## Project Structure

```
smart_clinic_1/
├── core/            # Main app: models, views, forms, templates
├── smart_clinic/    # Project settings and URLs
└── manage.py
```

## Author

Basmala
