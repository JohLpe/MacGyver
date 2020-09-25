import pygame
from game import Game

pygame.init()


def main():

    pygame.display.set_caption("MacGyver Escape")
    board = pygame.display.set_mode((600, 600))

    background = pygame.image.load('ressource/void.png')
    inventory = pygame.image.load('ressource/inventory.png')
    pygame.mixer.music.load('ressource/bgst.mp3')
    pygame.mixer.music.play()

    game = Game()
    game.verifyItemsPlacement()

    playable = True

    while playable:
        """loop to make the game work"""

        board.blit(background, (0, 0))
        for coordinates in game.walls.placement:
            board.blit(game.walls.image, coordinates)
        for coordinates in game.floor.placement:
            board.blit(game.floor.image, coordinates)
        board.blit(inventory, (210, 562))
        board.blit(game.upstairs.image, game.upstairs.placementU)
        board.blit(game.downstairs.image, game.downstairs.placementD)
        board.blit(game.enemy.image, game.enemy.placement)
        board.blit(game.tube.image, game.tube.placement)
        board.blit(game.needle.image, game.needle.placement)
        board.blit(game.ether.image, game.ether.placement)
        board.blit(game.syringe.image, game.syringe.placement)
        board.blit(game.hero.image, game.hero.placement)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                playable = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move = game.hero.rect.x + game.hero.step
                    moveTuple = (move, game.hero.rect.y)
                    if moveTuple in game.floor.placement:
                        game.hero.move_right()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, playable)
                        game.win(board, playable)
                elif event.key == pygame.K_LEFT:
                    move = game.hero.rect.x - game.hero.step
                    moveTuple = (move, game.hero.rect.y)
                    if moveTuple in game.floor.placement:
                        game.hero.move_left()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, playable)
                        game.win(board, playable)
                elif event.key == pygame.K_UP:
                    move = game.hero.rect.y - game.hero.step
                    moveTuple = (game.hero.rect.x, move)
                    if moveTuple in game.floor.placement:
                        game.hero.move_up()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, playable)
                        game.win(board, playable)
                elif event.key == pygame.K_DOWN:
                    move = game.hero.rect.y + game.hero.step
                    moveTuple = (game.hero.rect.x, move)
                    if moveTuple in game.floor.placement:
                        game.hero.move_down()
                        game.grabItem()
                        game.makeSyringe()
                        game.stab(board, playable)
                        game.win(board, playable)
                else:
                    pass


if __name__ == "__main__":
    main()
