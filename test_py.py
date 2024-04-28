import psycopg2

db = psycopg2.connect(
    dsn='postgresql://postgres:postgres@localhost:5438/postgres',
)
