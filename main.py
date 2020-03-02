import boardGen
import consoleRender
import gameLogic
import argparse
from time import sleep

parser = argparse.ArgumentParser(description="Conway's game of life.")
parser.add_argument('--width', '-W', nargs='?', type=int, default=30, help='Width of the game board in columns. Default=30')
parser.add_argument('--height', '-H', nargs='?', type=int, default=30, help='Height of the game board in rows. Default=30')
parser.add_argument('--speed', '-s', nargs='?', type=float, default=0.2, help='Game simulation speed in seconds. Default=0.2')
parser.add_argument('--spawnrate', '-S', nargs='?', type=float, default=0.3, help='Spawn rate of cells as decimal percentage. Default=0.3')

args = parser.parse_args()

width = args.width
height = args.height
board = boardGen.generate_board(width, height, True, args.spawnrate)

while True:
    consoleRender.render_board(board)
    board = gameLogic.next_board_state(board)
    sleep(args.speed)
    consoleRender.clear_console()
