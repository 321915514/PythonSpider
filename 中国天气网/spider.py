import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []


def main():
    page = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
    for url in page:
        url = 'http://www.weather.com.cn/textFC/' + url + '.shtml'
        parse_page(url)
    # 根据最低气温排序
    ALL_DATA.sort(key=lambda data: data['min_temp'])
    data = ALL_DATA[0:10]
    charts = Bar('中国最低气温排行榜')
    cities = list(map(lambda x: x['city'], data))
    temp = list(map(lambda x: x['min_temp'], data))
    charts.add('', cities, temp)
    charts.render('temperature.html')


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    div = soup.find_all('div', attrs={'class': 'conMidtab'})[0]
    tables = div.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for tr in trs:
            tds = tr.find_all('td')
            city_td = tds[-8]
            city = list(city_td.stripped_strings)[0]
            print(city)
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})


if __name__ == '__main__':
    main()
