from urllib.parse import urlparse

result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#here")
print(result)