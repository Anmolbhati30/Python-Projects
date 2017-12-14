import time	
print("The code will find the smallest integer that is perfectly divisible by 1 to your number")  # Menu
def div_by():																					  # Define function
	
	while True:
		try:
			num = int(input("Enter a number: "))                                                  # Range input
			if num != 0:
				break 																			  # Break loop
			else:
				print("Enter a non-zero integer value")                                           # Error handling
		except ValueError:
			print("Enter a valid integer value")                                                  # Non-zero, non-float check
	
	number = 1                                                                                    # Start of range
	
	while True:
		if all(number%(x+1) == 0 for x in range(num)):                                            # Range check
			break																				  # Break loop
		number += 1                                                                               # Check next number
			

	print('The smallest number divisible by numbers 1 -',num,' is:',number)                              # Display

	while True:
		ask = input("Would you like to test a new range? (y/n): ")                                # Ask user if they want to check another range

		if ask == 'y' or ask == 'Y':                                                              # 'Yes' Check
			div_by()                                                                              # Action for yes - restart function
			break 																				  # Break loop
		elif ask == 'n' or ask == 'N':                                                            # 'No' Check
			print("Bye!")																		  # Quit message
			time.sleep(0.5)  																	  # Time to read message                                                                     
			quit()																				  # Action for no - quit program
		else:
			print("Please make a valid choice (y/n)")                                             # Error handling


div_by()