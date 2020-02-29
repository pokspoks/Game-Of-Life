import random

""" Generates a 2D board of desired size and optionally randomizes cell values with a given chance. """
def generate_board(width, height, randomize_values=False, active_cell_chanc=0.5):
    result = [[0]*width for _ in range(height)]

    if randomize_values == True:
        return randomize_board(result, active_cell_chanc)
    else:
        return result


""" Modifies 2D list's values to be 0 or 1 randomly. """
def randomize_board(board_state, active_cell_chance=0.5):
    height = len(board_state)
    width = len(board_state[0])

    for y in range(height):
        for x in range(width):
            rand_value = random.random()

            if rand_value < active_cell_chance:
                board_state[y][x] = 1
            else:
                board_state[y][x] = 0

    return board_state
