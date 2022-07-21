from flask import request
from flask_restx import Namespace, Resource
from app.setup_db import db
from app.models import Movie, MovieSchema


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
        movies = Movie.query.all()
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201



@movie_ns.route('/<int:pk>/')
class MoviesView(Resource):
    def get(self, pk):
        try:
            note = Movie.query.get(pk)
            return movie_schema.dump(note), 200
        except Exception as e:
            return str(e), 404

    def put(self, pk):
        nots = Movie.query.get(pk)
        req_json = request.json
        nots.author = req_json.get("Movie")
        db.session.add(nots)
        db.session.commit()
        return "", 204

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201

    def delete(self, pk):
        movie = Movie.query.get(pk)
        db.session.delete(movie)
        db.session.commit()
        return "", 204