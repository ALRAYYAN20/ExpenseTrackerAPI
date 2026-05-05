from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db
from ..oauth2 import get_current_user
from ..schemas import ExpenseCreate, ExpenseUpdate

router = APIRouter()

# GET    /expenses        — get all expenses for logged in user
# POST   /expenses        — create a new expense
# PUT    /expenses/{id}   — update an expense
# DELETE /expenses/{id}   — delete an expense

# Function 1 — Get all expenses:

# Hits GET /expenses
# Queries database for all expenses where owner_id matches the logged in user
# Returns the list
@router.get('/expenses/')
def get_expense(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    all_expense = db.query(models.Expense).filter(models.Expense.user_id == current_user).all()
    return all_expense   


# Function 2 — Create expense:

# Hits POST /expenses
# Takes expense data from request body using ExpenseCreate schema
# Creates new Expense object, sets owner_id to current user
# Saves to DB and returns it

# Decorator: @router.post('/expenses/')
# Takes expense: ExpenseCreate as request body
# Takes db and current_user as dependencies
# Creates a new models.Expense object
# Sets user_id = current_user
# Saves to DB with add, commit, refresh
# Returns the new expense
@router.post('/expenses/')
def create_expense( expense: ExpenseCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    # creates new object and saves to db
    create_exp = models.Expense(title = expense.title, amount = expense.amount, category = expense.category, user_id = current_user)

    db.add(create_exp)
    db.commit()
    db.refresh(create_exp)
    return {'message' : 'Expense created successfully'}
    

# Function 3 — Update expense:

# Hits PUT /expenses/{id}
# Finds expense by id
# Check if it belongs to current user — if not, raise 403
# Update fields and save

@router.put('/expenses/{expense_id}')
def update_expense(expense_id: int, expense_data: ExpenseUpdate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    update_exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not update_exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    # 2. Ownership check
    if update_exp.user_id != current_user:
        raise HTTPException(status_code=403, detail="Not authorized")

    # 3. Update fields

    if expense_data.title is not None:
        update_exp.title = expense_data.title

    if expense_data.amount is not None:
        update_exp.amount = expense_data.amount

    if expense_data.category is not None:
        update_exp.category = expense_data.category

    # 4. Save changes
    db.commit()
    db.refresh(update_exp)
    return { 'message' : 'Expenses update successfully'}

# Function 4 — Delete expense:

# Hits DELETE /expenses/{id}
# Finds expense by id
# Check if it belongs to current user — if not, raise 403
# Delete it and return success message

@router.delete('/expense/{expense_id}')
def delete_expense(expense_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    delete_exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not delete_exp:
        raise HTTPException (status_code = 404, detail = 'Expense not found')
    
    if delete_exp.user_id != current_user:
        raise HTTPException (status_code = 403, detail = 'Not authorized')
    
    db.delete(delete_exp)
    db.commit()
    return {'message': 'Expense deleted successfully'}