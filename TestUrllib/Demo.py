from urllib import request
from http.cookiejar import CookieJar
from urllib import parse

# 登录

# 创建cookiejar对象
cookiejar = CookieJar()
# 创建opener
handler = request.HTTPCookieProcessor(cookiejar)
# 使用opener发送请求()
opener = request.build_opener(handler)
login_url = 'http://47.103.204.177/BookStore/UserServlet'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36'}
data = {'username': 123, 'password': 123, 'vcode': 'xh2c'}
resp = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
opener.open(resp)
# 访问个人主页
url = 'http://47.103.204.177/BookStore/gouwuche.jsp'
# 应该使用以前的opener
res = request.Request(url, headers=headers)
result = opener.open(res)
print(result.read().decode('utf-8'))
