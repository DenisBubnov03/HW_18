
from flask_restx import Namespace, Resource
from app.container import  genre_service
from app.dao.model.genre import GenreSchema




genre_ns = Namespace('genre')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        genre = genre_service.get_all()
        return genres_schema.dump(genre), 200



@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404
