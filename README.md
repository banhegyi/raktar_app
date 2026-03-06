# Raktar App

A simple warehouse inventory web application built with Python and Flask.

The application allows users to view products stored in a warehouse and inspect detailed product information
such as SKU, quantity and location. The project demonstrates backend development concepts such as database integration,
environment configuration and containerized deployment.

---

## Features

- Display warehouse product list
- View detailed product information
- PostgreSQL database integration
- Environment-based configuration
- Docker container support

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
- dotenv (environment variables)

---

## Project Structure
The project follows a layered structure to separate responsibilities.

raktar_app
│
├── routes/ → Flask route handlers
├── services/ → business logic layer
├── db/ → database connection logic
├── models.py → database models
├── templates/ → HTML templates
│
├── app.py → Flask application factory
├── run.py → application entry point
├── wsgi.py → production server entry
├── init_db.py → database initialization
│
├── Dockerfile
├── Procfile
├── requirements.txt
└── README.md

## Running the Application

Install dependencies:


pip install -r requirements.txt


Start the application:


python run.py


Open in browser:


http://localhost:5000


---

## Running with Docker

Build and run:


docker build -t raktar-app .
docker run -p 5000:5000 raktar-app


---

## Project Purpose

This project was created to practice:

- Python backend development
- relational database usage
- modular application architecture
- containerized deployment with Docker
