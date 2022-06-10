""""""

import re
from typing import List
from pydantic import BaseModel,EmailStr, constr, validator


class UserBase(BaseModel):
    """"""
    name: constr(max_length=40)
    email: EmailStr

    @validator("name")
    def validate_name(cls, val):
        """validation name"""
        if re.match(r'^[A-Z][a-z]*$', val) is None:
            raise ValueError('Bad name')
        return val

    class Config:
        """configuration"""
        orm_mode = True


class UserList(BaseModel):
    """list schema"""
    __root__: List[UserBase]

    class Config:
        """configuration"""
        orm_mode = True


class UserCreate(UserBase):
    """create schema"""


class UserUpdate(UserBase):
    """update schema"""


class INdbUserBase(UserBase):
    """db schema"""
    user_id: int
    role_id: int
