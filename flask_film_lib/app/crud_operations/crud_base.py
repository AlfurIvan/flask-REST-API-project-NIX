"""base crud operations under crud abs"""

from json import loads
from typing import List, Dict, Union, Optional, Any
from app.models.db import db
from .crud_abs import AbcCRUD, ModelType, CreateSchemaType, \
    UpdateSchemaType, BaseSchemaType
from app.config import DEFAULT_PAGINATION_VALUE


class BaseCRUD(AbcCRUD):
    """
    Class with default realization of CRUD
    :param .model: flask-sqlalchemy model class
    :param .schema: pydantic model class
    :param .list_schema: list of schemas
    """

    def get(self, db_session: db.session, lookup_id: Any) -> Optional[BaseSchemaType]:
        """
        Shows for 1 object by id
        :param db_session: database session
        :param lookup_id: what item we want to see
        :return: sought-for item
        """
        return self.schema.from_orm(db_session.query(self.model).get(lookup_id))

    def get_page(self, db_session: db.session, *, page: int = 1,
                 on_page: int = DEFAULT_PAGINATION_VALUE) -> List[BaseSchemaType]:
        """
        Shows list of objects
        :param db_session: database session
        :param page: what page number do we want to render
        :param on_page: how many items we're going to print on 1 page
        :return: returns list of items
        """
        return self.list_schema.from_orm(
            [self.schema.from_orm(item) for item in db_session.query(self.model)
                .padginate(page=page, on_page=on_page).items])

    def create(self, db_session: db.session,
               new_obj: Union[CreateSchemaType, Dict[str, Any]], **kwargs) -> BaseSchemaType:
        """
Create object
        :param db_session: database session
        :param new_obj: new element to add
        :param kwargs:
        :return: returns new object from database
        """
        js_obj = loads(new_obj)
        db_obj = self.model(**js_obj)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return self.schema.from_orm(db_obj)

    def update(self, db_session: db.session, *, db_obj: ModelType,
               new_obj: Union[UpdateSchemaType, Dict[str, Any]]) -> BaseSchemaType:
        """
        Update object
        :param db_session: database session
        :param new_obj: new element with which we will either update the existing one or add a new one
        :param db_obj: existing object in database(to update)
        :return: returns updated object
        """
        obj_data = loads(db_obj)
        if isinstance(new_obj, dict):
            upd_data = new_obj
        else:
            upd_data = new_obj.dict(exclude_unset=True)
        for attr in obj_data:
            if attr in upd_data:
                setattr(db_obj, attr, upd_data[attr])
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return self.schema.from_orm(db_obj)

    def delete(self, db_session: db.session, *, del_id: int) -> ModelType:
        """
        Delete object
        :param db_session: database session
        :param del_id: id of element to delete
        :return: returns deleted object
        """
        to_del = db_session.query(self.model).get(del_id)
        db_session.delete(to_del)
        db_session.commit()
        return self.schema.from_orm(to_del)
