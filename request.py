from urllib.parse import urlencode
from urllib.request import urlopen, Request
# GET
http_response = urlopen('http://www.example.com?email=whddjr2225@naver.com')
body = http_response.read()
print(body)


# POST
http_response = urlopen('http://www.example.com')
print(type(http_response))

data = {
    'email': 'whddjr2225@naver.com',
    'password': '1234',
    'name': '박종억'
}

data = urlencode(data).encode('utf-8')

# Request 객체는 post 방식으로 보낼 때 꼭 필요한 놈
request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')

http_response = urlopen(request)
print(http_response.read())
