import xlwt

workbook=xlwt.Workbook(encoding='ascil')
worksheet=workbook.add_sheet('My Worksheet')
style=xlwt.XFStyle()
font=xlwt.Font()
font.name='Time New Roman'
font.bold=True
style.font = font
worksheet.write(1,0,'Formatted value',style)
worksheet.write(0, 0, 'Unformatted value') # 不带样式的写入
workbook.save('formatting.xls')
