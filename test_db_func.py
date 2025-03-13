from numpy.random.mtrand import permutation

from __init__db import User
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'sqlite:///Database.db'
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

def add_user(response):
    session = Session()
    new_user = User(
        first_name=response['name'],
        last_name=response['surname'],
        middle_name = response['patronymic'],
        email=response['email'],
        is_admin=True,
        confirmed = False,
    )
    new_user.set_password(response['password'])
    session.add(new_user)
    session.commit()

def is_confirmed(email):
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    return user.confirmed

def is_existing(email):
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    if user:
        return True
    return False

def set_confirmed(email):
    session = Session()
    user = session.query(User).filter_by(email=email).first()
    print(user.confirmed)
    user.confirmed = 1
    print(user.confirmed)
    session.commit()

