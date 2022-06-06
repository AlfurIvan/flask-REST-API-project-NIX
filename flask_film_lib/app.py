"""Main module"""

from flask import Flask
from flask_migrate import Migrate
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
migrate_ = Migrate(app, db)
db.init_app(app)


@app.route('/')
def root():
    """Main page"""
    return 'Welcome to my flask REST-API service'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)