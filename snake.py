import os
import time
from math import floor
import keyboard
from random import randint

clear = lambda: os.system('cls')









HEIGHT = 20
WIDTH = 20
FPS = 60

def main():
    # set the initial state of the game
    game_state = init()
    while(True):
        frame_start_time = time.time()
        # gets the user input
        result_of_input = user_input()
        # calculates the game state
        game_state = physics(result_of_input, game_state)
        # creates the visual representaition from the information of the game
        # state
        graphics(game_state, frame_start_time)

    # cleanly close the program
    tear_down()


def init():
    # game state is an array containing the locations of snake and fruit
    game_state = []
    # create the snake data using LIST COMPREHENSION #swag
    snake_data = [[floor(WIDTH/2) + n, floor(HEIGHT/2)] for n in range(3)]
    game_state.append(snake_data)
    # create the fruit data
    legal_values = False
    while not legal_values:
        # generates a random x and y value, candidates for the fruit coordinates
        potential_fruit_coords = [randint(1, WIDTH - 2), randint(1, HEIGHT - 2)]
        # checks that the x and y pair is not already occupied by the snek
        if potential_fruit_coords not in snake_data:
            legal_values = True

    game_state.append(potential_fruit_coords)
    return game_state


def graphics(game_state, frame_start_time):
    board = ""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # check if coordinates produced match the game state
            coordinates = [x, y]
            if coordinates == game_state[1]:
                board += 'F'
            elif coordinates in game_state[0]:
                if coordinates == game_state[0][0]:
                    # draws head
                    board += 'O'
                else:
                    # draws body
                    board += 'o'
            # draws wall
            elif x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1:
                # draws wall
                board += '#'
            # draws unoccupied cell
            else:
                board += ' '
                #draws nothing
        board += '\n'
    print(board)
    delta_time = time.time() - frame_start_time
    time.sleep(max(1/FPS, 1/FPS - delta_time))
    clear()


def physics(direction, state):
    #checks where the snake is
    snake = state[0]
    snake_head = snake[0]
    new_snake = []
    # if up
    if direction == 0:
        snake_head[1] -= 1
    #if left
    if direction == 1:
        snake_head[0] -= 1
    # if down
    if direction == 2:
        snake_head[1] += 1
    # if right
    if direction == 3:
        snake_head[0] += 1
    new_snake.append(snake_head)
    # iterates through the former snake and takes all but the last one
    for part in snake:
        new_snake.append(part)
    return [new_snake, state[1]]
    #increments the head by the direction, then replaces each body part with the last.






def user_input():
    if keyboard.is_pressed('w'):
        return 0
    if keyboard.is_pressed('a'):
        return 1
    if keyboard.is_pressed('s'):
        return 2
    if keyboard.is_pressed('d'):
        return 3














def grid_to_cell_index(x,y):
    return y * HEIGHT + x

















































if __name__ == "__main__":
    main()

