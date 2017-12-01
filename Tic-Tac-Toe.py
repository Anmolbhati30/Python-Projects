import time

def home():
	print("""

Player 1 = X
Player 2 = O

Player 1 goes first

The numbers in the box correspind to that move.
	 """)


def move():
    global moves
    moves = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,        
    }

    global options
    options = []

    for i in moves:
        options.append(moves[i])

def board():
    global moves
    print(' --- --- ---') 
    print('|',moves['a'],'|',moves['b'],'|',moves['c'],'|') 
    print(' --- --- ---')  
    print('|',moves['d'],'|',moves['e'],'|',moves['f'],'|')
    print(' --- --- ---')  
    print('|',moves['g'],'|',moves['h'],'|',moves['i'],'|')
    print(' --- --- ---') 




	#print(moves['a'],moves['b'],moves['c'])
	#print(moves['d'],moves['e'],moves['f'])
	#print(moves['g'],moves['h'],moves['i'])

def tictactoe():

    global game_finish
    game_finish = False

    if game_finish is False:
        player1()
    else:
        win_screen()

def player1():
    global a,b,c,d,e,f,g,h,i,board,game_finish,options,lastmove 
    lastmove = 'p1'
    print("Available moves:",*options)

    while True:
        try:    
            p1turn = int(input(" Player 1 - Make a turn: "))
            break
        except ValueError:
            print("Please make a valid move:")

    while True:
        if p1turn not in options:
            print("That move is not available")
            while True:
                try:    
                    p1turn = int(input("Player 1 - Make a turn: "))
                    break
                except ValueError:
                    print("Please make a valid move:")
        else:
            options.remove(p1turn)
            break
    
    

    for i in moves:
        if moves[i] == p1turn:
            moves[i] = 'X'

    board()
    time.sleep(0.5)
    win_check()
    player2()

def player2():
    
    global a,b,c,d,e,f,g,h,i,board,game_finish,options,lastmove
    lastmove = 'p2'

    print("Available moves:",*options)

    while True:
        try: 
            p2turn = int(input("Player 2 - Make a turn: "))
            break
        except ValueError:
            print("Please make a valid move:")

    while True:
        if p2turn not in options:
            print("That move is not available")
            while True:
                try:    
                    p2turn = int(input("Player 2 - Make a turn: "))
                    break
                except ValueError:
                    print("Please make a valid move:")
        else:
            options.remove(p2turn)
            break
    

    for i in moves:
        if moves[i] == p2turn:
            moves[i] = 'O'

    board()
    time.sleep(0.5)
    win_check()
    player1()

def win_check():

    global lastmove
    
    if moves['a'] == moves['b'] == moves['c'] or moves['d'] == moves['e'] == moves['f'] or moves['g'] == moves['h'] == moves['i']: # rows win
        game_finish = True
        win_screen()

    elif moves['a'] == moves['d'] == moves['g'] or moves['b'] == moves['e'] == moves['h'] or moves['c'] == moves['f'] == moves['i']: # columns win
        game_finish = True
        win_screen()

    elif moves['a'] == moves['e'] == moves['i'] or moves['c'] == moves['e'] == moves['g']: # diagonals win
        game_finish = True
        win_screen()

    else:
        draw_check()
        pass

def draw_check():
    if all(moves[i] == 'X' or moves[i] == 'O' for i in moves):
    	draw_screen()
    else:
        pass

def win_screen():

    if lastmove == 'p1':
   	    print("Player 1 won!")
    elif lastmove == 'p2':
   	    print("Player 2 won")
    else:
    	print("Error")

    time.sleep(0.5)

    ask = input("Would you like to play again? ")
    if ask == 'Yes' or ask == 'yes' or ask == 'y' or ask == 'Y':
        game_start()

    else:
        print('Thanks for playing!')
        time.sleep(1.5)
        quit()

def draw_screen():
    print('Draw!')
    time.sleep(0.5)

    ask = input("Would you like to play again? ")
    if ask == 'Yes' or ask == 'yes' or ask == 'y' or ask == 'Y':
        game_start()

    else:
        print('Thanks for playing!')
        time.sleep(1.5)
        quit()
   
def game_start():
    home()
    move()
    board()
    tictactoe()
    
game_start()
