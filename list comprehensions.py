def find_even_nums(num):
	even = [var for var in range(1,num+1) if var % 2 == 0]
	return even
print(find_even_nums(1))
