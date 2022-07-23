from app.dao.genre import GenreDao


class GenreService:
    def __init__(self, dao : GenreDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()
