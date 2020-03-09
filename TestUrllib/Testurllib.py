from urllib import request#导入库
from urllib import parse#用于编码
data={'wd':'刘德华'}
data=parse.urlencode(data)
data=parse.parse_qs(data)
#url='http://www.baidu.com/s?'+data
print(data)
#response=request.urlopen(url)#请求baidu.com
#print(response.read())

#request.urlretrieve('http://www.baidu.com','baidu.html')
#将百度的网页下载到本地baidu.html

#urlencode用法
#https://www.baidu.com/s?wd=hello&rsv_spt=1&rsv_iqid=0xc249d2880001381f&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=5&rsv_sug7=101&rsv_sug2=0&inputT=1310&rsv_sug4=2416
#将参数为中文的字符转换为浏览器能够识别的字符
#data={'wd':'你好','age':12,'gender':'男'}
#data=parse.urlencode(data)
#print(data)
