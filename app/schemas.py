from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseUpdate(BaseModel):
    title : Optional[str] = None
    amount : Optional[float] = None 
    category : Optional[str] = None 
