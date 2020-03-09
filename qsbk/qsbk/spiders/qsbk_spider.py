# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy_demo.qsbk.qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['xiaohuabang.cn']
    start_urls = []
    for i in range(1, 190):
        start_urls.append('http://www.xiaohuabang.cn/duanzi/hunduanzi/p%d/' % i)
    def parse(self, response):
        hrefs = response.xpath("//a[@class='link_more']/@href").getall()
        for href in hrefs:
            url = 'http://www.xiaohuabang.cn'+href
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        title = response.xpath("//em[contains(@style,'font')]/text()").get()
        content = "".join(response.xpath("//div[@class='block untagged noline']//div[@class='content']//text()").getall()).strip()
        content = re.sub(r"[\s\n\s?]", '', content)
        item = QsbkItem(title=title, content=content)

        yield item
