from app.dao.movie import MovieDao


class MovieService:
    def __init__(self, dao : MovieDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)
        movie.description = data.get("description")

    def create(self, data):
        return self.dao.create(data)

    def delete(self, mid):
        self.dao.delete(mid)