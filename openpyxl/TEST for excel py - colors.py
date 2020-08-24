import openpyxl
from openpyxl.styles import *
from copy import copy
from random import randint
wb = openpyxl.load_workbook('HandW4.xlsx')
# Get workbook active sheet   
# from the active attribute. 
sheet = wb.active
  
#color='FF0000'
#MC = sheet['A1']

#fill = PatternFill(fill_type='solid',fgColor='101010') #fgColor=colors.YELLOW)
#sheet.cell(row = 31, column = 74).fill=fill
#MC.fill=fill
# R G B red green blue



for r in range(1,80):
	for c in range(1,250):
		COL = '{}{}{}'.format(randint(10,99),randint(10,99),randint(10,99))
		#print(COL)
		fill = PatternFill(fill_type='solid',fgColor=COL) # #'200000'
		sheet.cell(row = r, column = c).fill=fill


# save the file 
#wb.save('dimension.xlsx')
wb.save('HandW5.xlsx')
