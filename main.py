import boardGen
import consoleRender
import gameLogic
from time import sleep

width = 269
height = 64
board = boardGen.generate_board(width, height, True, 0.3)

while True:
    consoleRender.render_board(board)
    board = gameLogic.next_board_state(board)
    sleep(0.1)
    consoleRender.clear_console()
