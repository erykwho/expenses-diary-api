import flask_restful as restful
from flask import Blueprint  # pragma: no cover

from resources.category.categories import Categories, Category

category = Blueprint(
    'category', __name__,
)

api = restful.Api()
api.init_app(category)

api.add_resource(Categories, '/v1/categories',)
api.add_resource(Category, '/v1/categories/<int:id>')
