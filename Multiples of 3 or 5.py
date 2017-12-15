print("This code will return all the factors of 3 and 5 upto a maximum valu, and their sum")
def mult_of_3_or_5():
	num_array = []
	while True:
		try:
			max_val = abs(int(input("Enter a number: ")))                                                   
			break                                          
		except ValueError:
			print("Enter a valid integer value")


	num = 1
	while True:

		if num > max_val:
			print("\n")
			break

		if num % 3 == 0 or num % 5 == 0:
			num_array.append(num)
		num += 1 

	print("Numbers:",*num_array)
	print("Sum:",sum(num_array))

	mult_of_3_or_5()

mult_of_3_or_5()