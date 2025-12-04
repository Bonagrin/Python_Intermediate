import http.server

class WebSzerver(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes('<html><body>Hello, <b>Python</b> világ!</body></html>', 'utf-8'))
        
http.server.HTTPServer(('localhost', 8080), WebSzerver).serve_forever()