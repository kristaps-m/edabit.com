def get_indices(lst, el):
	X = enumerate(lst)
	new_lst = []
	for lists_item_index,THE_item_in_list in X:
		if THE_item_in_list == el:
			new_lst.append(lists_item_index)
		#print(lists_item_index,THE_item_in_list)	
	return new_lst
	
	'''	
	X = []
	C = 0
	for i in lst:
		if i == el:
			X.append(C)
			C += 1
		if i != el:
			C += 1
	return X
	
count = 0
	indices = []
	for item in lst:
		if item == el:
			indices.append(count)
		count += 1
	return indices
'''
	

print(get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'))# [0, 1, 3, 5])
print(get_indices([1, 5, 5, 2, 7], 7))# [4])
print(get_indices([1, 5, 5, 2, 7], 5))#[1, 2])
print(get_indices([1, 5, 5, 2, 7], 8))# [])
print(get_indices([8, 8, 8, 8, 8], 8))# [0, 1, 2, 3, 4])
print(get_indices([8, 8, 7, 8, 8], 8))# [0, 1, 3, 4])
print(get_indices([True, False, True, False], True))# [0, 2])
print(get_indices([True, False, True, False], False))# [1, 3])
print()
#print(get_indices([8, 8, 7, 8, 8,5,4,5,6,7,5,3,23,34,4,23,2,22,1,3,4,5,6,7,51,1,1,1,2,3,8,8,8,8,8,8], 8))
