import random
import os
import time

# define the board
board = {1, 2, 3,
         4, 5, 6,
         7, 8, 9}

print "***TIC-TAC-TOE GAME***"


# create the board
def show():
    print  board[0], '|', board[1], '|', board[2]
    print '----------'
    print board[3], '|', board[4], '|', board[6]
    print '----------'
    print board[7], '|', board[8], '|', board[9]


while True:
    # os.system('clear')
    choice = raw_input("Select the spot")
    choice = int(choice)
    board[choice] = "x"
    # Check to see if the space is empty
    if (board[choice] != ''):
        print"Whitespace is not empty"
    else:
        board[choice] = "X"

show()
