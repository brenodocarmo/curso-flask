def application(environ, start_response):
	body = b'Hello world!\n'
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)
	return [body]



if __name__ == "__main__":
	from wsgiref.simple_server import make_server

	make_server('0.0.0.0', 8000, application).serve_forever()
