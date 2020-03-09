from urllib import request
from urllib import parse
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
data={'first':'true','pn':1,'kd':'python'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
'Accept':'application/json',
'Host':'www.lagou.com'}
req=request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
result=request.urlopen(req)
print(result.read().decode('utf-8'))
