import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/76.0.3809.100 Safari/537.36'}


#
response = requests.get('https://demo.codemanas.com/code-manas-pro/', headers=headers)
                        # params = {'wd': '中国', 'ie': 'utf-8',
# 'f': 3,
# 'rsv_bp': 1,
# 'rsv_idx': 2,
# 'tn': 'baiduhome_pg',
# 'rsv_spt': 1,
# 'oq': 100,
# 'rsv_pq': 9282010e00005646,
# 'rsv_t': '65b6ZN8IJiXpluNcz/pIQxWDy8QWRjCXH7ym3yqE583HxR32Ytg75ZGh3MGjaslBNJxC',
# 'rqlang': 'cn',
# 'rsv_enter': 1,
# 'rsv_dl': 'ts_0',
# 'rsv_sug3': 9,
# 'rsv_sug1': 10,
# 'rsv_sug7': 101,
# 'rsv_sug2': 1,
# 'prefixsug': 'zhongu',
# 'rsp': 0,
# 'inputT': 4623}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/76.0.3809.100 Safari/537.36'}params=params, headers=headers)
# print(type(response.text))
# print(type(response.content))
# print(response.url)
with open('boke.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
print(response.content.decode('utf-8'))
# print(response.status_code)
