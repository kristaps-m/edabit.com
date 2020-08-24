def next_prime(num):
	while True:
		L = []
		for i in range(2,num):
			if num % i == 0:
				L.append(i)
				num +=1
			return L
			else:
				return num
	
	
'''
while [i for i in range(2, num) if num%i==0]:
	num+=1
else:
	return num
'''
'''
DC = 0 #divisors counter
for i in range(1,num+1):
	if num % i == 0:
		DC += 1
if DC == 2:		
	return num
else:	
	NL = [num+i+1 for i in range(100)]
	for i in NL:
		DC2 = 0
		for u in range(1,i+1):
			if i % u ==0:
				DC2 += 1
		if DC2 == 2:
			return i
'''
		


	
print(next_prime(12))# 13)
print(next_prime(24))# 29)
print(next_prime(11))# 11)
print(next_prime(13))# 13)
print(next_prime(14))# 17)
print(next_prime(33))# 37)

print(next_prime(73462))# 37)
