# Raktar App – Warehouse Management System

# Raktar App – Warehouse Management System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

A containerized warehouse inventory web application built with Python (Flask), PostgreSQL, and Docker.

The system provides a simple backend-driven interface for managing warehouse products, including product listing and detailed inventory information such as SKU, quantity, and storage location.

The project demonstrates backend architecture design, relational database integration, and containerized deployment workflows.

---
## Key Features
- Product list retrieval from database
- Detailed product information view (SKU, quantity, location)
- PostgreSQL database integration
- Environment-based configuration management
- Fully containerized setup with Docker & Docker Compose

---

## Architecture Overview

The application follows a layered backend architecture:

- Routes layer – HTTP request handling (Flask routes)
- Service layer – business logic separation
- Database layer – PostgreSQL connection and queries
- Model layer – data structure definitions
- Template layer – basic UI rendering (Jinja2)

This structure ensures separation of concerns and maintainability.

---

## Technology Stack

Backend:
- Python
- Flask

Database:
- PostgreSQL
- psycopg

Infrastructure:
- Docker
- Docker Compose

Other tools:
- python-dotenv (environment variables)

---

## Project Structure
The project follows a layered structure to separate responsibilities.

```
raktar_app
│
├── routes/        # Flask route handlers
├── services/      # Business logic layer
├── db/            # Database connection logic
├── models.py      # Database models
├── templates/     # HTML templates
│
├── app.py         # Flask application factory
├── run.py         # Application entry point
├── wsgi.py        # Production server entry
├── init_db.py     # Database initialization
│
├── Dockerfile
├── Procfile
├── requirements.txt
└── README.md
```

## How to run locally

Install dependencies:

pip install -r requirements.txt


Start the application:

python run.py


Open in browser:

http://localhost:5000


---

## Run with Docker

Build and run:

docker build -t raktar-app .

docker run -p 5000:5000 raktar-app


---

## Project Goals

This project was developed to practice:

- Flask backend development
- REST-style application structure
- PostgreSQL relational database usage
- Layered software architecture
- Containerized deployment with Docker
- Environment-based configuration management

---

## What this project demonstrates

- Backend system design using Python
- Database-driven application development
- Separation of business logic and routing
- Basic DevOps workflow (Docker)
- Production-ready application structure (WSGI support)


