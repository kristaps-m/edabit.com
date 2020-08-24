import openpyxl

wb = openpyxl.load_workbook('store.xlsx')#, data_only=True) #open excel file

sheet = wb.active #sets var to first sheet

#----changes value of the D2 cell
#sheet['d2'] = 400 

#----add new row?
#new_product = (11, 'Tablet', 12, 600, 12*600)
#sheet.append(new_product)

for c,d,e in sheet['c2:e12']:
	e.value = c.value*d.value






#change file only works if you save it!
wb.save('store.xlsx')

