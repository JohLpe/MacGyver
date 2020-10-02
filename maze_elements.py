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


class Maze():
    "class defining the collectable items from the game"

    def __init__(self, image):

        self.sprSize = 40
        self.image = image
        self.plcList = []
        self.plcTuple = placement_items()

    def letter_to_sprite(self, letterList, letterPick):

        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == letterPick:
                    x = x * self.sprSize
                    letterList.append((x, y))
                else:
                    pass
        return letterList

    def is_floor(self):
        self.letter_to_sprite(self.plcList, 'F')
        self.letter_to_sprite(self.plcList, 'A')
        self.letter_to_sprite(self.plcList, 'G')
        self.letter_to_sprite(self.plcList, 'U')
        self.letter_to_sprite(self.plcList, 'D')
        return self.plcList

    def is_wall(self):
        self.letter_to_sprite(self.plcList, 'W')
        return self.plcList

    def is_inventory(self):
        self.letter_to_sprite(self.plcList, 'I')
        return self.plcList

    def is_upstairs(self):
        self.letter_to_sprite(self.plcList, 'U')
        return self.plcList

    def is_downstairs(self):
        self.letter_to_sprite(self.plcList, 'D')
        return self.plcList
