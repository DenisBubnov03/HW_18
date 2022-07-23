from flask import Flask
from flask_restx import Api
from config import Config
from app.setup_db import db
from app.views.director import director_ns
from app.views.movie import movie_ns
from app.views.genre import genre_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.debug = True
    app.run(host="localhost", port=10001, debug=True)
