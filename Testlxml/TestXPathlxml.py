from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html", parser=parser)
#获取所有tr标签
trs = html.xpath('//div')
for i in trs:
    print(etree.tostring(i,encoding='utf-8').decode('utf-8'))
