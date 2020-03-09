from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar=MozillaCookieJar('cookie.txt')

handler=request.HTTPCookieProcessor(cookiejar)
