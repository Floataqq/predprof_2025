from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, foreign, relationship
import os


if os.path.exists("Database.db"):
    print("\u001b[35;1m Killed all goidas \u001b[0m")
    os.remove("Database.db")

database_url = 'sqlite:///Database.db'
engine = create_engine(database_url)
Base = declarative_base()

class tile(Base):
    __tablename__ = 'tiles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    left_id = Column(Integer, nullable=True)
    up_id = Column(Integer, nullable=True)
    point = relationship('points', back_populates='tiles')
    json = Column(String(10 ** 5), nullable=True)

class point(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tile_id = Column(Integer, ForeignKey('Tiles.id'))
    tile = relationship('tiles', back_populates='points')
    num = Column(Integer, nullable=False)
    mean = Column(Integer, nullable=False)

class station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    radius = Column(Integer, nullable=False)

class base_point(Base):
    __tablename__ = 'base_points'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()