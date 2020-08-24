import re
def trouble(num1, num2):
	pattern1 = re.compile(r"1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|8{3}|0{3}|9{3}|7{3}") # 1{3}|9{3}|7{3}
	pattern2 = re.compile(r"1{2}|2{2}|3{2}|4{2}|5{2}|6{2}|8{2}|0{2}|9{2}|7{2}")
	x = re.findall(pattern1, str(num1))
	y = re.findall(pattern2, str(num2))
	if len(x) <1:
		return False
	else:
		for i in y:
			if i in "".join(x):
				return True
		return False 

# ~ import re
# ~ def trouble(num1, num2):
    # ~ r = lambda i,n: r"" + str(i) + "{" + str(n) + "}"
    # ~ return any(re.findall(r(i,3),str(num1)) and re.findall(r(i,2),str(num2)) for i in "0123456789")
        
        
# ~ def trouble(num1, num2):
  # ~ for i in "0123456789":
    # ~ if i*3 in str(num1) and i*2 in str(num2):
      # ~ return True
  # ~ return False
	
	
print(trouble(451999277, 41177722899))# True)
print(trouble(444, 44))# True)
print(trouble(1222345, 12345))# False)
print(trouble(12345, 12345))# False)
print(trouble(888, 888))# True)
print(trouble(666789, 12345667))# True)
print(trouble(10560002, 100))# True)
print(trouble(1, 1))# False)
print(trouble(9111922229333339, 9559669779))# False)
