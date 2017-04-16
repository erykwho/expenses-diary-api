import psycopg2 as psql

from config.config import Config

config = Config()
host = config.POSTGRESQL_HOST
user = config.POSTGRESQL_USER
__password = config.POSTGRESQL_PASS
port = config.POSTGRESQL_PORT
database = config.POSTGRESQL_DB


def db_conn():
    return psql.connect(database=database,
                        user=user,
                        password=__password,
                        host=host,
                        port=port)
