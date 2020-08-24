def first_before_second(s, first, second):
	NR1=s.rfind(first)
	NR2=s.rfind(second)
	inx1=s.index(first)
	inx2=s.index(second)
	return NR1 < inx2 #NR1, NR2, inx1,inx2
	#first last aperance can't be bigger than 
	#second first aperance
	#So first can't be after second
	
	
	
	
print(first_before_second("a rabbit jumps joyfully", "a", "j"))# True)
print(first_before_second("knaves knew about waterfalls", "k", "w"))# True)
print(first_before_second("maria makes money", "m", "o"))# True)
print(first_before_second("the hostess made pecan pie", "h", "p"))# True)
print(first_before_second("barry the butterfly flew away", "b", "f"))# True)
print(first_before_second("moody muggles", "m", "g"))# True)
print()
print(first_before_second("happy birthday", "a", "y"))# False)
print(first_before_second("precarious kangaroos", "k", "a"))# False)
print(first_before_second("maria makes money", "m", "i"))# False)
print(first_before_second("taken by the beautiful sunrise", "u", "s"))# False)
print(first_before_second("sharp cheddar biscuit", "t", "s"))# False)
print(first_before_second("moody muggles", "m", "o"))# False)
