import pygame as pg
from game import Game

pg.init()


def main():

    pg.display.set_caption("MacGyver Escape")
    board = pg.display.set_mode((600, 600))

    background = pg.image.load('ressource/void.png')
    inventory = pg.image.load('ressource/inventory.png')
    pg.mixer.music.load('ressource/bgst.mp3')
    pg.mixer.music.play()

    game = Game()
    game.verifyItemsPlacement()

    playable = True

    while playable:
        """loop to make the game work"""

        board.blit(background, (0, 0))
        for coordinates in game.walls.wall_tiles():
            board.blit(game.walls.image, coordinates)
        for coordinates in game.floor.floor_tiles():
            board.blit(game.floor.image, coordinates)
        board.blit(inventory, (210, 562))
        board.blit(game.upstairs.image, game.upstairs.placementU)
        board.blit(game.downstairs.image, game.downstairs.placementD)
        board.blit(game.enemy.image, game.enemy.guardian_tile())
        board.blit(game.tube.image, game.tube.plc)
        board.blit(game.needle.image, game.needle.plc)
        board.blit(game.ether.image, game.ether.plc)
        board.blit(game.syringe.image, game.syringe.plc)
        board.blit(game.hero.image, game.hero.plc)

        pg.display.flip()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                playable = False
                pg.quit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    move = game.hero.rect.x + game.hero.step
                    moveTuple = (move, game.hero.rect.y)
                    if moveTuple in game.floor.floor_tiles():
                        game.hero.move_right()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, event, playable)
                        game.win(board, event, playable)
                elif event.key == pg.K_LEFT:
                    move = game.hero.rect.x - game.hero.step
                    moveTuple = (move, game.hero.rect.y)
                    if moveTuple in game.floor.floor_tiles():
                        game.hero.move_left()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, event, playable)
                        game.win(board, event, playable)
                elif event.key == pg.K_UP:
                    move = game.hero.rect.y - game.hero.step
                    moveTuple = (game.hero.rect.x, move)
                    if moveTuple in game.floor.floor_tiles():
                        game.hero.move_up()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, event, playable)
                        game.win(board, event, playable)
                elif event.key == pg.K_DOWN:
                    move = game.hero.rect.y + game.hero.step
                    moveTuple = (game.hero.rect.x, move)
                    if moveTuple in game.floor.floor_tiles():
                        game.hero.move_down()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, event, playable)
                        game.win(board, event, playable)
                else:
                    pass


if __name__ == "__main__":
    main()
