import re
def no_yelling(phrase):
	# ~ #pattern = re.compile(r"[\w .'!]+ ?\w+[!\?\.]")
	# ~ pattern = re.compile(r"([!?])+$")
	# ~ x = re.findall(pattern, phrase)
	# ~ #y = re.sub(pattern,phrase,x[0])
	# ~ return x
	return re.sub("([!?])+$",r"\1",phrase)
	
	
print(no_yelling("What went wrong?????????"))# "What went wrong?")
print(no_yelling("Oh my goodness!!!"))# "Oh my goodness!")
print(no_yelling("WHAT!"))# "WHAT!")
print(no_yelling("WHAT?"))# "WHAT?")
print(no_yelling("Oh my goodness!"))# "Oh my goodness!")
print(no_yelling("I just cannot believe it."))# "I just cannot believe it.")
print(no_yelling("I just!!! can!!! not!!! believe!!! it!!!"))# "I just!!! can!!! not!!! believe!!! it!")
print(no_yelling("That's a ton!! of cheese!!!!"))# "That's a ton!! of cheese!")
