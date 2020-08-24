
def lcm(a, b):
	# getting prime factors from both lists
	PFa = PF(a)
	PFb = PF(b)
	# making short list to look for countables
	Mega = sorted(set((PFa + PFb)))
	L = []
	# this loop compares both list and adds to L
	# if [2,2,2,2] in first list are more than [2,2]
	# the loop append 2**4 to L
	for i in Mega:
		if PFa.count(i) > PFb.count(i):
			L.append(i**PFa.count(i))
		elif PFa.count(i) == PFb.count(i):
			L.append(i**PFa.count(i))
		else:
			L.append(i**PFb.count(i))
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
	
print(lcm(6, 10), 30) # 2,3    // 2 , 5
print(lcm(30, 60), 60)
print(lcm(10000, 333), 3330000)
print(lcm(75, 135), 675)
print(lcm(102, 2), 102)
print()
print(lcm(10000000000000000, 3333333333333333))

# 2 * 15 = 2 * 3 * 5 =30
