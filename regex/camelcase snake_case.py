# ~ def to_snake_case(txt):
	# ~ S = ""
	# ~ for i in txt:
		# ~ if i.isupper():
			# ~ S += "_"+i.lower()
		# ~ else:
			# ~ S+=i
	# ~ return S

# ~ def to_camel_case(txt):
	# ~ T = txt.split("_")
	# ~ if len(T)>1:
		# ~ return T[0]+"".join(T[i].capitalize() for i in range(1,len(T)))
	# ~ return txt
	
	
import re
def to_snake_case(txt):
	pattern = re.compile(r"([a-z])([A-Z])")
	match = pattern.sub(r'\1_\2', txt).lower()
	return match
	

def to_camel_case(txt):
	pattern = re.compile(r"(_)([a-z])")
	match = pattern.sub(lambda x: x.group(2).upper(), txt)
	a = re.sub(r"_", "", match)
	return a
	
	
# camelCase to snake_case tests
print(to_snake_case("edabit"))# "edabit")
print(to_snake_case("helloEdabit"))# "hello_edabit")
print(to_snake_case("isModalOpen"))# "is_modal_open")
print(to_snake_case("getBackgroundColor"))# "get_background_color")
print(to_snake_case("isLoading"))# "is_loading")
print(to_snake_case("x"))# "x")

# snake_case to camelCase tests
print(to_camel_case("edabit"))# "edabit")
print(to_camel_case("hello_edabit"))# "helloEdabit")
print(to_camel_case("is_modal_open"))# "isModalOpen")
print(to_camel_case("get_background_color"))# "getBackgroundColor")
print(to_camel_case("is_loading"))# "isLoading")
print(to_camel_case("x"))# "x")
