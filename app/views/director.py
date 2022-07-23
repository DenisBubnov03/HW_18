from flask_restx import Namespace, Resource

from app.container import director_service
from app.dao.model.directors import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


############## DIRECTOR ##############
@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        director = director_service.get_all()
        return directors_schema.dump(director), 200


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404
