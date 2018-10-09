import os
import time
from math import floor
import keyboard
from random import randint

clear = lambda: os.system('cls')









HEIGHT = 20
WIDTH = 20
DEFAULT_DIRECTION = 1
FPS = 1

last_direction = None


def main():
    # set the initial state of the game
    game_state = init()
    while True:
        frame_start_time = time.time()
        # gets the user input
        user_input()
        # calculates the game state
        # print("Snake starts as:", game_state[0])
        # print("About to perform physics on", game_state)
        game_state = physics(game_state)
        # creates the visual representaition from the information of the game
        graphics(game_state, frame_start_time)
    # cleanly close the program
    tear_down()


def init():
    global last_direction
    last_direction = DEFAULT_DIRECTION
    # game state is an array containing the locations of snake and fruit
    game_state = []
    # create the snake data using LIST COMPREHENSION #swag
    snake_data = [[floor(WIDTH/2) + n, floor(HEIGHT/2)] for n in range(3)]
    game_state.append(snake_data)
    # create the fruit data
    # legal_values = False
    # while not legal_values:
    #     # generates a random x and y value, candidates for the fruit coordinates
    #     potential_fruit_coords = [randint(1, WIDTH - 2), randint(1, HEIGHT - 2)]
    #     # checks that the x and y pair is not already occupied by the snek
    #     if potential_fruit_coords not in snake_data:
    #         legal_values = True
    fruit = new_fruit(snake_data)

    game_state.append(fruit)
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


def physics(state):
    global last_direction
    new_snake = []
    last_bit = state[0][len(state[0]) - 1]
    for i in range(len(state[0]) - 1, 0, -1):
        new_snake.insert(0, state[0][i-1])
    if last_direction == 0:
        new_snake.insert(0, [state[0][0][0], state[0][0][1] - 1])
    if last_direction == 1:
        new_snake.insert(0, [state[0][0][0] - 1, state[0][0][1]])
    if last_direction == 2:
        new_snake.insert(0, [state[0][0][0], state[0][0][1] + 1])
    if last_direction == 3:
        new_snake.insert(0, [state[0][0][0] + 1, state[0][0][1]])
    # checks to see if the head has consumed the fruit
    if new_snake[0] == state[1]:
        # adds the last part of the original snake to the snake
        new_snake.append(last_bit)
        # creates a new fruit that is on a different part of the board
        fruit = new_fruit(new_snake)
    else:
        fruit = state[1]

    return [new_snake, fruit]

def new_fruit(snake_data):
    legal_values = False
    while not legal_values:
        # generates a random x and y value, candidates for the fruit coordinates
        potential_fruit_coords = [randint(1, WIDTH - 2), randint(1, HEIGHT - 2)]
        # checks that the x and y pair is not already occupied by the snek
        if potential_fruit_coords not in snake_data:
            legal_values = True
    return potential_fruit_coords


def user_input():
    global last_direction
    if keyboard.is_pressed('w'):
        last_direction = 0
    if keyboard.is_pressed('a'):
        last_direction = 1
    if keyboard.is_pressed('s'):
        last_direction = 2
    if keyboard.is_pressed('d'):
        last_direction = 3















def grid_to_cell_index(x,y):
    return y * HEIGHT + x

















































if __name__ == "__main__":
    main()
