import flask_restful as restful
from flask import Blueprint  # pragma: no cover

from resources.authentication.login import Login, Logout

authentication = Blueprint(
    'authentication', __name__,
)

api = restful.Api()
api.init_app(authentication)

api.add_resource(Login, '/v1/login')
api.add_resource(Logout, '/v1/logout')
