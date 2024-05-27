import psycopg2
from time import sleep

dbname = "mydatabase"
dbuser = "postgres"
dbpassword = "postgres"
dbhost = "localhost"

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mytable (
            id INT,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()


def insert_data(conn, num_rows):
    cursor = conn.cursor()
    insert_query = """INSERT INTO mytable (id, name) VALUES (%s, %s)"""
    rows = [(i, ("Row %d" % i)) for i in range(num_rows)]
    cursor.executemany(insert_query, rows)
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    try:
        conn = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost)
        create_table(conn)

        while True:
            insert_data(conn, 100000)
            print("Inserted %d rows" % 10000)
            sleep(1)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
