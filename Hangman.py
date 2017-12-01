import time
import string
alphabet = list(string.ascii_lowercase)
for x in string.ascii_uppercase:
    alphabet.append(x)

special_chars = [" ", "-"]


def hangman():
    global mistakes
    if mistakes == 1:
    	print("""

	    | 
	    |         
	    |        
	    |        
	    |
	    |

		""")
    if mistakes == 2:
	    print("""
	     _________
	    |        
	    |        
	    |        
	    |        
	    |
	    |

		""")
    if mistakes == 3:
        print("""	
	     _________
	    |         |
	    |        
	    |        
	    |        
	    |
	    |

		""")
    if mistakes == 4:
        print("""
             _________
	    |         |
	    |         0
	    |        
	    |        
	    |
	    |

		""")
    if mistakes == 5:
        print("""
	     _________
	    |         |
	    |         0
	    |         |
	    |        
	    |
	    |

		""")
    if mistakes == 6:
        print("""
	     _________
	    |         |
	    |         0""")
        print("            |        /|""\\")
        print("""            |        
	    |
	    |
	    """)
	
    if mistakes == 7:
        print ("""
             _________
            |         |
            |         0""")
        print("            |        /|""\\")
        print(" 	    |        / ""\\")
        print("""            |
            |

                """)	


    else:
        pass
		



def word_input():
    global incorrect
    incorrect = []
    global mistakes
    mistakes = 0
    global word
    word = str(input("Enter a word: "))
    global word_array
    word_array = []
    for x in word:
        if x in alphabet or x in special_chars:
            pass
        else:
            print("Please enter a valid word")
            word_input()


    for i in word:
    	word_array.append(i)
    print(*word_array)
    print("\n"*50)
   

    global guessed_word
    guessed_word = []
    for x in word:
        if x in special_chars:
            guessed_word.append(x)
        else:
            guessed_word.append("_")
    print("Word:",*guessed_word)
    



def display():
    print("\n"*50)
    print("Word:",*guessed_word,'\n')
    print("Incorrect guessed letters:",*incorrect)
    hangman()




def word_guess():
    global guess,mistakes
    guess = input("\nGuess a letter: ")
    

    if len(guess) > 1 or guess not in alphabet:
        print("Please guess a valid letter")
        word_guess()
    elif guess in guessed_word or guess in incorrect:
        print("You have already guessed this letter")
        word_guess()
    else:
        word_check()




def word_check():
    global mistakes
    
    if any(i == guess for i in word_array):
        print("Correct Guess")
        for x in range(len(word_array)):
            if word_array[x] == guess:
                guessed_word[x] = guess
                
        display()
        win_check()    


    else:
        incorrect.append(guess)
        mistakes += 1

        display()
        win_check()

    word_guess()

def win_check():
    
    global mistakes
    if mistakes >= 7:
        print("You Lost! - The word was:",word)
        replay = input("Would you like to play again? ")

        if replay == "yes" or replay == "y":
            game_start()
        else:
            print("Thanks for playing")        
            time.sleep(1.5)
            quit()    
    elif all(i != '_' for i in guessed_word):
        print("You Won!")
        
        replay = input("Would you like to play again? ")

        if replay == "yes" or replay == "y":
            game_start()
        else:
            print("Thanks for playing")
            time.sleep(1.5)
            quit()
    
    else:
        pass

def game_start():
    word_input()
    word_guess()

game_start()
