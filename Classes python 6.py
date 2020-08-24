class player():

	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight
		
	def get_age(self):	
		return '{} is age {}'.format(self.name, self.age)
		
	def get_height(self):	
		return '{} is {}cm'.format(self.name, self.height)
		
	def get_weight(self):	
		return '{} weighs {}kg'.format(self.name, self.weight)
		
		
		
player1 = player('Patrick Mahomes', 24, 188, 104)
player2 = player('Jimmy Garoppolo', 28, 188, 102)
player3 = player('Julio Jones', 31, 191, 100)

print(player1.get_age(), 'Patrick Mahomes is age 24')
print(player1.get_height(), 'Patrick Mahomes is 188cm')
print(player1.get_weight(), 'Patrick Mahomes weighs 104kg')

print(player2.get_age(), 'Jimmy Garoppolo is age 28')
print(player2.get_height(), 'Jimmy Garoppolo is 188cm')
print(player2.get_weight(), 'Jimmy Garoppolo weighs 102kg')

print(player3.get_age(), 'Julio Jones is age 31')
print(player3.get_height(), 'Julio Jones is 191cm')
print(player3.get_weight(), 'Julio Jones weighs 100kg')
