import re
def tweet(txt):
	pattern = re.compile(r"[#@]\w+")
	x = re.findall(pattern,txt)
	return " ".join(x)
	
# Original challenge by @Ruud Peter Boelens

print(tweet('Visit us at @edabit'))# '@edabit')
print(tweet('This is #definitely, the @second test'))# '#definitely @second')
print(tweet('#Finally, a test!'))# '#Finally')
print(tweet('#Paris is the capital of #France.'))# '#Paris #France')
print(tweet('The @committee consists of #eminent #jurists.'))# '@committee #eminent #jurists')
print(tweet('#Honesty is the best @policy!!'))# '#Honesty @policy')
print(tweet('@RonaldRoss was awarded the Nobel Prize for his work on the transmission of #malaria.'))# '@RonaldRoss #malaria')
print(tweet('Follow @JavaScript'))# '@JavaScript')
