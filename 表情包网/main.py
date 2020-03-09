import requests
import os
import re
from lxml import etree

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36 '
    }


def get_url():
    for i in range(1, 648):
        url = 'http://www.doutula.com/photo/list/?page=%d' % i
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        parse_page(html)
        break


def parse_page(html):
    images = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in images:
        file_url = img.get('data-original')
        alt = img.get('alt')
        suffix = os.path.splitext(file_url)
        alt = re.sub(r"[!\?,\.！？]", '', alt)
        filename = alt + suffix[1]
        download_img(file_url, filename)
        # 此处不能用urllib.request.urlretrieve() 会403


def download_img(url, filename):
    filename = 'D:\\images\\'+filename
    response = requests.get(url, headers=headers)
    with open(filename, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    get_url()
