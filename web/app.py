from wsgiref.simple_server import make_server

def web_app(environment, response):
    body = b'Generated Shortened Url!\n'
    status = "200 OK"
    headers = [('Content-type', 'text/plain')]
    response(status, headers)
    return [body]

with make_server('', 8000, web_app) as server:
    print('Serving on port 8000')
    server.serve_forever()