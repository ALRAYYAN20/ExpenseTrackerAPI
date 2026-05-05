from fastapi import FastAPI
from .database import engine
from . import models
from . routers import auth, expenses
models.Base.metadata.create_all(bind=engine)
#This tells SQLAlchemy to look at all your models and create the actual tables in PostgreSQL automatically when the app starts.

app = FastAPI()

app.include_router(auth.router)
app.include_router(expenses.router)

@app.get('/')
def root():
    return {'message': 'Expense Tracker API'}