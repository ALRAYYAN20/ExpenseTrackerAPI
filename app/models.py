# Write two SQLAlchemy models — User and Expense.
# User should have:

# id (primary key, auto increment)
# username (string, unique, can't be null)
# email (string, unique, can't be null)
# password (string, can't be null)
# created_at (datetime, defaults to now)

# Expense should have:

# id (primary key, auto increment)
# title (string, can't be null)
# amount (float, can't be null)
# category (string)
# date (datetime)
# owner_id (foreign key → links to User's id)

import sqlalchemy
from datetime import datetime
from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    id = mapped_column(Integer, primary_key = True)
    # int column created and primary key = True means, ids will auto increament from 1
    username : Mapped[str] = mapped_column(String(50))
    # creates column just like above , this syntax is shortcut, CANNOT BE NULL
    email : Mapped[str] = mapped_column(String (100), unique = True, nullable = False)
    # same, cannot be null
    password : Mapped[str] = mapped_column(String (255))
    # same , max str lenght 8 chrs
    create_date : Mapped[datetime] = mapped_column(insert_default = func.now())
    # notes time when data was created
    expense_relation = relationship('Expense', back_populates = 'user_relation')
 
class Expense(Base):
    __tablename__ = 'expense'

    id = mapped_column(Integer, primary_key = True)
    # int column created and primary key = True means, ids will auto increament from 1
    title : Mapped[str]
    amount : Mapped[float]
    category : Mapped[str]
    create_date : Mapped[datetime] = mapped_column(insert_default = func.now())
    user_id = mapped_column(ForeignKey('user.id'))
    user_relation = relationship('User', back_populates = 'expense_relation')

    