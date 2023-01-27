import psycopg2

# don't forget to edit connect to match your database
# synstax db://user:password@localhost:port/dbname
CONNECTION = "postgres://postgres:admin1234@localhost:5432/SWU"


def setup_timescale():
    conn = psycopg2.connect(CONNECTION)
    cursor = conn.cursor()
    simulate_query = """CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"""
    cursor.execute(simulate_query)
    conn.commit()
    cursor.close()

setup_timescale()
