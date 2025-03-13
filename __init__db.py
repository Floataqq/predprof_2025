from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("Database.db"):
    print("\u001b[35;1m Killed all goidas \u001b[0m")
    os.remove("Database.db")

database_url = 'sqlite:///Database.db'
engine = create_engine(database_url)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), unique=False, nullable=False)
    last_name = Column(String(100), unique=False, nullable=True)
    middle_name = Column(String(100), unique=False, nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, unique=False, default=datetime.now)
    is_admin = Column(Boolean, unique=False, default=False)
    password_hash = Column(String(128), nullable=False)
    confirmed = Column(Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(
    first_name='admin',
    email='admin@admin.com',
    set_password='123',
    is_admin=True
)

session.add(new_user)
session.commit()
session.close()