"""pydantic schema for Films"""

import re
from typing import Optional, List
from pydantic import BaseModel, HttpUrl, conint, confloat, constr, validator
from datetime import date

from .directors import DirectorBase
from .genres import GenreBase


class FilmBase(BaseModel):
    """base schema"""
    name: constr(max_length=40)
    rel_year: conint
    description: Optional[constr] = None
    poster = HttpUrl
    rate = confloat(ge=0, le=10)
    director: DirectorBase
    genres: List[GenreBase]

    @validator("rel_year")
    def val_release(cls, val):
        """validate release date"""
        if val > int(date.today().year) or val < 1895:
            raise ValueError("Wrong year")
        return val

    @validator("name")
    def val_name(cls, val):
        """validation name(title)"""
        if re.match(r'[A-Z][a-z]*(\s(([A-Z][a-z]*)|([a-z]+)))*(\s\d+)*$', val):
            raise ValueError("Wrong Year")
        return val

    @validator("rate")
    def val_rate(cls, val):
        """validation rating"""
        if val > 10 or val < 0:
            raise ValueError("Wrong rate")
        return val

    class Config:
        """configuration"""
        orm_mode = True


class FilmList(BaseModel):
    """list schema"""
    __root__: List[FilmBase]

    class Config:
        """Configuration class"""
        orm_mode = True


class FilmCreate(FilmBase):
    """Create schema"""
    user_id: int


class FilmUpdate(FilmBase):
    """Update schema"""


class INdbFilmBase(FilmBase):
    """db schema"""
    film_id: int
    user_id: int
