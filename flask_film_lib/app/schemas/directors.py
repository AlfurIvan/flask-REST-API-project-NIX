"""directors --> directorSchema
pydantic schema for Director"""

import re
from pydantic import BaseModel, validator, constr
from typing import List


class DirectorBase(BaseModel):
    """base schema"""
    director_name: constr(max_length=40)

    @validator("director_name")
    def val_name(cls, val):
        """validator for dir`s name"""
        if re.match('^[A-Z][-a-zA-Z]+$', val) is None:
            raise ValueError("Bad name")
        return val

    class Config:
        """configuration"""
        orm_mode = True


class DirectorList(BaseModel):
    """list schema"""
    __root__: List[DirectorBase]

    class Config:
        """configuration"""
        orm_mode = True


class DirectorCreate(DirectorBase):
    """create schema"""


class DirectorUpdate(DirectorBase):
    """update schema"""


class INdbDirectorBase(DirectorBase):
    """db schema"""
    director_id: int
