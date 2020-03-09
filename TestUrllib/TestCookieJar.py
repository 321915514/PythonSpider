from urllib import request
from http.cookiejar import MozillaCookieJar

# 保存cookie信息
cookieJar = MozillaCookieJar('cookie.txt')
# 加载cookie
cookieJar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookieJar)
opener = request.build_opener(handler)
resp = opener.open("http://www.baidu.com")
cookieJar.save(ignore_discard=True)
# 打印cookie信息
for cookie in cookieJar:
    print(cookie)
