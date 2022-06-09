"""abstract base CRUD repo"""

from abc import ABC, abstractmethod
from typing import Generic, List, Dict, Union, Type, TypeVar, Optional, Any
from pydantic import BaseModel
from app.models.db import db
from . import DEFAULT_PAGINATION_VALUE

ModelType = TypeVar("ModelType", bound=db.Model)
BaseSchemaType = TypeVar("BaseSchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ListSchemaType = TypeVar("ListSchemaType", bound=BaseModel)


class AbcCRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType], ABC):
    """Create Read Update Delete abstracts + read_multi"""

    def __init__(self, model: Type[ModelType], schema: Type[BaseSchemaType],list_schema:Type[ListSchemaType]):
        self.model = model
        self.schema = schema
        self.list_schema = list_schema

    @abstractmethod
    def create(self, db_session: db.session, new_obj: Union[CreateSchemaType,
                                                            Dict[str, Any]], **kwargs) -> BaseSchemaType:
        """Create object"""

    @abstractmethod
    def get(self, db_session: db.session, lookup_id: Any) -> Optional[BaseSchemaType]:
        """Shows for 1 object by id"""

    @abstractmethod
    def get_page(self, db_session: db.session, *, page: int = 1,
                 on_page: int = DEFAULT_PAGINATION_VALUE) -> List[BaseSchemaType]:
        """Shows list of objects. Pagination value = DEFAULT_PAGINATION_VALUE"""

    @abstractmethod
    def update(self, db_session: db.session, *,
               db_obj: ModelType, new_obj: Union[UpdateSchemaType, Dict[str, Any]]) -> BaseSchemaType:
        """Update object"""

    @abstractmethod
    def delete(self, db_session: db.session, *, del_id: int) -> ModelType:
        """Delete object"""
