from typing import Dict

import requests
import json
import pandas as pd
from lxml import etree

url = 'https://data.wxb.com/rank/day/2020-02-22/%E7%A7%91%E6%8A%80?sort=&page=1&page_size=50&is_new=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36',
    'Cookie': 'PHPSESSID=beac3d26447612afc0000369ce0a6b37; Qs_lvt_288791=1582549381; Qs_pv_288791=4313460905624405000; '
              'aliyungf_tc=AQAAAKyqam5YtgQAWQMTOkuQHo7LO0N2; visit-wxb-id=847ecde119a5cefbe55b022b9af2debe ',
}

response=requests.get(url, headers=headers)
json_obj=json.loads(response.text,encoding='utf-8')
url_id=[]
articles = []
for i in json_obj['data']:
    url_id.append(i['wx_origin_id'])
for url in url_id:
    headers['Referer'] = 'https://data.wxb.com/details/postRead?id='+url
    for j in range(1, 11):
        resp = requests.get('https://data.wxb.com/account/statArticles/'+url+'?period=30&page='+str(j)+'&sort=', headers=headers)
        json_obj = json.loads(resp.text, encoding='utf-8')
        for i in json_obj['data']:
            article = {'title': i['title'], 'url': i['url']}
            articles.append(article)
            # for article in article_url:
            #     res=requests.get(article)
            #     print(res.url)
            #     print(res.text)
                # html=etree.HTML(res.text)
                # head=html.xpath("//head")
                # for i in head:
                #     print(etree.tostring(i, encoding='utf-8').decode('utf-8'))

pf = pd.DataFrame(list(articles))
columns = {
        'title': '名称',
        'url': '网址'
    }
pf.rename(columns=columns, inplace=True)
pf.to_excel('D:/公众号文章.xlsx', encoding='utf-8', index=False)
