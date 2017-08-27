import flask_restful as restful
from flask import Blueprint  # pragma: no cover

from resources.authentication.login import Login

authentication = Blueprint(
    'authentication', __name__,
)

api = restful.Api()
api.init_app(authentication)

api.add_resource(Login, '/v1/login')
