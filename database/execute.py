from psycopg2.extras import RealDictCursor


def execute(conn, query, params=None):
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute(query, params)
                conn.commit()
            except Exception as error:
                conn.rollback()
                raise error
    except Exception as error:
        raise error


def execute_to_json(conn, query, params=None):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(query, params)

        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(row.keys(), row.values())))

        return results


def execute_to_scalar(conn, query, params=None):
    with conn.cursor() as cursor:
        cursor.execute(query, params)

        result = cursor.fetchone()

    return result[0]
