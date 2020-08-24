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

L = [str(i) for i in range(10,99)]

# end =    r=79 c=249

for r in range(1,32):
	for c in range(10,99):
		#while r < 30 and c < 73:
		#for u in L:
			#for i in range(1):
		#print(r,c,u,i)
		COL = '{}0000'.format(c)
		#print(COL)
		fill = PatternFill(fill_type='solid',fgColor=COL) # #'200000'
		sheet.cell(row = r, column = c).fill=fill

'''
for r in range(1,32):
	for c in range(10,99):
		#while r < 30 and c < 73:
		#for u in L:
			#for i in range(1):
		#print(r,c,u,i)
		COL = '00{}00'.format(c)
		#print(COL)
		fill = PatternFill(fill_type='solid',fgColor=COL) # #'200000'
		sheet.cell(row = r, column = c).fill=fill
		
for r in range(1,32):
	for c in range(10,99):
		#while r < 30 and c < 73:
		#for u in L:
			#for i in range(1):
		#print(r,c,u,i)
		COL = '0000{}'.format(c)
		#print(COL)
		fill = PatternFill(fill_type='solid',fgColor=COL) # #'200000'
		sheet.cell(row = r, column = c).fill=fill
'''
# save the file 
#wb.save('dimension.xlsx')
wb.save('HandW5.xlsx')
# 
