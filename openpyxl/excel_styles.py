import openpyxl
from openpyxl.styles import *
from copy import copy
wb = openpyxl.load_workbook('store.xlsx')
sheet = wb.active

MC = sheet['B4']

#print(dir(openpyxl.styles))

#Font family Tahoma // size 16 // Color red// Bold yes // Italic yes
font = Font(name='Tahoma', size=16, color=colors.RED, bold=True, italic=True, strike=False)
#font = Font(name='Tahoma', size=16)
MC.font = font

fill = PatternFill(fill_type='solid', fgColor=colors.YELLOW)
MC.fill=fill

double_border_green = Side(border_style='double', color=colors.GREEN)
thin_border_red = Side(border_style='thin', color='FF0000')
MC.border = Border(left=double_border_green, top=double_border_green,\
right=thin_border_red, bottom = thin_border_red)

NC = sheet['b10'] #new cell 
new_font = copy(MC.font) #copies old font to new variable
new_font.color = colors.BLUE #changes color of new font
NC.font = new_font



wb.save('store.xlsx')
