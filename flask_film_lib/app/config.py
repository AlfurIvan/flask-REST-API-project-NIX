"""Config module"""

POSTGRES_USER = 'user'
POSTGRES_PASSWORD = 'pss'

DEFAULT_PAGINATION_VALUE = 10


class Config:
    """config class"""
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://$user:pss@0.0.0.0:5432/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xdb-\xbd\x84y.\n\xa8B8\xd6\xb7FP\xa0\xe4\x96\x9ew\x188Q\xd2\xa9'
