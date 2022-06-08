"""Migrations"""

from flask_script import Manager
from flask_migrate import MigrateCommand
from wsgi import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    pass


if __name__ == '__main__':
    manager.run()
