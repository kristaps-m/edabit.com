import re
def validate_email(txt):
	# "john.smith@email.com"
	P= re.compile(r"[\w\.]+@\w+\.com")
	x=re.match(P,txt)
	# ~ if x:
		# ~ return True
	# ~ return False
	return bool(x)
	
print(validate_email('@edabit.com'), False)
print(validate_email('@edabit'), False)
print(validate_email('matt@edabit.com'), True)
print(validate_email(''), False, "Don't forget about empty strings!")
print(validate_email('hello.gmail@com'), False)
print(validate_email('bill.gates@microsoft.com'), True)
print(validate_email('hello@email'), False)
print(validate_email('%^%$#%^%'), False)
print(validate_email('www.email.com'), False)
print(validate_email('email'), False)
