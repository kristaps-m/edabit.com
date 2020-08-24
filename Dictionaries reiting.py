

D = {
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}
L = {}

for k, v in D.items():	
	if v == '***':
		L[k] = v		
print(L)
	
#print(D.values())
