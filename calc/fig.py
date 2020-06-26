from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    x = 'nonexistent'
    y = 'nonexistent'
    try:
	if a.isdigit() and b.isdigit():
            a, b = int(a), int(b)
	    x = a + b
	    y = a * b
	elif '' not in [a, b]:
	    a, b = float(a), float(b)
	    x = a + b
	    y = a * b
	elif '' in [a, b]:
	    x = 'no value'
	    y = 'no value'
    except Value Error:
	x = 'not running'
	y = 'not running'
    response_body = html+"Addition is {} and Multiplication is {}".format(x, y)
    start_response('200 OK', [
	('Content-Type', 'text/html'),
	('Content-Length', str(len(response_body)))
    ])
    return [response_body]
