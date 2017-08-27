import flask_restful as restful
from flask import request
from psycopg2._psycopg import AsIs

from authentication.authentication import login_required
from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar, execute
from logger.logger import new
from queries.expense import SELECT_EXPENSES, COUNT_EXPENSES, INSERT_EXPENSE, SELECT_EXPENSE, UPDATE_EXPENSE, \
    DELETE_EXPENSE
from returns import status_ok
from returns.bad_request import missing_fields, invalid_fields
from returns.internal_server_error import unexpected_error
from utils.validate_body import validate_body, validate_update_columns

logger = new("Expense")

COLUMNS = [
    "user_id",
    "payment_origin_id",
    "category_id",
    "reference_date",
    "description",
    "amount",
    "regreted",
    "comments"
]

REQUIRED_COLUMNS = [
    "payment_origin_id",
    "category_id",
    "reference_date",
    "amount"
]

UPDATEABLE_COLUMNS = [
    "payment_origin_id",
    "category_id",
    "reference_date",
    "description",
    "amount",
    "regreted",
    "comments"
]


class Expenses(restful.Resource):
    def __init__(self):
        pass

    @login_required
    def get(self):
        try:
            conn = db_conn()
            user_id = request.headers.get('User-Id')
            response = dict()
            response['content'] = execute_to_json(conn, SELECT_EXPENSES, user_id)
            response['total'] = execute_to_scalar(conn, COUNT_EXPENSES, user_id)

            conn.close()
            return response, 200
        except AuthenticationFailed as err:
            return err.http_response
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
            execute(conn, INSERT_EXPENSE, content)
            conn.close()

            return status_ok.inserted()
        except KeyError as error:
            logger.info(error)
            return missing_fields(error.fields)
        except Exception as error:
            logger.info(error)
            return unexpected_error()


class Expense(restful.Resource):
    def __init__(self):
        pass

    @login_required
    def get(self, id=None):
        try:
            conn = db_conn()
            response = dict()

            response['content'] = execute_to_json(conn, SELECT_EXPENSE, (id, ))

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
                execute(conn, UPDATE_EXPENSE, arguments)
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
            execute(conn, DELETE_EXPENSE, (id, ))
            conn.close()

            return status_ok.deactivated()
        except Exception as error:
            logger.info(error)
            return unexpected_error()
