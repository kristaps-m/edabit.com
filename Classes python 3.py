class Name:
	def __init__(self, fname, lname):
			self.fname = fname.capitalize()
			self.lname = lname.capitalize()
			self.fullname = '{} {}'.format(fname.capitalize(),lname.capitalize())
			self.initials = '{}.{}'.format(fname[0].upper(),lname[0].upper())



a1 = Name("john", "SMITH")
print(a1.fname)#, "John")
print(a1.lname, "Smith")
print(a1.fullname, "John Smith")
print(a1.initials, "J.S")

a2 = Name("sARah", "fRolliE")
print(a2.fname, "Sarah")
print(a2.lname, "Frollie")
print(a2.fullname, "Sarah Frollie")
print(a2.initials, "S.F")
