from urllib import request

url='https://httpbin.org/ip'

# print(request.urlopen(url).read())
#没有使用代理

#使用代理

handler=request.ProxyHandler({'http':'112.84.55.122:9999'})

openner=request.build_opener(handler)

res=openner.open(url)

print(res.read())

