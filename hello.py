import re

def app(environ, start_response):
    qs = environ['QUERY_STRING']
    pattern = r"[0-9a-z]+=[0-9a-z]+"
    result = []
    if re.search(pattern, qs):
        result = re.findall(pattern, qs)
    result = "\r\n".join(result)
    start_response("200 OK", [
        ("Content-Type", "text/plain")])
    return [i.encode() for i in result]
   
    
