import re

# 1 * 可以匹配0或任意多个字符
text = 'aqw+q123ad1232'
# result = re.match('\s*', text)
# + 匹配1个或多个字符
# result = re.match('\w+', text)
# aqw
# ? 匹配一个或0个(要么没有,要么就只有一个)
# result = re.match('\w?', text)
# a
# {m} 匹配m个字符
# result = re.match('\w{2}', text)
# aq
# {m, n} 匹配m-n个字符
test = '\\n'
test1 = 'apple is $22, orange is $12'
test2 = 'Hello ni hao'
result = re.search('\\\\n', test)  # \\\\表示 \\ 表示一个\ \\后面一个表示一个\ 即 \\n 用python匹配 则是\n
# aqw
res = re.findall('\$\d+', test1)
# ['$22', '$12']

# sub函数
print(re.sub('\$\d+', '0', test1))
# apple is 0, orange is 0
print(res)
print(re.split(' ', test2))
# ['Hello', 'ni', 'hao']
