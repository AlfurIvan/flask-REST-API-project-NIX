from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from .db import db


films_genres = db.Table(
    # linked sub table WHY I CAN`T USE DOCSTRINGS HERE???
    "films_genres",
    db.metadata,
    db.Column("film_id", db.Integer, db.ForeignKey("films.film_id")),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.genre_id")),
)


class Films(db.Model):
    """Films ORM model"""
    __tablename__ = 'films'

    film_id = db.Column(
        db.INTEGER,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(length=40), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(length=1023))
    poster = db.Column(db.String(length=100), nullable=False)
    rate = db.Column(db.SmallInteger, nullable=False)
    director_id = db.Column("directors", db.ForeignKey("directors.director_id"))
    genre_id = db.relationship("genres", secondary=films_genres, backref="films", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))


class Genres(db.Model):
    """Genres ORM model"""
    __tablename__ = 'genres'

    genre_id = db.Column(
        db.Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    genre = db.Column(db.String(length=40), nullable=False)


class Directors(db.Model):
    """Directors ORM model"""
    __tablename__ = 'directors'

    director_id = db.Column(
        db.Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    director_name = db.Column(db.String(length=60), nullable=False, default="<unknown>")


class Users(db.Model):
    """User ORM model"""
    __tablename__ = 'users'

    user_id = db.Column(
        db.INTEGER,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    login = db.Column(db.String(length=20), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"))

    def __init__(self, login, password_hash, role_id):
        self.login = login
        self.password_hash = generate_password_hash(password_hash, method='sha256')
        self.role_id = role_id

    def get_id(self):
        """Ovr mixin method"""
        return self.user_id

    def __str__(self):
        return f'User {self.user_id}: {self.login}'


class Roles(db.Model):
    """Roles ORM model"""
    __tablename__ = 'roles'

    role_id = db.Column(
        db.Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    role = db.Column(db.String(length=20), nullable=False)
