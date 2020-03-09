import requests

resp = requests.get('http://www.baidu.com')
print(resp.cookies.get_dict())
