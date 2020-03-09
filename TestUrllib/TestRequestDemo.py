from urllib import request
from urllib import parse

data = {
    'p': 1
}
url = 'http://47.103.204.177/crudtest/emps?' + parse.urlencode(data)
result = request.urlopen(url)
print(result.read().decode('utf-8'))
