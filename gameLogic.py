def next_board_state(board_state):
    new_board_state = []

    for y, row in enumerate(board_state):
        new_board_state.append([])
        for x, cell in enumerate(row):
            neighbours = get_neighbours(board_state, x, y)

            if cell == 1:
                if neighbours < 2:
                    new_board_state[y].append(0)
                if neighbours > 1 and neighbours < 4:
                    new_board_state[y].append(1)
                if neighbours > 3:
                    new_board_state[y].append(0)
            else:
                if neighbours == 3:
                    new_board_state[y].append(1)
                else:
                    new_board_state[y].append(0)

    return new_board_state


def get_neighbours(board_state, x, y):
    neihgbours = 0
    width = len(board_state[0]) - 1
    height = len(board_state) - 1

    # V+1
    if y + 1 < height:
        if board_state[y+1][x] == 1:
            neihgbours += 1
    # V-1
    if y - 1 > 0:
        if board_state[y-1][x] == 1:
            neihgbours += 1
    # H+1
    if x + 1 < width:
        if board_state[y][x+1] == 1:
            neihgbours += 1
    # H-1
    if x - 1 > 0:
        if board_state[y][x-1] == 1:
            neihgbours += 1
    # V+1,H+1
    if y + 1 < height and x + 1 < width:
        if board_state[y+1][x+1] == 1:
            neihgbours += 1
    # v-1,H-1
    if y - 1 > 0 and x - 1 > 0:
        if board_state[y-1][x-1] == 1:
            neihgbours += 1
    # V+1,H-1
    if y + 1 < height and x - 1 > 0:
        if board_state[y+1][x-1] == 1:
            neihgbours += 1
    # V-1,H+1
    if y - 1 > 0 and x + 1 < width:
        if board_state[y-1][x+1] == 1:
            neihgbours += 1

    return neihgbours
