class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, other):
		if self.age < other.age:
			return "{} is {} me.".format(other.name, 'older than')
		if self.age==other.age:
			return "{} is {} me.".format(other.name, 'the same age as')
		if self.age>other.age:
			return "{} is {} than me.".format(other.name, 'younger than')
		
		
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2))# "Joel is older than me.")
print(p1.compare_age(p3))# "Lily is the same age as me.")

print(p2.compare_age(p1))# "Samuel is younger than me.")
print(p2.compare_age(p3))# "Lily is younger than me.")

print(p3.compare_age(p1))# "Samuel is the same age as me.")
print(p3.compare_age(p2))# "Joel is older than me.")
