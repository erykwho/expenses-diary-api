import psycopg2

DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: float(value) if value is not None else None)

DATE2STRING = psycopg2.extensions.new_type(
    psycopg2.extensions.DATE.values,
    'DATE',
    psycopg2.STRING)

DATETIME2STRING = psycopg2.extensions.new_type(
    psycopg2.extensions.PYDATETIME.values,
    'DATE',
    psycopg2.STRING)

psycopg2.extensions.register_type(DEC2FLOAT)
psycopg2.extensions.register_type(DATE2STRING)
psycopg2.extensions.register_type(DATETIME2STRING)
