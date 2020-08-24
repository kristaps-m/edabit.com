#http://www.learningaboutelectronics.com/Articles/How-to-count-the-number-of-objects-in-a-class-in-Python.php

class User:
	user_count = 0
	def __init__(self, username):
		self.username=username
		User.user_count += 1
	
#print(User.user_count, 0)

u1 = User("johnsmith10")
print(User.user_count)#, 1)
print(u1.username, "johnsmith10")


u2 = User("marysue1989")
print(User.user_count, 2)
print(u2.username, "marysue1989")

u3 = User("milan_rodrick")
print(User.user_count, 3)
print(u3.username, "milan_rodrick")

user4 = User("joshua_senoron")
print(User.user_count, 4)
print(user4.username, "joshua_senoron")

user10 = User("LuckyLootCrate123")
print(User.user_count, 5)
print(user10.username, "LuckyLootCrate123")
