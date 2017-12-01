import random
import math
def pi2o6():
	coprime = 0
	cofactor = 0


	for x in range(1000000):
		random_num1 = random.randint(0,120)
		random_num2 = random.randint(0,120)
		if math.gcd(random_num1,random_num2) == 1:
			coprime += 1
		else:
			cofactor += 1


	print(coprime, cofactor)

	print(coprime/1000000)

pi2o6()