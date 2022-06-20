"""CRUD for director table"""

from .crud_base import BaseCRUD
from app.models.models import Films, Directors
from app.models.db import db
from app.schemas.directors import DirectorCreate, DirectorBase, DirectorUpdate, DirectorList


class DirectorCRUD(BaseCRUD[Directors, DirectorCreate, DirectorUpdate]):
    """Directors CRUDs over BaseCRUD for Director`s model"""

    def delete(self, db_session: db.session, *, del_id: int) -> DirectorBase:
        """delete method"""
        obj = db_session.query(self.model).get(del_id)
        for film in db_session.query(Films).all():
            if film.director is not None:
                film.director.remove(obj)
        db_session.delete(obj)
        db_session.commit()
        return self.schema.from_orm(obj)


director = DirectorCRUD(Directors, DirectorBase, DirectorList)
