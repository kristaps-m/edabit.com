def prime_numbers(num):
	PL = [] #prime list
	#from 2 to num
	for u in range(2,num+1):
		C = 0
		# check if 'u' is prime
		for i in range(1,u+1):
			if u % i == 0:
				C += 1
	# if it have 2 divisors it appends
		if C==2:
			PL.append(u)
	return len(PL)
	
	
print(prime_numbers(20))# 8)
print(prime_numbers(30))# 10)
print(prime_numbers(100))# 25)
print(prime_numbers(200))# 46)
print(prime_numbers(1000))# 168)
print(prime_numbers(-5))# 0)
print(prime_numbers(66))# 18)
print(prime_numbers(133))# 32)
print(prime_numbers(99))# 25)
