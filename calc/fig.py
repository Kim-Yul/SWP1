from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    x = 'nonexistent'
    y = 'nonexistent'
    try:
        a, b = int(a), int(b)
	x = a + b
	y = a * b
    except Value Error:
	x = 'no value'
	y = 'no value'
    response_body = html+"Addition is {} and Multiplication is {}".format(x, y)
    start_response('200 OK', [
	('Content-Type', 'text/html'),
	('Content-Length', str(len(response_body)))
    ])
    return [response_body]
