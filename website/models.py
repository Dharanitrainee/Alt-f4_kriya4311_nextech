from flask_sqlalchemy import SQLAlchemy
from . import db
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class database(Base):
    __tablename__ = 'Users'
    id = Column("id",Integer,primary_key=True)
    roll_number = Column("roll_number", String(11), unique=True, nullable=False)
    password = Column("password", String, nullable=False)
   

    def __init__(self,roll_number,password):
        self.roll_number = roll_number
        self.password = password

    def __repr__(self):
        return f" ({self.password}) ({self.roll_number})"

engine = create_engine("sqlite:///mydb.db", echo=True, future=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
sessions = Session()

sample_users = [
    {"roll_number": "23l421", "password": "password1"},
    {"roll_number": "23n433", "password": "password2"},
    {"roll_number": "23n435", "password": "password3"},
]

for user_data in sample_users:
    new_user = database(**user_data)
    sessions.add(new_user)

try:
    sessions.commit()
    print("Sample users added successfully!")
except IntegrityError:
    sessions.rollback()
    print("Error: Sample users already exist in the database or there was an integrity error.")