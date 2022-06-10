"""CRUD for genres table"""

from .crud_base import BaseCRUD
from app.models.models import Films, Genres
from app.models.db import db
from app.schemas.genres import GenreCreate, GenreBase, GenreUpdate, GenreList


class GenreCRUD(BaseCRUD[Genres, GenreCreate, GenreUpdate]):
    """Genres CRUDs over BaseCRUD for Genres`s model"""

    def delete(self, db_session: db.session, *, del_id: int) -> GenreBase:
        """delete method"""
        obj = db_session.query(self.model).get(del_id)
        for film in db_session.query(Films).all():
            if film.genres.count(obj)>0:
                film.genres.remove(obj)
        db_session.delete(obj)
        db_session.commit()
        return self.schema.from_orm(obj)


genre = GenreCRUD(Genres, GenreBase, GenreList)
