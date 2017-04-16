import flask_restful as restful
from flask import Blueprint  # pragma: no cover

from project.category.categories import Category

category = Blueprint(
    'category', __name__,
)

api = restful.Api()
api.init_app(category)

api.add_resource(Category, '/v1/categories/', '/v1/categories/<category_id>')
