# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('sqlite:///food_ordering.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
