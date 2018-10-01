# Python's bundled WSGI server
from wsgiref.simple_server import make_server
from wsgiref.util import guess_scheme
import json, crypto_spread

# set the encoding
encoding = 'utf-8'

# set port
port = 8000

#create object of MyApp
# my_obj = crypto_spread.MyApp()

def application_(environ, start_response):

    try:
        response_text = crypto_spread.dispatch(environ)
    except Exception as exc:
        print(exc)
        status = "500 Internal Server Error"
        response_text = ''
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain; charset=' + encoding)] # HTTP Headers
    start_response(status, headers)

    return [response_text.encode('utf-8')]


httpd = make_server('', port, application_)
print(f"Serving on port {port}...")

# Serve until process is killed
httpd.serve_forever()
