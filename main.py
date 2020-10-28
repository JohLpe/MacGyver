import pygame as pg
import sys
from board import Board

pg.init()


def main():
    """Main code to run the game."""

    board = Board()
    board.verify_items_placement()
    playable = True

    while playable:

        board.init_board()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                playable = False
                pg.quit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    board.hero.move_right(board)
                if event.key == pg.K_LEFT:
                    board.hero.move_left(board)
                if event.key == pg.K_UP:
                    board.hero.move_up(board)
                if event.key == pg.K_DOWN:
                    board.hero.move_down(board)
                if event.key == pg.K_r and board.end_game:
                    main()
                if event.key == pg.K_q and board.end_game or\
                   event.key == pg.K_a and board.end_game:
                    sys.exit()
            else:
                pass


if __name__ == "__main__":
    main()
