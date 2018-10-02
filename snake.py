import os
import time
from random import randint

clear = lambda: os.system('cls')









HEIGHT = 20
WIDTH = 20

def main():
    # set the initial state of the game
    game_state = init()
    while(True):
        # gets the user input
        #result_of_input = user_input()
        # calculates the game state
        #game_state = physics(result_of_input)
        # creates the visual representaition from the information of the game
        # state
        graphics(game_state)
    # cleanly close the program
    #tear_down()
    
# 0 = empty space
# 1 = boundary
# 2 = fruit
# 3 = snake head
# 4 = snake body
def init():
    cells = []
    # initialize the game board
    fruit = [randint(0, WIDTH), randint(0, HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # check if cell is a boundary
            if x == 0 or y == 0 or x == WIDTH - 1 or y == HEIGHT - 1:
                cells.append(1)
            elif x == fruit[0] and y == fruit[1]:
                cells.append(2)
            else:
                cells.append(0)
    return cells


def graphics(game_state):
    # board output is a string representation of the board
    board_output = ""
    # decides which symbol each cell state is represented by
    symbol_lookup = ['e','b','2','3','4']
    # runs a for loop for each cell
    for i in range(WIDTH * HEIGHT):
        # makes a new line if the line is the width of the board 
        if i % WIDTH == 0 and i > 0:
            board_output += '\n'
        board_output += symbol_lookup[game_state[i]]
    # clears the screen
    clear()
    # prints the completed string that represents the board
    print(board_output)
    time.sleep(0.016)
    

    
            
        
        
    







































if __name__ == "__main__":
    main()
    
