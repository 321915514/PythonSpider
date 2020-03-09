import re
import requests
import pandas as pd
poems = []


def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36'
    }
    for i in range(1, 10):
        # response = requests.get('https://www.gushiwen.org/default_' + str(i) + '.aspx', headers=headers)
        response = requests.get('https://so.gushiwen.org/shiwen/default_0AA'+str(i)+'.aspx', headers=headers)
        html = response.text
        titles = re.findall(r'<div\sclass="cont".*?<b>(.*?)</b>', html, re.DOTALL)
        dynasties = re.findall(r'<p\sclass="source".*?<a.*?>(.*?)</a>', html, re.DOTALL)
        authors = re.findall(r'<p\sclass="source">.*?<span.*?<a.*?>(.*?)</a>', html, re.DOTALL)
        content_tag = re.findall(r'<div\sclass="contson".*?>(.*?)</div>', html, re.DOTALL)
        contents = []
        for content in content_tag:
            content = re.sub(r'<.*?>', '', content)
            contents.append(content.strip())
        for value in zip(titles, dynasties, authors, contents):
            title, dynasty, author, content = value
            poem = {
                'title': title,
                'dynasty': dynasty,
                'author': author,
                'content': content
            }
            poems.append(poem)


if __name__ == '__main__':
    get_urls()
    pf = pd.DataFrame(list(poems))
    columns = {
        'title': '诗名',
        'dynasty': '朝代',
        'author': '作者',
        'content': '内容'
        }
    pf.rename(columns=columns, inplace=True)
    pf.to_excel('D:/古诗词.xlsx', encoding='utf-8', index=False)
    print(len(poems))
