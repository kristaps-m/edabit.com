#Given an int, figure out how many ones, threes and nines you could fit into the number. 
#You must create a class. You will make variables(self.ones, self.threes, self.nines) to do this.

class ones_threes_nines:
	def __init__(self, num):
		self.ones = num // 1
		self.threes = num // 3
		self.nines = num // 9
	
n1 = ones_threes_nines(0)
print(n1.ones, 0)
n2 = ones_threes_nines(1)
print(n2.threes, 0)
n3 = ones_threes_nines(2)
print(n3.nines, 0)
n4 = ones_threes_nines(3)
print(n4.ones, 3)
n5 = ones_threes_nines(4)
print(n5.threes, 1)
n6 = ones_threes_nines(10)
print(n6.nines, 1)
n7 = ones_threes_nines(13)
print(n7.ones, 13)
n8 = ones_threes_nines(15)
print(n8.threes, 5)
n9 = ones_threes_nines(17)
print(n9.nines, 1)
n10 = ones_threes_nines(20)
print(n10.nines, 2)
