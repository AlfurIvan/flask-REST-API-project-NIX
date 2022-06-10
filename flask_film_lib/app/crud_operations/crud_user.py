"""CRUD for user table"""

from typing import Union, Dict, Any
from json import loads
from werkzeug.security import generate_password_hash
from crud_base import BaseCRUD
from app.models.models import Users
from app.models.db import db
from app.schemas.users import UserCreate, UserBase, UserList, UserUpdate


class UserCRUD(BaseCRUD[Users, UserCreate, UserUpdate]):
    """Users CRUDs over BaseCRUD for User`s model"""

    def create(self, db_session: db.session,
               new_obj: Union[UserCreate, Dict[str, Any]], **kwargs) -> UserBase:
        """"""
        enc_obj = loads(new_obj)
        enc_obj['password'] = \
            generate_password_hash(enc_obj['password'], method='pbkdf2:sha256')
        db_obj = self.model(**enc_obj)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return self.schema.from_orm(db_obj)


user = UserCRUD(Users, UserBase, UserList)
