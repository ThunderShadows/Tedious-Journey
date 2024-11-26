# Python Automation project Using Excel and openpyxl library/package
import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['A1']
cell = sheet.cell(1,1)
print(cell.value)