import flask_restful as restful

from logger.logger import new
from project.returns.not_implemented import not_implemented

logger = new("Category")


class PaymentOrigins(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        return not_implemented()

    @staticmethod
    def post():
        return not_implemented()


class PaymentOrigin(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get(id=None):
        return not_implemented()

    @staticmethod
    def patch(id=None):
        return not_implemented()

    @staticmethod
    def delete(id=None):
        return not_implemented()
