#https://edabit.com/challenge/KPicBthv6WhHFGapg
'''
Count the Syllables
Create a function that returns the number of syllables in a simple string.
The string is made up of short repeated words like "Lalalalalalala" (which would have 7 syllables).
'''
import collections
#txt="Bobobobobobobobo"
txt="Bofbofbofbofbofbofbofbof"
#results = collections.Counter(the_string)
#print(results)

def count_syllables(txt):
	return sum(1 for i in txt.lower() if i in 'aeiou')

print(count_syllables(txt))
