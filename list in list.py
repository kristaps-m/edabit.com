def count_ones(matrix):
	#NL = [i for i in matrix for a in i]
	#NL = [i for i in for a in matrix]
	#NL = [number for group in matrix for number in group]
	#NL = [i for a in matrix for i in a]
	NL = [the_one_i_need for from_little_list_in_list in matrix for the_one_i_need in from_little_list_in_list]
	return NL.count(1)
	
	
print(count_ones([
	[1, 0, 1],
	[0, 0, 0],
	[0, 0, 1]
]))# 3)

print(count_ones([
	[1, 1, 1],
	[0, 0, 1],
	[1, 1, 1]
]))# 7)

print(count_ones([
	[1, 2, 3],
	[0, 2, 1],
	[5, 7, 33]
]))# 2)

print(count_ones([
	[5, 2, 3],
	[0, 2, 5],
	[5, 7, 33]
]))# 0)

print(count_ones([
	[5, 2], 
	[0, 2], 
	[5, 1]
]))# 1)

print(count_ones([
	[1, 1], 
	[0, 1]
]))# 3)

print(count_ones([
	[0, 1], 
	[0, 0]
]))# 1)
