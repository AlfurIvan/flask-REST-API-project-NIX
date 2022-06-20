""""""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.config import Config


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)
