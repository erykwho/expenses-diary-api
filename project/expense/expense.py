import flask_restful as restful

from database.connection import db_conn
from database.execute import execute_to_json, execute_to_scalar
from logger.logger import new

logger = new("Expense")


class Expense(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        logger.info("GET - Expense")

        try:
            conn = db_conn()

            query_count = '''
            SELECT
                COUNT(*)
            FROM
                "expense"
            WHERE
                is_active IS true;
            '''

            query_select = '''
            SELECT
                user_id,
                payment_origin_id,
                category_id,
                reference_date,
                description,
                amount,
                regreted,
                comments
            FROM
                "expense"
            WHERE is_active IS true;
            '''

            result = execute_to_json(conn, query_select)
            count = execute_to_scalar(conn, query_count)

            response = dict()
            response['content'] = result
            response['total'] = count

            conn.close()
            return response, 200
        except Exception as error:
            logger.info(error)
            return error, 500
