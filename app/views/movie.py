from flask import request
from flask_restx import Namespace, Resource

from app.container import movie_service
from app.dao.model.movie import MovieSchema, Movie

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

############## MOVIE ##############
@movie_ns.route('/')
class MovieView(Resource):

    @movie_ns.doc(params={'director_id': "director_id", "genre_id": "genre_id", "year": "year"})
    def get(self):
        genre_id = request.args.get("genre_id", type=int)
        director_id = request.args.get("director_id", type=int)
        year = request.args.get("year", type=int)
        if director_id and genre_id:
            movies = Movie.query.filter(Movie.director_id == director_id, Movie.genre_id == genre_id).all()
            return movies_schema.dump(movies), 200
        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id).all()
            return movies_schema.dump(movies)
        if genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id).all()
            return movies_schema.dump(movies)
        if year:
            movies = Movie.query.filter(Movie.year == year).all()
            return movies
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201



@movie_ns.route('/<int:mid>/')
class MoviesView(Resource):
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204