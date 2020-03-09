import requests

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Host': 'www.lagou.com'
}
# 使用代理
# proxy={
#     'http':'27.43.190.11:9999'
# }
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false', data=data, headers=headers) #proxies=proxy)
print(response.text)
