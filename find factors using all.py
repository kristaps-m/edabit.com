#https://edabit.com/challenge/cSwpsZqMoSMvQFizB
#Write a function that returns True if all integers in a list are factors of a number, and False otherwise.
def check_factors(factors, num):
	return all([num%i == 0 for i in factors])

print(check_factors([2, 3, 4], 12))# True)
print(check_factors([1, 2, 3, 8], 12))# False, '8 is not a factor of 12')
print(check_factors([1, 2, 50], 100))# True)
print(check_factors([1, 9, 81], 81))# True)
print(check_factors([5, 10, 50], 500))# True)
print(check_factors([5, 10, 499], 500))# False, '499 is not a factor of 500')
print(check_factors([3, 6], 9))# False, '6 is not a factor of 9')
'''
	for i in factors:
		if num % i == 0:
			print(i)
			
			
	X = 0
	for i in factors:					
		X = X + (num % i)
	if X==0:
		print(True)
	if X >0:
		print(False)
		
			
			
			
	X = []
	for i in range(1,num+1):
		if num % i == 0:
			X.append(i)
			
	ToF = None
	for i in factors:
		if i in X:
			ToF = True
		else:
			ToF = False
	return ToF
			'''
