import os


def render_board(
        board_state,
        cursor_pos,
        dead_cell_char=' ',
        dead_cell_highlight_char='█',
        alive_cell_char='O',
        alive_cell_higlight_char='●',
        horizontal_border_char='-',
        vertical_border_char='|'):

    buffer = ''
    first_cell = True

    print_horizontal_border(board_state, horizontal_border_char)

    for r, row in enumerate(board_state):
        for c, cell in enumerate(row):
            if first_cell == True:
                buffer += vertical_border_char
                first_cell = False

            if cell == 1:
                if [r, c] == cursor_pos:
                    buffer += alive_cell_higlight_char
                else:
                    buffer += alive_cell_char
            else:
                if [r, c] == cursor_pos:
                    buffer += dead_cell_highlight_char
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
