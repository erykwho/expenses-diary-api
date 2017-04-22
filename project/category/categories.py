import flask_restful as restful
from flask import request
from psycopg2.extensions import AsIs

from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar
from logger.logger import new
from project.returns import status_ok, bad_request, internal_server_error

logger = new("Category")


class Categories(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        logger.info("GET - Category")
        try:
            conn = db_conn()

            query_count = '''
            SELECT
                COUNT(*)
            FROM
                "category"
            WHERE
                user_id = 1
                AND is_active IS true;
            '''

            query_select = '''
            SELECT
                id,
                name,
                description
            FROM
                "category"
            WHERE
                user_id = 1
                AND is_active IS true;
            '''  # TODO: Remover user_id marretado

            result = execute_to_json(conn, query_select)
            count = execute_to_scalar(conn, query_count)

            response = dict()
            response['content'] = result
            response['total'] = count

            conn.close()
            return response, 200
        except Exception as error:
            logger.error(error)
            return internal_server_error.unexpected_error()

    @staticmethod
    def post():

        try:
            query_update = '''
            INSERT INTO "category" (
                user_id,
                name,
                description
            ) VALUES
              (%(user_id)s, %(name)s, %(description)s);
            '''

            content = request.get_json()
            logger.info("Request Body: {content}".format(content=content))

            conn = db_conn()
            cursor = conn.cursor()
            print(content)
            cursor.execute(query_update, content)

            cursor.close()
            conn.commit()
            conn.close()

            return status_ok.inserted()
        except Exception as error:
            logger.error(error)
            return internal_server_error.unexpected_error()


class Category(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def patch(id=None):
        try:
            id = int(id)
        except ValueError as error:
            logger.error(error)
            return bad_request.must_be_integer()
        except Exception as error:
            logger.error(error)
            return internal_server_error.unexpected_error()

        try:
            query_update = '''
            UPDATE "category"
                SET (%s) = (%s)
            WHERE
                id = (%s);
            '''

            content = request.get_json()
            logger.info("Request Body: {content}".format(content=content))

            conn = db_conn()
            cursor = conn.cursor()
            for key, value in content.items():
                arguments = (AsIs(key), value, id)
                cursor.execute(query_update, arguments)

            cursor.close()
            conn.commit()
            conn.close()

            return status_ok.modified()
        except Exception as error:
            logger.error(error)
            return internal_server_error.unexpected_error()

    @staticmethod
    def delete(id=None):
        try:
            id = int(id)
        except ValueError as error:
            logger.error(error)
            return bad_request.must_be_integer()
        except Exception as error:
            logger.error(error)
            return internal_server_error.unexpected_error()

        try:
            query_update = '''
            UPDATE "category"
                SET is_active = false
            WHERE
                id = (%s);
            '''

            conn = db_conn()
            cursor = conn.cursor()
            cursor.execute(query_update, (id,))

            cursor.close()
            conn.commit()
            conn.close()

            return status_ok.deactivated()
        except Exception as error:
            logger.error(error)
            return internal_server_error.unexpected_error()
