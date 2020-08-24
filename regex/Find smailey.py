import re
def count_smileys(lst):
	"""A smiley has eyes. Eyes can be : or ;.
A smiley has a nose but it doesn't have to. A nose can be - or ~.
A smiley has a mouth which can be ) or D."""
	pattern = re.compile(r"[:|;][-|~]?[)|D]")
	C = 0
	for i in lst:
		x = re.findall(pattern,i)
		if x:
			C += 1		
	return C
	
	
print(count_smileys([":)", ";(", ";}", ":-D"]))# 2)
print(count_smileys([";D", ":-(", ":-)", ";~)"]))# 3)
print(count_smileys([";]", ":[", ";*", ":$", ";-D"]))# 1)
print(count_smileys([";(", ":>", ":}", ":]"]))# 0)
print(count_smileys([":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)", ":)",]))# 13)
print(count_smileys([':)',':(',':D',':O',':;']))# 2)
print(count_smileys([':-)',';~D',':-D',':_D']))# 3)
print(count_smileys([':---)','))',';~~D',';D']))# 1)
print(count_smileys([';~)',':)',':-)',':--)']))# 3)
print(count_smileys([':o)',':--D',';-~)']))# 0)
print(count_smileys([]))# 0, "An empty list should return 0")
