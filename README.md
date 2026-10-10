#  CyberAI Academy — Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![HTML5](https://img.shields.io/badge/Frontend-HTML5%20%2F%20CSS3-orange?logo=html5)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive, responsive, and secure full-stack web platform designed to present cybersecurity and AI courses, facilitate student registrations, and manage safety contact reports. Built as part of the Meta Django Development curriculum guidelines using pure Python, Django MVT pattern, and CSS.

---

##  Features

- ** Course Catalog**: View available cybersecurity and AI courses fetched dynamically from the database.
- ** Online Enrollment System**: Functional registration forms backed by Django `ModelForm` with automated field validations.
- ** Contact & Security Reporting**: Custom contact interface allowing users to submit inquiries or report security incidents directly to administration.
- ** Admin Dashboard**: Full administrative portal (`/admin/`) for managing courses, reviewing enrollment lists, and managing messages.
- ** Responsive UI**: Custom CSS layout following clean UI design principles with modern layout techniques.
- **Secure Architecture**: Built-in Django protections against CSRF attacks, SQL injection, and unauthorized data modifications.

---

## Project Structure

```text
cyber_ai_academy/
│
├── core/                   # Django Project Configuration Directory
│   ├── settings.py         # App Settings & DB Configuration
│   ├── urls.py             # Main Routing Configuration
│   └── wsgi.py             # WSGI Application Entrypoint
│
├── academy/                # Core Application Directory
│   ├── models.py           # Database Models (Course, Enrollment, ContactMessage)
│   ├── views.py            # Business Logic & Dynamic Rendering
│   ├── forms.py            # ModelForm Validations & Fields
│   ├── urls.py             # App-level Route Endpoints
│   └── admin.py            # Admin Panel Interface Registration
│
├── templates/              # HTML Templates (Template Inheritance)
│   ├── base.html           # Core Page Structure
│   └── academy/            # Specific Page Templates
│
├── static/                 # Static Assets
│   └── css/
│       └── style.css       # Main Application Stylesheet
│
├── db.sqlite3              # Local SQLite Database
├── manage.py               # Django CLI Script
├── requirements.txt        # Python Dependencies List
└── README.md               # Project Documentation
