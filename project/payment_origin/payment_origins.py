import flask_restful as restful
from flask import request

from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar, execute
from logger.logger import new
from project.payment_origin.queries import SELECT_PAYMENT_ORIGINS, COUNT_PAYMENT_ORIGINS, INSERT_PAYMENT_ORIGIN
from project.returns import status_ok
from project.returns.bad_request import missing_fields
from project.returns.internal_server_error import unexpected_error
from project.returns.not_implemented import not_implemented
from utils.validate_body import validate_body

logger = new("PaymentOrigin")

COLUMNS = [
    "user_id",
    "name",
    "description",
    "abbreviation"
]

REQUIRED_COLUMNS = [
    "user_id",
    "name"
]


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
        try:
            content = validate_body(request.get_json(), REQUIRED_COLUMNS, COLUMNS)
            logger.info("Request Body: {content}".format(content=content))

            conn = db_conn()
            execute(conn, INSERT_PAYMENT_ORIGIN, content)
            conn.close()

            return status_ok.inserted()
        except KeyError as error:
            logger.info(error)
            return missing_fields(error.fields)
        except Exception as error:
            logger.info(error)
            return unexpected_error()


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
