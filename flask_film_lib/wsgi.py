"""Main module"""

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from app.models.db import db

app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)
CORS(app)
db.init_app(app)


@app.route('/')
def root():
    """Main page"""
    return 'Welcome to my flask REST-API service'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
