import os


def render_board(board_state, dead_cell_char=' ', alive_cell_char='O', horizontal_border_char='-', vertical_border_char='|'):
    buffer = ''
    first_cell = True

    print_horizontal_border(board_state, horizontal_border_char)

    for row in board_state:
        for cell in row:
            if first_cell == True:
                buffer += vertical_border_char
                first_cell = False

            if cell == 1:
                buffer += alive_cell_char
            else:
                buffer += dead_cell_char
        buffer += vertical_border_char

        print(buffer)

        buffer = ''
        first_cell = True

    print_horizontal_border(board_state, horizontal_border_char)


def print_horizontal_border(board_state, char):
    buffer = ''
    for _ in range(len(board_state[0]) + 2):
        buffer = buffer + char

    print(buffer)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
