"""CRUD for film table under film_abs"""

from json import loads
from typing import List, Dict, Any, Union, Optional

from app.models.models import Films, Genres, Directors
from app.models.db import db
from app.schemas.films import FilmBase, FilmList, FilmCreate, FilmUpdate
from .crud_base import BaseCRUD
from .crud_film_abs import FilmAbs
from config import DEFAULT_PAGINATION_VALUE as D
from sqlalchemy import extract


class FilmCRUD(BaseCRUD[Films, FilmCreate, FilmUpdate], FilmAbs):
    """Film CRUDs over BaseCRUD and FilmAbs for Film`s model"""

    def create(self, db_session: db.session,
               new_obj: Union[FilmCreate, Dict[str, Any]], **kwargs) -> FilmBase:
        """create method"""
        genres = kwargs['genres']
        obj = loads(new_obj)
        db_obj = self.model(**obj)
        for g in genres:
            db_obj.genres.append(g)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return self.schema.from_orm(db_obj)

    def mul_query(self, db_session: db.session):
        """method to creatind multiple queries"""
        return db_session.query(self.model)

    @staticmethod
    def query_paginator(query, page: int = 1, on_page: int = D):
        """method to paginate multiple queries"""
        return query.paginate(page=page, on_page=on_page).itens()

    def get_multi(self, db_session: db.session, *, page: int = 1, on_page: int = D) -> List[FilmBase]:
        """Read all records(first 10)"""
        return self.list_schema.from_orm(
            [self.schema.from_orm(item) for item in
             self.query_paginator(self.mul_query(db_session).order_by(self.model.film_id.asc()),
                                  page=page, on_page=on_page)])

    def get_by_part_name(self, db_session: db.session, name: str,
                         page: int = 1, on_page: int = D) -> Optional[List[FilmBase]]:
        """get by partial match"""
        name = f'%{name}%'
        return self.list_schema.from_orm([self.schema.from_orm(item) for item in
                                          self.query_paginator(self.mul_query(db_session).filter(
                                              self.model.name.ilike(name)).order_by(self.model.film_id.asc()),
                                                               page=page, on_page=on_page)])

    def date_filter(self, query, val):
        """release date filter"""
        start, end = val.split("-")
        return query.filter(extract('year', self.model.rel_date).between(start, end))

    def director_filter(self, query, val):
        """director filter"""
        return query.filter(self.model.director.any(Directors.director_name.in_(val)))

    def genres_filter(self, query, val):
        """genres filter"""
        genres_names = val.split("&")
        return query.filter(self.model.genre.any(Genres.genre.in_(genres_names)))

    def get_by_3_filters(self, db_session: db.session, vals: List[str],
                         page: int = 1, on_page: int = D) -> List[FilmBase]:
        """search with genres, directors, release date"""
        query = db_session.query(self.model).distinct()

        if vals[0] is not None:
            query = self.date_filter(query=query, val=vals[0])
        if vals[1] is not None:
            query = self.director_filter(query=query, val=vals[1])
        if vals[2] is not None:
            query = self.genres_filter(query=query, val=vals[2])

        return self.list_schema.from_orm(
            [self.list_schema.from_orm(item) for item in
             query.order_by(self.model.film_id.asc()).paginate(page=page, on_page=on_page).items()])

    def date_asc(self, query):
        """sort ascending by date"""
        return query.order_by(self.model.release_date.asc())

    def date_desc(self, query):
        """sort descending by date"""
        return query.order_by(self.model.release_date.desc())

    def rate_asc(self, query):
        """sort ascending by rate"""
        return query.order_by(self.model.rate.asc())

    def rate_desc(self, query):
        """sort ascending by rate"""
        return query.order_by(self.model.rate.desc())

    def get_by_rel_rate(self, db_session: db.session, order: List[str],
                        page: int = 1, on_page: int = D) -> Optional[List[FilmBase]]:
        """ search sorted by release_date and rating"""
        query = self.mul_query(db_session)

        if order[0] is not None:
            if order[0] == 'asc':
                query = self.date_asc(query)
            else:
                query = self.date_desc(query)

        if order[1] is not None:
            if order[0] == 'asc':
                query = self.rate_asc(query)
            else:
                query = self.rate_desc(query)

        return self.list_schema.from_orm([self.schema.from_orm(item)
                                          for item in self.query_paginator(query, page=page, on_page=on_page)])

film = FilmCRUD(Films, FilmBase, FilmList)
