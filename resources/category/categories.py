import flask_restful as restful
from flask import request
from psycopg2.extensions import AsIs

from authentication.authentication import login_required
from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar, execute
from logger.logger import new
from queries.category import SELECT_CATEGORIES, COUNT_CATEGORIES, INSERT_CATEGORY, SELECT_CATEGORY, \
    UPDATE_CATEGORY, DELETE_CATEGORY
from returns import internal_server_error
from returns import status_ok
from returns.bad_request import invalid_fields, missing_fields
from returns.internal_server_error import unexpected_error
from utils.validate_body import validate_body, validate_update_columns

logger = new("Category")

COLUMNS = [
    "user_id",
    "name",
    "description"
]

REQUIRED_COLUMNS = [
    "name"
]

UPDATEABLE_COLUMNS = [
    "name",
    "description"
]


class Categories(restful.Resource):
    def __init__(self):
        pass

    @login_required
    def get(self):
        logger.info("GET - Category")
        try:
            conn = db_conn()

            user_id = request.headers.get('User-Id')
            response = dict()
            response['content'] = execute_to_json(conn, SELECT_CATEGORIES, (user_id,))
            response['total'] = execute_to_scalar(conn, COUNT_CATEGORIES, (user_id,))

            conn.close()
            return response, 200
        except Exception as error:
            logger.error(error)
            return internal_server_error.unexpected_error()

    @login_required
    def post(self):

        try:

            content = validate_body(request.get_json(), REQUIRED_COLUMNS, COLUMNS)
            logger.info("Request Body: {content}".format(content=content))

            content['user_id'] = request.headers.get('User-Id')

            conn = db_conn()
            execute(conn, INSERT_CATEGORY, content)
            conn.close()

            return status_ok.inserted()
        except KeyError as error:
            logger.info(error)
            return missing_fields(error.fields)
        except Exception as error:
            logger.info(error)
            return unexpected_error()


class Category(restful.Resource):
    def __init__(self):
        pass

    @login_required
    def get(self, id=None):
        try:
            conn = db_conn()
            response = dict()

            response['content'] = execute_to_json(conn, SELECT_CATEGORY, (id,))

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
                execute(conn, UPDATE_CATEGORY, arguments)
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
            execute(conn, DELETE_CATEGORY, (id,))
            conn.close()

            return status_ok.deactivated()
        except Exception as error:
            logger.info(error)
            return unexpected_error()
