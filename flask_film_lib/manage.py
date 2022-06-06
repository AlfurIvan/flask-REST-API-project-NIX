"""Migrations"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import db


manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    pass


if __name__ == '__main__':
    manager.run()
