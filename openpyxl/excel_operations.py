import openpyxl
wb = openpyxl.load_workbook('store.xlsx')

#create new sheet
#wb.create_sheet('Turnover')
wb.create_sheet('Turnover_ONE', 0)

#remove worksheet!!
sheet1 = wb['Turnover_ONE']
wb.remove(sheet1)

#copy worksheet mother efer!!!
source = wb['Turnover']
destination = wb.copy_worksheet(source)
print(destination.title)


wb.save('store.xlsx')
