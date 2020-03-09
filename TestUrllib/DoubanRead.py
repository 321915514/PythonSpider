from urllib import request
from urllib import parse
import xlwt
import json

workbook = xlwt.Workbook(encoding='ascil')
worksheet = workbook.add_sheet('2019豆瓣图书排行top10', cell_overwrite_ok=True)
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Time New Roman'
font.bold = True
style.font = font


def writeinExcel(data, i):
    if i == 0:
        for i in range(1, 11):
            for j in range(1, 7):
                worksheet.write(i, j, data)
                workbook.save('豆瓣.xls')

    if i == 1:
        for i in range(12, 21):
            for j in range(1, 7):
                worksheet.write(i, j, data)  # 不带样式的写入
                workbook.save('豆瓣.xls')

    if i == 2:
        for i in range(23, 32):
            for j in range(1, 7):
                worksheet.write(i, j, data)  # 不带样式的写入
                workbook.save('豆瓣.xls')

    if i == 3:
        for i in range(34, 43):
            for j in range(1, 7):
                worksheet.write(i, j, data)  # 不带样式的写入
                workbook.save('豆瓣.xls')
    if i == 4:
        for i in range(45, 54):
            for j in range(1, 7):
                worksheet.write(i, j, data)  # 不带样式的写入
                workbook.save('豆瓣.xls')

    if i == 5:
        for i in range(56, 65):
            for j in range(1, 7):
                worksheet.write(i, j, data)  # 不带样式的写入
                workbook.save('豆瓣.xls')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
urls = ['https://book.douban.com/ithil_j/activity/widget/955',
        'https://book.douban.com/ithil_j/activity/widget/1094',
        'https://book.douban.com/ithil_j/activity/widget/1095',
        'https://book.douban.com/ithil_j/activity/widget/1096',
        'https://book.douban.com/ithil_j/activity/widget/1097',
        'https://book.douban.com/ithil_j/activity/widget/1098',
		# 'https://book.douban.com/ithil_j/activity/widget/1099'
		# 'https://book.douban.com/ithil_j/activity/widget/1037',
		# 'https://book.douban.com/ithil_j/activity/widget/1111',
		# 'https://book.douban.com/ithil_j/activity/widget/1040',
		# 'https://book.douban.com/ithil_j/activity/widget/1048',
		# 'https://book.douban.com/ithil_j/activity/widget/1041',
		# 'https://book.douban.com/ithil_j/activity/widget/1042',
		]
for i in urls:
    for j in range(0, 55, 11):
        req = request.Request(i, headers=headers)
        result = request.urlopen(req)
        json_str = result.read().decode('utf-8')
        data = json.loads(json_str)
        worksheet.write(j, 0, data['res']['payload']['subtitle'] + data['res']['payload']['title'] + 'top10', style)
        for book in data['res']['subjects']:
            writeinExcel(book['title'], urls.index(i))
            writeinExcel(book['rating'], urls.index(i))
            writeinExcel(book['rating_count'], urls.index(i))
            writeinExcel(book['cover'], urls.index(i))
            writeinExcel(book['type'], urls.index(i))
            writeinExcel(book['url'], urls.index(i))
workbook.save('豆瓣.xls')
