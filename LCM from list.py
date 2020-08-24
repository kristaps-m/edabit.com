
def lcm_of_list(numbers):
	# getting prime factors from both lists
	BIGL = [PF(i) for i in numbers]
	# making short list to look for countables
	Mega = sorted(set(n for sublst in BIGL for n in sublst))
	L = []
	# this loop goes trugh all prime factors
	# and rises prime factor to the power of
	# max() factor count
	# if max count of 2's in one list are 4
	# then L.append(2**4)
	for i in Mega:
		L.append(i**max([l.count(i) for l in BIGL]))
	# multiples all intigers in L
	return eval("*".join(map(str,L)))
	
def PF(X): #prime factors
    d = 2
    L = []
    while X != 1:
        #print(d, X,L)
        if X % d == 0:
            L.append(d)
            X = X // d
        else:
            d+=1
    return L
	
print(lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2520)
print(lcm_of_list([13, 6, 17, 18, 19,20, 37]), 27965340)
print(lcm_of_list([44, 64, 12, 17, 65]), 2333760)
print(lcm_of_list([200, 30, 18, 11, 8, 64, 34]), 2692800)
print()
# ~ print(lcm(10000000000000000, 3333333333333333))

# 2 * 15 = 2 * 3 * 5 =30
