""""""

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
# from flask_login import LoginManager

from app.models.db import db
from app.config import Config
from app.models.models import Users

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


migrate = Migrate()
migrate.init_app(app, db)

CORS(app)


# login_man = LoginManager()
# login_man.login_view = 'api.authentication_login'
# login_man.init_app(app)


# @login_man.user_loader
# def load_usr(user_id):
#     return Users.query.get(int(user_id))
