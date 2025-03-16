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
    __tablename__ = 'tile'
    id = Column(Integer, primary_key=True, autoincrement=True)
    num = Column(Integer, nullable=True)
    point = relationship('point', back_populates='tile')
    json = Column(String(10 ** 5), nullable=True)

class point(Base):
    __tablename__ = 'point'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tile_id = Column(Integer, ForeignKey('tile.id'))
    tile = relationship('tile', back_populates='point')
    num = Column(Integer, nullable=False)
    mean = Column(Integer, nullable=False)

class station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    radius = Column(Integer, nullable=False)

class base_point(Base):
    __tablename__ = 'base_point'
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