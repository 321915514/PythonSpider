import requests
import os
import re
from lxml import etree
import threading
from queue import Queue

# 生产者消费者下载表情包
#  其中需要两个队列,一个是获取每一页的url 还有一个获取每个表情的url
# 生产者负责获取每个表情包的url,消费者负责将表情的url写进文件

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36 '
}


class Producer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):  # 构造函数
        super(Producer, self).__init__(*args, **kwargs)  # 继承父类的方法
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        images = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in images:
            file_url = img.get('data-original')
            alt = img.get('alt')
            suffix = os.path.splitext(file_url)
            alt = re.sub(r"[!\?,\.！？]", '', alt)
            filename = alt + suffix[1]
            self.img_queue.put((file_url, filename))
            # download_img(file_url, filename)
            # 此处不能用urllib.request.urlretrieve() 会403


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):  # 构造函数
        super(Consumer, self).__init__(*args, **kwargs)  # 继承父类的方法
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url, filename = self.img_queue.get()  # 解析元组
            self.download_img(img_url, filename)

    def download_img(self, url, filename):
        file_name = 'D:\\images\\' + filename
        response = requests.get(url, headers=headers)
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(filename + '下载完成')


def main():
    page_queue = Queue(100)
    img_queue = Queue(50000)
    for i in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % i
        page_queue.put(url)  # 将每一页的url加入队列中
    for i in range(5):
        Producer(page_queue, img_queue).start()
    for i in range(5):
        Consumer(page_queue, img_queue).start()


if __name__ == '__main__':
    main()
