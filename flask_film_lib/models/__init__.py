from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin:

    @classmethod
    def create(cls, *args, **kwargs):
        session = db.session()
        obj = cls(*args, **kwargs)
        session.add(obj)
        session.flush()
        session.commit()
        return obj
