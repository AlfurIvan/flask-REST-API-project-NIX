"""pydantic schema for Genre"""

import re
from typing import List
from pydantic import BaseModel, constr, validator


class GenreBase(BaseModel):
    """base schema"""
    genre: constr(max_length=30)

    @validator('genre')
    def val_genre(cls, val):
        if re.match('^[A-Z][-a-zA-Z]+$', val) is None:
            raise ValueError("Bad genre")
        return val

    class Config:
        """configuration"""
        orm_mode = True


class GenreList(BaseModel):
    """list schema"""
    __root__: List[GenreBase]

    class Config:
        """configuration"""
        orm_mode = True


class GenreCreate(BaseModel):
    """Create schema"""


class GenreUpdate(BaseModel):
    """Update schema"""


class INdbGenreBase(GenreBase):
    """db schema"""
    director_id: int
