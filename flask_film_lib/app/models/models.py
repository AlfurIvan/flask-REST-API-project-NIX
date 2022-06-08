from . import db


class Films(db.Model):
    """Class, stored films and their attrs"""
    __tablename__ = 'films'

    film_id = db.Column(
        db.INTEGER,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.VARCHAR(40), nullable=False)
    date = db.Column(db.INTEGER, nullable=False)
    description = db.Column(db.TEXT)
    poster = db.Column(db.VARCHAR(100), nullable=False)
    rate = db.Column(db.SMALLINT, nullable=False)
    director_id = db.Column(db.INTEGER, db.ForeignKey("directors.director_id"))
    user_id = db.Column(db.INTEGER, db.ForeignKey("users.user_id"))


films_genres = db.Table(
    "films_genres",
    db.Model.metadata,
    db.Column("film_id", db.ForeignKey("films.film_id"), primary_key=True),
    db.Column("genre_id", db.ForeignKey("genres.genre_id"), primary_key=True),
)


class Genres(db.Model):
    """"""
    __tablename__ = 'genres'

    genre_id = db.Column(
        db.INTEGER,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    genre = db.Column(db.VARCHAR(40), nullable=False)


class Directors(db.Model):
    """"""
    __tablename__ = 'directors'

    director_id = db.Column(
        db.INTEGER,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    director_name = db.Column(db.VARCHAR(60), nullable=False, default="<unknown>")


class Users(db.Model):
    """"""
    __tablename__ = 'users'

    user_id = db.Column(
        db.INTEGER,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    login = db.Column(db.VARCHAR(20), nullable=False)
    password = db.Column(db.VARCHAR(20), nullable=False)
    role_id = db.Column(db.INTEGER, db.ForeignKey("roles.role_id"))

    def __str__(self):
        return f'User {self.user_id}: {self.login}'


class Roles(db.Model):
    """"""
    __tablename__ = 'roles'

    role_id = db.Column(
        db.INTEGER,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    role = db.Column(db.VARCHAR(20), nullable=False)
