#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from urllib.parse import urlparse, parse_qs

FIRST_LAW_COMMANDS = [
    '---...-..---.--.-.-|.--|---.--..-...-.---...-..'
]
SECOND_LAW_COMMANDS = [
    '-...-...-.-.|.....-...-.'
]


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        request_path = self.path
        
        print("\n----- Request Start ----->\n")
        print("Request path:", request_path)
        print("Request headers:", self.headers)
        print("<----- Request End -----\n")
        
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()
        
    def do_POST(self):
        
        request_path = self.path
        
        print("\n----- Request Start ----->\n")
        print("Request path:", request_path)
        
        request_headers = self.headers
        content_length = request_headers.get('Content-Length')
        length = int(content_length) if content_length else 0
        signal = self.rfile.read(length)
        fields = parse_qs(signal.decode("utf-8"))
        # print(fields)
        # print("Content Length:", length)
        # print("Request headers:", request_headers)
        # print("Request payload:", signal)
        # print("<----- Request End -----\n")
        # {'msg': ['.--.----....-..------.-..---..--...'], 'muz': ['True']}
        if not str2bool(fields['muz'][0]):
            self.send_response(406)
        if fields['msg'][0] in FIRST_LAW_COMMANDS:
            self.send_response(200)
        elif fields['msg'][0] in SECOND_LAW_COMMANDS:
            self.send_response(501)
        else:
            self.send_response(418)    
        self.end_headers()
    
    do_PUT = do_POST
    do_DELETE = do_GET

def str2bool(request):
    return request.lower() in ("True")

def main():
    port = 8080
    print('Listening on 0.0.0.0:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
    main()