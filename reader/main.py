import datetime
from mysql.connector import connect, Error
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        with connect(
                host="172.17.0.1",
                user='root',
                password='goodpassword',
                database='web',
        ) as connection:
            select = "SELECT SUM(numbers) FROM queries WHERE date = '{0}'".format(datetime.datetime.now().date())
            with connection.cursor() as cursor:
                cursor.execute(select)
                result = cursor.fetchall()
                res = str(result[0][0])
                self.wfile.write(str.encode(res))

httpd = HTTPServer(('', 8081), SimpleHTTPRequestHandler)
httpd.serve_forever()
