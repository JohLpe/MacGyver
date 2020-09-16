import pygame
from game import Game

pygame.init()

pygame.display.set_caption("MacGyver Escape")
board = pygame.display.set_mode((600, 600))

background = pygame.image.load('ressource/background.png')
inventory = pygame.image.load('ressource/inventory.png')
pygame.mixer.music.load('ressource/bgst.mp3')
pygame.mixer.music.play()

game = Game()

playable = True

while playable:
    """loop to make the game work"""

    board.blit(background, (0, 0))
    board.blit(inventory, (230, 562))
    board.blit(game.enemy.image, game.enemy.rect)
    board.blit(game.tube.image, game.tube.placement)
    board.blit(game.needle.image, game.needle.placement)
    board.blit(game.ether.image, game.ether.placement)
    board.blit(game.syringe.image, game.syringe.placement)
    board.blit(game.hero.image, game.hero.rect)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playable = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move = game.hero.rect.x + game.hero.step
                moveTuple = (move, game.hero.rect.y)
                if moveTuple in game.floor.defineFloorTiles():
                    game.hero.move_right()
                    game.grabItem()
                    game.makeSyringe()
                    game.stab(board, playable)
                    game.win(board, playable)
            elif event.key == pygame.K_LEFT:
                move = game.hero.rect.x - game.hero.step
                moveTuple = (move, game.hero.rect.y)
                if moveTuple in game.floor.defineFloorTiles():
                    game.hero.move_left()
                    game.grabItem()
                    game.makeSyringe()
            elif event.key == pygame.K_UP:
                move = game.hero.rect.y - game.hero.step
                moveTuple = (game.hero.rect.x, move)
                if moveTuple in game.floor.defineFloorTiles():
                    game.hero.move_up()
                    game.grabItem()
                    game.makeSyringe()
                    game.stab(board, playable)
            elif event.key == pygame.K_DOWN:
                move = game.hero.rect.y + game.hero.step
                moveTuple = (game.hero.rect.x, move)
                if moveTuple in game.floor.defineFloorTiles():
                    game.hero.move_down()
                    game.grabItem()
                    game.makeSyringe()
            else:
                pass
