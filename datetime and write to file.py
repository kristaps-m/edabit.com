import random
import datetime

FO = open('cowsandbulls.txt', 'a') #file open
XX = str(random.randint(1, 5)) # 4 dig numb can't be 22 so it start form 1k str(2020)#
DT = datetime.datetime.now()

#print(x.strftime("%d.%m.%Y // %H:%M::%S"))
FO.write(XX+' // '+str(DT.strftime("%d.%m.%Y // %H:%M::%S")+'\n'))

while True:
	UI = input("Gues number from 1 to 5: ")
	if UI == XX:
		print('You have won')
		break
	else:
		print('Wrong number')


FO.close()
