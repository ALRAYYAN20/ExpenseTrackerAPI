# Expense Tracker API

A REST API built with FastAPI and PostgreSQL.

## Features
- User registration and login with JWT authentication
- Password hashing with bcrypt
- Full CRUD for expenses
- Protected routes

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- python-jose (JWT)
- passlib (bcrypt)

## Setup
1. Clone the repo
2. Create virtual environment and install dependencies:
   pip install -r requirements.txt
3. Create a .env file with:
   DATABASE_URL=postgresql://user:password@localhost/dbname
   SECRET_KEY=yoursecretkey
4. Run:
   uvicorn app.main:app --reload

## Endpoints
- POST /register - Create account
- POST /login - Get JWT token
- GET /expenses - Get all expenses
- POST /expenses - Create expense
- PUT /expenses/{id} - Update expense
- DELETE /expenses/{id} - Delete expense
