from urllib import parse

url='http://www.baidu.com/s?wd=hello&username=123#12'

print(parse.urlparse(url))
print(parse.urlparse(url).scheme)
print(parse.urlparse(url).netloc)
print(parse.urlsplit(url))