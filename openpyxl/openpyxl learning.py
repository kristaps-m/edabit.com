import openpyxl

wb = openpyxl.load_workbook('store.xlsx', data_only=True) #open excel file

print(wb.sheetnames) #print all shet names
print()
for sheet in wb:
	print(sheet.title) #print sheet names verticaly using loop


sheet = wb['Products'] #set variable of sheet products
print(sheet)
sheet = wb.active #set variable of first sheet

b2_cell = sheet['B2'] #set variable of B2 cell
c2_cell = sheet['c2']

print(b2_cell.value, c2_cell.value) #print values of cells
#print value of cell USINING > row and column coridnates
print(sheet.cell(row=4, column=2).value)  #Smart Watch
#print c2_cells row and column
print(c2_cell.row, c2_cell.column) #2 3


print(sheet['A5'].data_type) #n for numeric
print(sheet['B5'].data_type) #s for string
print(sheet['A5'].encoding) #utf-8
#to find out where did u define sheet use .parent ?!
print(sheet['D4'].parent) #<worksheet "Products">


cell_range = sheet['B2:C11']
for product, price in cell_range:
	print(f'Product: {product.value} Price: {price.value}') #Product: Mobile Phone Price: 15

#find out the range where data is stored or dimensions
print(sheet.dimensions, 'dimensions {Kroplis}')

#find out the max row and max column with containing data
print(sheet.max_row, sheet.max_column) #11 5

#Some how print out whole contents of all first sheet!
for row in sheet.rows:
	for cell in row:
		print(f'{cell.value} ', end='')
	print('\n')

#Print out all contents like TUPLE()
for row in sheet.values:
	print(row)

