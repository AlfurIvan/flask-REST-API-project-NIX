"""Config module"""

from os import getenv

POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")


class Config:
    """config class"""
    SQLALCHEMY_DATABASE_URI = getenv("DB_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = getenv("APP_SECRET_KEY")
