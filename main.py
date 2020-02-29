import boardGen
import consoleRender
import gameLogic
import argparse
from time import sleep

parser = argparse.ArgumentParser(description="Conway's game of life.")
parser.add_argument('--width', '-W', nargs='?', default=30, type=int, help='Width of the game board as columns.')
parser.add_argument('--height', '-H', nargs='?', default=30, type=int, help='Height of the game board as rows.')
parser.add_argument('--speed', '-s', nargs='?', default=0.2, type=float, help='Game simulation speed.')
parser.add_argument('--spawnrate', '-S', nargs='?', default=0.3, type=float, help='Spawn rate of cells.')

args = parser.parse_args()

width = args.width
height = args.height
board = boardGen.generate_board(width, height, True, args.spawnrate)

while True:
    consoleRender.render_board(board)
    board = gameLogic.next_board_state(board)
    sleep(args.speed)
    consoleRender.clear_console()
