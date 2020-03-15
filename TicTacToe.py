# -*- coding: utf-8 -*-
"""
Python Bootcamp from Zero to Hero Udemy Course
Milestone 1 Project

Tic Tac Toe computer game for two players.
"""

# define clear_display function 
def clear_output():
    
    # for windows
    if name == 'nt':
        system('cls')
        return

    # for mac and linux(here, os.name is 'posix') 
    system('clear') 
    return

# Function to check for win or tie. Returns True when game over.
def done(board_xo, player, ch):
    winners=[  # This defines the winning rows/cols/diags.
        [1,2,3],[4,5,6],[7,8,9],
        [1,4,7],[2,5,8],[3,6,9],
        [1,5,9],[7,5,3]
    ]
    
    for i in winners:  # Check all possible wins
        # Make the row/col/diag a set that might only have all Xs or Os... just 1 char.
        sq_val = set(board_xo[i[0]] + board_xo[i[1]] + board_xo[i[2]])

        if sq_val == set(ch): # Does the winner row/col/diag only contain an X or O?
            print (f'\n{player} wins, congratulations!')
            return True
    if ' ' in list(board_xo.values()): # Empty squares exist.
        return False # Keep going in for loop.
    else: # No more blank squares available, so cat's game.
        print(f'\nThe cat wins, way to go Harley!')
        return True
        
# Function to input a player's square
def get_square(board_xo, player, ch):

    while True: # Repeat until input is correct.
        x_key = input(f'\n{player} ({ch}), enter your square using the numeric keypad... ')
        if x_key.isdigit():
            x_key = int(x_key)
            if 1 <= x_key <= 9:
                if board_xo[x_key] == ' ':
                    board_xo[x_key] = ch
                    break
                else: print (f'Square already taken by {board_xo[x_key]}, try an empty square, {player}!')
            else: print(f'Number entered must be between 1 and 9, {player}.')
        else: print(f'Entry must be a number, {player}.')

    return board_xo

def paint_board(board_xo):
    board = [list('   |   |   ') for _ in range(11)] # Initialize blank tic-tac-toe grid
    board[3] = board[7] = list('-----------')
    
    # Create map that identifies cells in the grid.
    ttt_map={1:[9,1],2:[9,5],3:[9,9],4:[5,1],5:[5,5],6:[5,9],7:[1,1],8:[1,5],9:[1,9]}

    for i in range(1,10):
        board[ ttt_map.get(i)[0]][ttt_map.get(i)[1]] = board_xo.get(i)
    for i in board: print("".join(i))

# Function to get & show a player's move. Returns True when game over.
def move(board_xo, player, ch):
    board_xo = get_square(board_xo,player,ch)
    clear_output(); print() # Start with a blank line.
    paint_board(board_xo)
    return done(board_xo, player, ch)

# This is the main loop
def main():
    while True:
        # Randomly select who goes first.
        input('\nPress Enter to start.')
        clear_output()

        if bool(random.getrandbits(1)): playerX = player1; playerO = player2
        else: playerX = player2; playerO = player1
        print ('\nFlipping a coin, please wait...')  # Make the coin flipping a little more exciting.
        for i in range(0,10):
            print('.'*(i+1))
            sleep(0.2)
        sleep(0.5)
        clear_output()
        print('\n ' + playerX + ' is X and goes first, ' + playerO + ' is O and goes second.\n')
  
        # Create the blank board
        board_xo = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        paint_board(board_xo)

        while True:  # Forever loop to alternately take X & O moves & break out when done.
            if move(board_xo,playerX,'X'): break
            if move(board_xo,playerO,'O'): break
                
        yes_no = input ('\nDo you want to play again? (Enter y or n) ')
        if yes_no.lower() == 'y': clear_output()
        else: return

# import system and system name from os 
from os import system, name

import random # random functions library

# import sleep time delays
from time import sleep 

# Clear the screen 
clear_output()
print ('\nWelcome to Grandpa\'s Tic-Tac-Toe Game!')
print ('This is a two player game pitting X vs O')
player1 = input ('\nPlayer 1, what is your name? ')
player2 = input ('\nPlayer 2, what is your name? ')
print()

print ('To select your square, use numeric keypad keys 1 through 9 followed by Enter')
print ('Here is how the keypad keys are mapped...\n')
board_map = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
paint_board(board_map)
print ('\nNOTE... Hit Ctrl-C (^C) any time to quit!')

main()

print("\nThank you for playing.  Grandpa says hi!")
sleep(3)