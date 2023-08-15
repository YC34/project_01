from http.server import HTTPServer,BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response_only(200,'OK')
		self.send_header('Content-type', 'text/plain')
		self.end_headers()
		self.wfile.write(b"Hello World")

if __name__ == '__main__':
	server = HTTPServer(('',8888),MyHandler)
	print("Start my port 8888")
	print("Press control+C to quit WebServer")
	server.serve_forever()
