"""module with abstract class for specific requests"""

from abc import ABC, abstractmethod
from typing import Optional, List
from app.models.db import db
from app.schemas.films import FilmBase
from app.config import DEFAULT_PAGINATION_VALUE as D


class FilmAbs(ABC):
    """abstract class for specific requests"""

    @abstractmethod
    def get_by_part_name(self, db_session: db.session, name: str,
                         page: int = 1, on_page: int = D) -> Optional[List[FilmBase]]:
        """search by partial match method"""

    @abstractmethod
    def get_by_3_filters(self, db_session: db.session, vals: List[str],
                         page: int = 1, on_page: int = D) -> Optional[List[FilmBase]]:
        """search with genres, directors, release date"""

    @abstractmethod
    def get_by_rel_rate(self, db_session: db.session, order: List[str],
                        page: int = 1, on_page: int = D) -> Optional[List[FilmBase]]:
        """ search sorted by release_date and rating"""
