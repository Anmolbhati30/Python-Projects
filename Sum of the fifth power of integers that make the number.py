
print("This code will check all numbers upo a certain value to see if the sum of the 5th power of the numbers that make up an integer returns the same value")
def sum_of_fifth_power_of_digits():
	num_array = []
	while True:
		try:
			num = int(input("Enter a number: "))
		except ValueError:
			print("plaease enter an integer value")
	for x in range(num):
		sum_val = 0
		num_list = list(str(x))
		for n in num_list:
			sum_val += int(n)**5
		if sum_val == x:
			num_array.append(x)
		else:
			pass
	print(num_array)



		

sum_of_fifth_power_of_digits()
