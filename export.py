import xlwt

a = 55
wb = xlwt.Workbook()
ws = wb.add_sheet('File#1')
ws.write(6,6,a)
font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 3

wb.save('File#1.xls')


