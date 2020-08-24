import re
def is_valid_phone_number(txt):
	# (123) 456-7890
	pattern = re.compile(r"^\(\d{3}\) \d{3}-\d{4}$")
	# ^=starts with
	# \( =escaping (
	# \d{3} = 3 only digits
	# - = dash betweem digits
	# \d{4}$ = ends with 4 digits
	x = re.search(pattern, txt)
	if x:
		return True
	return False
	
	
print(is_valid_phone_number("(123) 456-7890"))# True)
print(is_valid_phone_number("(1111)555 2345"))# False)
print(is_valid_phone_number("(098) 123 4567"))# False)
print(is_valid_phone_number("(123)456-7890"))# False)
print(is_valid_phone_number("abc(123)456-7890"))# False)
print(is_valid_phone_number("(123)456-7890abc"))# False)
print(is_valid_phone_number("abc(123)456-7890abc"))# False)
print(is_valid_phone_number("abc(123) 456-7890"))# False)
print(is_valid_phone_number("(123) 456-7890abc"))# False)
print(is_valid_phone_number("abc(123) 456-7890abc"))# False)
print(is_valid_phone_number("(123)-456-7890"))# False)
print(is_valid_phone_number("(123)_456-7890"))# False)
print(is_valid_phone_number("-123) 456-7890"))# False)
print(is_valid_phone_number("(519) 505-6498"))# True)
