import datetime
from mysql.connector import connect, Error
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        try:
            with connect(
                    host="172.17.0.1",
                    user='root',
                    password='goodpassword',
                    database='web',
            ) as connection:
                insert = "INSERT INTO queries VALUES (%s, %s)"
                records = [
                    (1, datetime.datetime.now().date()),
                ]
                with connection.cursor() as cursor:
                    cursor.executemany(insert, records)
                    connection.commit()
        except Error as e:
            print(e)

if __name__ == "__main__":
    with connect(
        host="172.17.0.1",
        user='root',
        password='goodpassword',
    ) as connection:
        create_db_query = "CREATE DATABASE IF NOT EXISTS web;"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            connection.commit()

    with connect(
        host="172.17.0.1",
        user='root',
        password='goodpassword',
        database='web',
    ) as connection:
        create_table_query = "CREATE TABLE IF NOT EXISTS queries (numbers int default 1, date date);"
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()

    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()

