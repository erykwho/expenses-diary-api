import flask_restful as restful
from flask import request

from authentication.password import valid_password
from database.connection import db_conn
from database.execute import execute_to_scalar
from exceptions.invalid_password import InvalidPassword
from exceptions.user_not_found import UserNotFound
from logger.logger import new
from queries.authentication import SELECT_USER_ID, SELECT_USER_PASSWORD
from returns.bad_request import missing_fields
from returns.internal_server_error import unexpected_error
from utils.validate_body import validate_body

logger = new("Authentication")

PASSWORD = "password"

REQUIRED_COLUMNS = [
    "email",
    PASSWORD
]

COLUMNS = [
    "email",
    PASSWORD
]


class Login(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def post():
        try:

            conn = db_conn()
            content = validate_body(request.get_json(), REQUIRED_COLUMNS, COLUMNS)
            password_hash = execute_to_scalar(conn, SELECT_USER_PASSWORD, content)

            if not password_hash:
                raise UserNotFound

            if not valid_password(content[PASSWORD], password_hash):
                raise InvalidPassword

            user_id = execute_to_scalar(conn, SELECT_USER_ID, content)

            return {
                       'email': content['email'],
                       'user_id': user_id
                   }, 200

        except (UserNotFound, InvalidPassword) as err:
            logger.error(err)
            return err.http_response
        except KeyError as error:
            logger.info(error)
            return missing_fields(error.fields)
        except Exception as error:
            logger.error(error)
            return unexpected_error()
        finally:
            conn.close()
