import pandas as pd
import requests
from lxml import etree
import xlwt
DOMAIN = 'https://www.dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36'}

movies = []


def get_details():
    for i in range(1, 8):
        url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_' + str(i) + '.html'
        response = requests.get(url, headers=HEADERS)
        text = response.text
        html = etree.HTML(text)
        detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
        for detail_url in detail_urls:
            movie = parse_detail(DOMAIN + detail_url)
            movies.append(movie)
            # pf = pd.DataFrame(list(movie))
            #             # print(pf)
            # columns_map = {
            #     'title': '名称',
            #     'cover': '封面',
            #     'year': '年份',
            #     'country': '国家',
            #     'category': '分类',
            #     'douban_rating': '豆瓣评分',
            #     'size': '分辨率',
            #     'actors': '演员',
            #     'director': '导演',
            #     'label': '标签',
            #     'download_url': '下载地址',
            #     'profile': '简介'}
            # pf.rename(columns=columns_map, inplace=True)
            # pf.fillna(' ', inplace=True)
            # pf.to_excel('d:/my.xlsx', encoding='utf-8', index=False)
            # data = movie
            # data_df = pd.DataFrame(data)
            # data_df.index = range(1, 100)
            # writer = pd.ExcelWriter('my.xlsx')
            # data_df.to_excel(writer, float_format='%.5f')
            # writer.save()


def parse_detail(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    movie['title'] = html.xpath("//div[@class='title_all']//font/text()")[0]
    if len(html.xpath("//div[@id='Zoom']//img/@src")):
        movie['cover'] = html.xpath("//div[@id='Zoom']//img/@src")[0]
    parse_movie_content(html, movie)  # 解析content
    movie_download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
    movie['download_url'] = movie_download_url
    return movie


def parse_movie_content(html, movie):
    movie_content = html.xpath("//div[@id='Zoom']//p/text()")
    for index, info in enumerate(movie_content):
        if info.startswith("◎年　　代"):
            info = info.replace("◎年　　代", "").strip()
            movie['year'] = info
        if info.startswith("◎产　　地"):
            info = info.replace("◎产　　地", "").strip()
            movie['country'] = info
        if info.startswith("◎类　　别"):
            info = info.replace("◎类　　别", "").strip()
            movie['category'] = info
        if info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分", "").strip()
            movie['douban_rating'] = info
        if info.startswith("◎视频尺寸"):
            info = info.replace("◎视频尺寸", "").strip()
            movie['size'] = info
        if info.startswith('◎导　　演'):
            info = info.replace("◎导　　演", "").strip()
            movie["director"] = info
        if info.startswith('◎主　　演'):
            info = info.replace("◎主　　演", "").strip()
            actors = [info]
            for actor in range(index + 1, len(movie_content)):
                if movie_content[actor].startswith("◎标　　签"):
                    break
                actors.append(movie_content[actor].strip())
            movie["actors"] = actors
        if info.startswith('◎标　　签'):
            info = info.replace("◎标　　签", "").strip()
            movie['label'] = info
        if info.startswith('◎简　　介'):
            info = movie_content[index + 1].strip()
            movie["profile"] = info


if __name__ == '__main__':
    get_details()
    pf = pd.DataFrame(list(movies))
    columns_map = {
        'title': '名称',
        'cover': '封面',
        'year': '年份',
        'country': '国家',
        'category': '分类',
        'douban_rating': '豆瓣评分',
        'size': '分辨率',
        'actors': '演员',
        'director': '导演',
        'label': '标签',
        'download_url': '下载地址',
        'profile': '简介'}
    pf.rename(columns=columns_map, inplace=True)
    pf.to_excel('D:/my.xlsx', encoding='utf-8', index=False)
