import flask_restful as restful
from flask import Blueprint  # pragma: no cover

from project.user.users import Users

user = Blueprint(
    'user', __name__,
)

api = restful.Api()
api.init_app(user)

api.add_resource(Users, '/v1/users')
# api.add_resource(User, '/v1/users/<int:id>')
