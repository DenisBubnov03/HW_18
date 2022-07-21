# # основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# # этот файл часто является точкой входа в приложение
#
# # Пример
#
from flask import Flask
from flask_restx import Api

from app.models import Movie
from config import Config
# from models import Review, Book
from app.setup_db import db
from app.views.director import director_ns
from app.views.movie import movie_ns
from app.views.genre import genre_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


# функция
def create_data(app, db):
    with app.app_context():
        db.create_all()
        m1 = Movie(id=32, title="Название", description="Описание", trailer="ссылка", year=2020)
        m2 = Movie(id=33, title="Название2", description="Описание2", trailer="ссылка2", year=2022)
        with db.session.begin():
            db.session.add_all([m1, m2])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)




