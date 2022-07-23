from app.dao.director import DirectorDao
from app.dao.genre import GenreDao
from app.dao.movie import MovieDao
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService
from app.setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)