"""pydantic schema for roles"""

from typing import List
from pydantic import BaseModel, constr


class RoleBase(BaseModel):
    """base schema"""
    name: constr(max_lenght=10)

    class Config:
        """Configuration class"""
        orm_mode = True


class RoleList(BaseModel):
    """list schema"""
    __root__: List[RoleBase]

    class Config:
        """configuration"""
        orm_mode = True


class RoleCreate(RoleBase):
    """create schema"""


class RoleUpdate(RoleBase):
    """update schema"""


class INdbRoleBase(RoleBase):
    """db schema"""
    role_id: int

