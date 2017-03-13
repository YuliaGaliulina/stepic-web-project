import re

def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    qs = environ['QUERY_STRING']
    pattern = r"[0-9a-z]+=[0-9a-z]+"
    result = []
    if re.search(pattern, qs):
        result = re.findall(pattern, qs)
    start_response(status, headers)
    return "\r\n".join(result).encode()
