# import json
# from functools import cached_property
# from http.cookies import SimpleCookie
# from http.server import BaseHTTPRequestHandler
# import socketserver
# import http.server

# from urllib.parse import parse_qsl,urlparse

# PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

# class WebRequestHandler(BaseHTTPRequestHandler):
#     @cached_property
#     def url(self):
#         return urlparse(self.path)
#     @cached_property
#     def query_data(self):
#         return dict(parse_qsl(self.url.query))
#     @cached_property
#     def post_data(self):
#         content_length = int(self.handlers.get("Contents-length",0))
#         return self.rfile.read(content_length)
#     @cached_property
#     def form_data(self):
#         return dict(parse_qsl(self.post_data.decode("utf-8")))

#     def get_response(self):
#         return json.dumps({
#                               "path":self.url.path,
#                               "query_data":self.query_data,
#                               "post_data":self.post_data.decode("utf-8"),
#                               "form_data" : self.form_data,
#                               "cookies" :{
#                                   name: cookie.value
#                                   for name,cookie in self.cookies.items()
#                               },
#                           })

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-Type","application/json")
#         self.end_headers()
#         self.wfile.write(self.get_response().encode("utf-8"))

#     def do_POST(self):
#         self.do_GET()



import http.server
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse 
import socketserver

PORT = 8100

Handler  = http.server.SimpleHTTPRequestHandler

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        if "gamer" in urlparse(self.path).path: 
            print("f")
        self.wfile.write("Helloworld".encode("utf-8"))




with socketserver.TCPServer(("",PORT),WebRequestHandler) as httpd:
    print("Seriving at the port ",PORT)
    httpd.serve_forever()
