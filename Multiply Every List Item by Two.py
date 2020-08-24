def get_multiplied_list(lst):
	X = []
	for i in lst:
		i *= 2
		X.append(i)
	return X	
	
print(get_multiplied_list([2, 5, 3,44]))

'''
def get_multiplied_list(lst):
	return [i*2 for i in lst]
'''
