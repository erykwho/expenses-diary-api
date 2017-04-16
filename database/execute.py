from psycopg2.extras import RealDictCursor


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
