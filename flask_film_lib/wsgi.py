"""Main module"""

from app import app
from app import routes

routes.hippie()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
