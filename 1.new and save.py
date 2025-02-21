from openpyxl import Workbook
wb = Workbook()

ws = wb.active

print(ws.title)

wb.save(r"./test.xlsx")

