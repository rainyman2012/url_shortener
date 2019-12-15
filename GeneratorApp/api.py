from wsgiref.simple_server import make_server

def application (environ, start_response):

    # Sorting and stringifying the environment key, value pairs
    body = b'Hello world!\n'    

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [body]

with make_server('', 8000, application) as server:
    print('Serving on port 8000')
    server.serve_forever()