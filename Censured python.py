def uncensor(txt, vowels):	
	txt = txt.replace('*', '{}')
	return txt.format(*vowels)
	
	'''
	EN = list(enumerate(txt))
	C = 0
	#print(EN)
	NS = ''
	for indx, l in EN:
		if l == '*':
			EN[indx] = vowels[C]
			NS += EN[indx]
			C += 1
		if l != '*':
			NS += txt[indx]
	return NS
	'''
	
print(uncensor('Wh*r* d*d my v*w*ls g*?', 'eeioeo'))# 'Where did my vowels go?')
print(uncensor('abcd', ''))# 'abcd', 'Works with no vowels.')
print(uncensor('*PP*RC*S*', 'UEAE'))# 'UPPERCASE', 'Works with uppercase')
print(uncensor('Ch**s*, Gr*mm*t -- ch**s*', 'eeeoieee'))# 'Cheese, Grommit -- cheese', 'Works with * at the end')
print(uncensor('*l*ph*nt', 'Eea'))# 'Elephant', 'Works with * at the start')
