import openpyxl
from openpyxl.styles import *
from copy import copy
wb = openpyxl.load_workbook('HandW2.xlsx')
# Get workbook active sheet   
# from the active attribute. 
sheet = wb.active
  
''' writing to the specified cell '''
#sheet.cell(row = 1, column = 1).value = ' hello '  
#sheet.cell(row = 2, column = 2).value = ' everyone '
  
# set the height of the row 
for i in range(1,150):
	sheet.row_dimensions[i].height = 20
  
#first columns A-Z
for i in range(1,27):
# chr(65+26)
# set the width of the column 
	sheet.column_dimensions[chr(64+i)].width = 4 #65= A

#rest of colums AA- infinity	
for u in range(1,15):
	for i in range(1,27):
		sheet.column_dimensions[chr(64+u)+chr(64+i)].width = 4 #65= A
# save the file 
#wb.save('dimension.xlsx')
wb.save('HandW4.xlsx')
