print("This function prints all the smallest numbers divisible by: 1, 1 -> 2, 1 -> 3,.., 1 -> num; where num is your number")
def div_by_upto():


	while True:
		try:
			num = int(input("Enter a number: "))                                                   
			if num != 0:
				break 																			   
			else:
				print("Enter a non-zero integer value")                                            
		except ValueError:
			print("Enter a valid integer value")
	
	number = 1
	test_num = 1
	
	while True:
		
		if num < test_num:
			break

		if all(number%(x+1) == 0 for x in range(test_num)):
			print("Smallest number divisible by all numbers upto:\n")
			print("{} : {}".format(test_num,number))
			test_num += 1
		number += 1

	div_by_upto()


div_by_upto()
