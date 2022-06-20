"""module for user pydentic schema"""

import re
from typing import List
from pydantic import BaseModel, constr, validator


class UserBase(BaseModel):
    """User pydantic schema"""
    login: constr(max_length=40)

    @validator("login")
    def validate_name(cls, val):
        """validation login"""
        if re.match(r'^[A-Z][a-z]*$', val) is None:
            raise ValueError('Bad login')
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
    role_id: int
    password: constr(max_length=255)


class UserUpdate(UserBase):
    """update schema"""
    role_id: int
    password: constr(max_length=255)


class INdbUserBase(UserBase):
    """db schema"""
    user_id: int
    role_id: int
