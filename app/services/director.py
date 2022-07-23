from app.dao.director import DirectorDao


class DirectorService:
    def __init__(self, dao : DirectorDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()
