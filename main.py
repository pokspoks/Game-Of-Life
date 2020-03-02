import argparse
import time
import time
import msvcrt

import boardGen
import consoleRender
import gameLogic

paused = False


def main():
    parser = argparse.ArgumentParser(description="Conway's game of life.")
    parser.add_argument('--width', '-W', nargs='?', type=int, default=10,
                        help='Width of the game board in columns. Default=10')
    parser.add_argument('--height', '-H', nargs='?', type=int, default=10,
                        help='Height of the game board in rows. Default=10')
    parser.add_argument('--speed', '-s', nargs='?', type=float, default=0.2,
                        help='Game simulation speed in seconds. Default=0.2')
    parser.add_argument('--empty', '-e', nargs='?', default=True,
                        help='Start game with empty board. Default=False')
    parser.add_argument('--spawnchance', '-c', nargs='?', type=float, default=0.3,
                        help='Spawn chance of living cells as decimal percentage. Default=0.3')

    args = parser.parse_args()

    width = args.width
    height = args.height
    board = boardGen.generate_board(width, height, args.empty, args.spawnchance)
    cursor_pos = [0, 0]

    while True:
        consoleRender.render_board(board, cursor_pos)
        if not paused:
            board = gameLogic.next_board_state(board)

        if msvcrt.kbhit():
            key = str(msvcrt.getch()).replace("b'", "").replace("'", "")
            keybind_action(key, cursor_pos, height, width, board, args.speed)
            time.sleep(args.speed / 1.5)
        else:
            time.sleep(args.speed)
        consoleRender.clear_console()


def keybind_action(key, cursor_pos, width, height, board, sim_speed):
    global paused

    if key == 'w':
        if cursor_pos[0] - 1 >= 0:
            cursor_pos[0] -= 1
    elif key == 's':
        if cursor_pos[0] + 1 <= height - 1:
            cursor_pos[0] += 1
    elif key == 'a':
        if cursor_pos[1] - 1 >= 0:
            cursor_pos[1] -= 1
    elif key == 'd':
        if cursor_pos[1] + 1 <= width - 1:
            cursor_pos[1] += 1
    elif key == 'i':
        if board[cursor_pos[0]][cursor_pos[1]] == 1:
            board[cursor_pos[0]][cursor_pos[1]] = 0
        else:
            board[cursor_pos[0]][cursor_pos[1]] = 1
    elif key == 'j':
        if sim_speed - 0.1 >= 0:
            sim_speed -= 0.1
    elif key == 'k':
        sim_speed += 0.1
    elif key == 'p':
        if paused:
            paused = False
        else:
            paused = True

    return cursor_pos


if __name__ == "__main__":
    main()
