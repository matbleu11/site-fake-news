import http.server
import socketserver
import pyton serveur.py
PORT = 8000
DIRECTORY = "."

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
