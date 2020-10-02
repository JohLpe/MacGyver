import random


class Items:
    "class defining the collectable items from the game"

    def __init__(self, image):

        self.sprSize = 40
        self.image = image
        maze = open('maze.txt', 'r')
        removalList = []
        accessibleTiles = []
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == 'F':
                    x = x * self.sprSize
                    accessibleTiles.append((x, y))
                elif letter == 'G':
                    x = x * self.sprSize
                    minX = x - self.sprSize
                    maxX = x + (self.sprSize * 2)
                    minY = y - self.sprSize
                    maxY = y + (self.sprSize * 2)
                    for y2 in range(minY, maxY, self.sprSize):
                        for x2 in range(minX, maxX, self.sprSize):
                            removalList.append((x2, y2))
        for coordinates in removalList:
            if coordinates in accessibleTiles:
                accessibleTiles.remove(coordinates)
        i = random.randrange(0, len(accessibleTiles))
        self.plc = accessibleTiles[i]
