import flask_restful as restful
from flask import request

from authentication.password import encrypt
from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar, execute
from logger.logger import new
from queries.user import SELECT_USERS, COUNT_USERS, INSERT_USER
from returns import status_ok
from returns.bad_request import missing_fields
from returns.internal_server_error import unexpected_error
from utils.validate_body import validate_body

logger = new("User")

PASSWORD = "password"

COLUMNS = [
    "firstName",
    "lastName",
    "email",
    PASSWORD
]

REQUIRED_COLUMNS = [
    "firstName",
    "lastName",
    "email",
    PASSWORD
]

UPDATEABLE_COLUMNS = [
    "firstName",
    "lastName",
    "email",
    PASSWORD
]


class Users(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        try:
            conn = db_conn()
            response = dict()

            response['content'] = execute_to_json(conn, SELECT_USERS)
            response['total'] = execute_to_scalar(conn, COUNT_USERS)

            conn.close()
            return response, 200
        except Exception as error:
            logger.error(error)
            return unexpected_error()

    @staticmethod
    def post():
        try:
            content = validate_body(request.get_json(), REQUIRED_COLUMNS, COLUMNS)
            content = encrypt(content)
            logger.info("Request Body: {content}".format(content=content))

            conn = db_conn()
            user_id = execute_to_scalar(conn, INSERT_USER, content)
            conn.commit()
            conn.close()

            if not user_id:
                raise Exception

            return status_ok.user_session(user_id, content['email'])
        except KeyError as error:
            logger.info(error)
            return missing_fields(error.fields)
        except Exception as error:
            logger.info(error)
            return unexpected_error()

#
# class User(restful.Resource):
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get(id=None):
#         try:
#             conn = db_conn()
#             response = dict()
#
#             response['content'] = execute_to_json(conn, SELECT_USER, (id,))
#
#             conn.close()
#             return response, 200
#         except Exception as error:
#             logger.error(error)
#             return unexpected_error()
#
#     @staticmethod
#     def patch(id=None):
#         try:
#             content = validate_update_columns(request.get_json(), UPDATEABLE_COLUMNS)
#             logger.info("Request Body: {content}".format(content=content))
#
#             conn = db_conn()
#
#             for key, value in content.items():
#                 arguments = (AsIs(key), value, id)
#                 execute(conn, UPDATE_USER, arguments)
#             conn.close()
#
#             return status_ok.modified()
#         except KeyError as error:
#             logger.info(error)
#             return invalid_fields(error.fields)
#         except Exception as error:
#             logger.info(error)
#             return unexpected_error()
#
#     @staticmethod
#     def delete(id=None):
#         try:
#
#             conn = db_conn()
#             execute(conn, DELETE_USER, (id,))
#             conn.close()
#
#             return status_ok.deactivated()
#         except Exception as error:
#             logger.info(error)
#             return unexpected_error()
