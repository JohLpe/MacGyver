import pygame as pg
import sys
from init_board import Board

pg.init()


def main():

    board = Board()
    playable = True

    while playable:

        board.init_board_visual(board)
        for event in pg.event.get():

            if event.type == pg.QUIT:
                playable = False
                pg.quit()

            elif event.type == pg.KEYDOWN:
                board.hero.move(board, event)
                if event.key == pg.K_r and board.endGame:
                    playable = False
                    break
                if event.key == pg.K_q and board.endGame or\
                   event.key == pg.K_a and board.endGame:
                    sys.exit()
            else:
                pass
    main()


if __name__ == "__main__":
    main()
