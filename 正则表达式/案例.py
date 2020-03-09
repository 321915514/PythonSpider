import re
# 验证手机号
text = '13991471643'
result = re.match('1[34578]\d{9}', text)
# print(result.group())
# 验证邮箱
email = '321915@163.com'
ret = re.match('\w+@[a-z0-9]+\.[a-z]+', email)

# 验证url

url = 'http://www.baidu.com/s?re=233'
resultUrl = re.match('(http|https|ftp)://[^\s]+', url)#

# 验证身份证

id = '61252619971008357x'
res = re.match('\d{17}[\dXx]', id)
print(res.group())
