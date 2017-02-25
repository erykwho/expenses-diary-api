import flask_restful as restful
from psycopg2.extras import RealDictCursor

from database.connection import db_conn
from logger.logger import new

logger = new("Expense")


def execute_to_json(conn, query):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(query)

        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(row.keys(), row.values())))

    return results


def execute_to_scalar(conn, query):
    with conn.cursor() as cursor:
        cursor.execute(query)

        result = cursor.fetchone()

    return result[0]


class Expense(restful.Resource):
    def __init__(self):
        pass

    @staticmethod
    def get():
        logger.info("GET - Expense")

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
