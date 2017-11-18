import flask_restful as restful
from flask import request
from psycopg2._psycopg import AsIs

from authentication.authentication import login_required
from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar, execute
from logger.logger import new
from queries.payment_origin import SELECT_PAYMENT_ORIGINS, COUNT_PAYMENT_ORIGINS, INSERT_PAYMENT_ORIGIN, \
    SELECT_PAYMENT_ORIGIN, UPDATE_PAYMENT_ORIGIN, DELETE_PAYMENT_ORIGIN
from returns import status_ok
from returns.bad_request import missing_fields, invalid_fields
from returns.internal_server_error import unexpected_error
from utils.validate_body import validate_body, validate_update_columns

logger = new("PaymentOrigin")

COLUMNS = [
    "user_id",
    "name",
    "description",
    "abbreviation"
]

REQUIRED_COLUMNS = [
    "name"
]

UPDATEABLE_COLUMNS = [
    "name",
    "description",
    "abbreviation"
]


class PaymentOrigins(restful.Resource):
    def __init__(self):
        pass

    @login_required
    def get(self):
        try:
            conn = db_conn()
            response = dict()

            user_id = request.headers.get('User-Id')

            response['content'] = execute_to_json(conn, SELECT_PAYMENT_ORIGINS, user_id)
            response['total'] = execute_to_scalar(conn, COUNT_PAYMENT_ORIGINS, user_id)

            conn.close()
            return response, 200
        except Exception as error:
            logger.error(error)
            return unexpected_error()

    @login_required
    def post(self):
        try:
            content = validate_body(request.get_json(), REQUIRED_COLUMNS, COLUMNS)
            logger.info("Request Body: {content}".format(content=content))

            content['user_id'] = request.headers.get('User-Id')

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

    @login_required
    def get(self, id=None):
        try:
            conn = db_conn()
            response = dict()

            response['content'] = execute_to_json(conn, SELECT_PAYMENT_ORIGIN, (id, ))

            conn.close()
            return response, 200
        except Exception as error:
            logger.error(error)
            return unexpected_error()

    @login_required
    def patch(self, id=None):
        try:
            content = validate_update_columns(request.get_json(), UPDATEABLE_COLUMNS)
            logger.info("Request Body: {content}".format(content=content))

            conn = db_conn()

            for key, value in content.items():
                arguments = (AsIs(key), value, id)
                execute(conn, UPDATE_PAYMENT_ORIGIN, arguments)
            conn.close()

            return status_ok.modified()
        except KeyError as error:
            logger.info(error)
            return invalid_fields(error.fields)
        except Exception as error:
            logger.info(error)
            return unexpected_error()

    @login_required
    def delete(self, id=None):
        try:

            conn = db_conn()
            execute(conn, DELETE_PAYMENT_ORIGIN, (id, ))
            conn.close()

            return status_ok.deactivated()
        except Exception as error:
            logger.info(error)
            return unexpected_error()
