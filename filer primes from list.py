def filter_primes(num):
	L = []
	for i in num:		
		CD = 0 #count divisors
		for u in range(1,i+1):			
			if i % u ==0:
				CD += 1
		if CD == 2:
			L.append(i)
	return L
	
	
print(filter_primes([7, 9, 3, 9, 10, 11, 27]))# [7, 3, 11])
print(filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))# [2, 3, 5, 7, 11, 13, 17, 19, 23])
print(filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]))# [1009, 3, 61, 1087, 1091, 1093, 1097])
print(filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]))# [10007, 1009])
