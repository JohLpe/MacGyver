import random


def placement_items():
    sprSize = 40
    maze = open('maze.txt', 'r')
    removalList = []
    accessibleTiles = []
    for y, line in enumerate(maze):
        y = y * sprSize
        for x, letter in enumerate(line):
            if x == 15:
                continue
            elif letter == 'F':
                x = x * sprSize
                accessibleTiles.append((x, y))
            elif letter == 'G':
                x = x * sprSize
                minX = x - sprSize
                maxX = x + (sprSize * 2)
                minY = y - sprSize
                maxY = y + (sprSize * 2)
                for y2 in range(minY, maxY, sprSize):
                    for x2 in range(minX, maxX, sprSize):
                        removalList.append((x2, y2))
    for coordinates in removalList:
        if coordinates in accessibleTiles:
            accessibleTiles.remove(coordinates)
    i = random.randrange(0, len(accessibleTiles))
    plc = accessibleTiles[i]
    return plc


class Item():

    def __init__(self, image):

        self.image = image
        self.plc = placement_items()

    # def verifyItemsPlacement(self):

    #     itemsPlcList = [self.tube.plcTuple,
    #                     self.needle.plcTuple, self.ether.plcTuple]
    #     itemsPlcList = list(set(itemsPlcList))
    #     if len(itemsPlcList) != 3:
    #         while len(itemsPlcList) != 3:
    #             del itemsPlcList
    #             self.tube = Maze(pg.image.load('ressource/tube.png'))
    #             self.needle = Maze(pg.image.load('ressource/needle.png'))
    #             self.ether = Maze(pg.image.load('ressource/ether.png'))
    #             itemsPlcList = [self.tube.plcTuple,
    #                             self.needle.plcTuple, self.ether.plcTuple]
    #             itemsPlcList = list(set(itemsPlcList))
    #     elif len(itemsPlcList) == 3:
    #         pass
