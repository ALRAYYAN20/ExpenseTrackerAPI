# Secure Expense Management

A production-ready REST API for personal expense management built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. Features secure JWT authentication, full CRUD operations, and cloud deployment.

🔗 **Live Demo:** https://expensetrackerapi-it5y.onrender.com/docs  
📦 **GitHub:** https://github.com/ALRAYYAN20/ExpenseTrackerAPI

---

## Features

- 🔐 **JWT Authentication** — Secure register and login with bcrypt password hashing
- 💸 **Expense CRUD** — Create, read, update, and delete expenses
- 🔒 **Protected Routes** — All expense endpoints require valid JWT token
- 👤 **User Ownership** — Users can only access and modify their own expenses
- ✅ **Input Validation** — Strict request validation with Pydantic schemas
- 🐳 **Dockerized** — Fully containerized for consistent deployment
- ☁️ **Cloud Deployed** — Live on Render with Neon PostgreSQL

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| Database | PostgreSQL (Neon) |
| ORM | SQLAlchemy |
| Auth | JWT, bcrypt, OAuth2 |
| Deployment | Docker, Render |
| Validation | Pydantic |
| Server | Uvicorn |

---

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/register` | ❌ | Create a new user account |
| POST | `/login` | ❌ | Login and receive JWT token |
| GET | `/expenses` | ✅ | Get all expenses for logged in user |
| POST | `/expenses` | ✅ | Create a new expense |
| PUT | `/expenses/{id}` | ✅ | Update an existing expense |
| DELETE | `/expenses/{id}` | ✅ | Delete an expense |

---

## Project Structure

```
ExpenseTrackerAPI/
├── app/
│   ├── __init__.py
│   ├── main.py          # App entry point, router registration
│   ├── models.py        # SQLAlchemy User and Expense models
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── database.py      # PostgreSQL connection and session
│   ├── oauth2.py        # JWT token verification
│   └── routers/
│       ├── auth.py      # Register and login endpoints
│       └── expenses.py  # Expense CRUD endpoints
├── Dockerfile
├── requirements.txt
└── .env.example
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Docker (optional)

### 1. Clone the repository

```bash
git clone https://github.com/ALRAYYAN20/ExpenseTrackerAPI.git
cd ExpenseTrackerAPI
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://user:password@localhost/expensetrackerdb
SECRET_KEY=your_secret_key_here
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the API.

---

## Running with Docker

```bash
docker build -t expensetrackerapi .
docker run -p 8000:8000 --env-file .env expensetrackerapi
```

---

## How It Works

### Authentication Flow
```
User registers with username, email, password
        ↓
Password hashed with bcrypt before storing
        ↓
User logs in → JWT token returned
        ↓
Token sent in Authorization header on every request
        ↓
Server verifies token → grants or denies access
```

### Expense Ownership
```
User creates expense
        ↓
owner_id set to current_user from JWT token
        ↓
On update/delete → verify expense.owner_id == current_user
        ↓
If mismatch → 403 Forbidden
If match → proceed with operation
```

---

## Database Schema

### User
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key, Auto Increment |
| username | String(50) | Not Null |
| email | String(100) | Unique, Not Null |
| password | String(255) | Not Null (hashed) |
| created_at | DateTime | Default: now() |

### Expense
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key, Auto Increment |
| title | String | Not Null |
| amount | Float | Not Null |
| category | String | Nullable |
| created_at | DateTime | Default: now() |
| owner_id | Integer | Foreign Key → User.id |

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | JWT signing secret |

---

## Author

**Alrayyan Mukadam**  
[GitHub](https://github.com/ALRAYYAN20) · [LinkedIn](https://www.linkedin.com/in/alrayyan-mukadam-9bb96128b)
