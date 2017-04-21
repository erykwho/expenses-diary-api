import flask_restful as restful

from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar
from logger.logger import new
from project.payment_origin.queries import SELECT_PAYMENT_ORIGINS, COUNT_PAYMENT_ORIGINS
from project.returns.not_implemented import not_implemented

logger = new("Category")


class PaymentOrigins(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        conn = db_conn()
        response = dict()

        # TODO: get user_id to send to query
        response['content'] = execute_to_json(conn, SELECT_PAYMENT_ORIGINS)
        response['total'] = execute_to_scalar(conn, COUNT_PAYMENT_ORIGINS)

        conn.close()
        return response, 200

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
