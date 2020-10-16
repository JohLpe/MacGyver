import random


def letter_to_sprite(letterPick):

    sprSize = 40
    maze = open('maze.txt', 'r')
    letterList = []
    if type(letterPick) == str:
        for y, line in enumerate(maze):
            y = y * sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == letterPick:
                    x = x * sprSize
                    letterList.append((x, y))
    elif type(letterPick) == list:
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                else:
                    for i in range(0, len(letterPick)):
                        if letter == letterPick[i]:
                            x = x * 40
                            letterList.append((x, y))
    return letterList


def item_placement():

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


def hero_placement():

    sprSize = 40
    maze = open('maze.txt', 'r')
    for y, line in enumerate(maze):
        y = y * sprSize
        for x, letter in enumerate(line):
            if x == 15:
                continue
            if letter == 'A':
                coordX = x * sprSize
                coordY = y * sprSize
                break
    return coordX, coordY


def guardian_nearby_tiles():

    nearbyTiles = []
    sprSize = 40
    maze = open('maze.txt', 'r')
    for y, line in enumerate(maze):
        y = y * sprSize
        for x, letter in enumerate(line):
            if x == 15:
                continue
            if letter != 'G':
                continue
            if letter == 'G':
                x = x * sprSize
                minX = x - sprSize
                maxX = x + (sprSize * 2)
                minY = y - sprSize
                maxY = y + (sprSize * 2)
                for y2 in range(minY, maxY, sprSize):
                    for x2 in range(minX, maxX, sprSize):
                        nearbyTiles.append((x2, y2))
    return nearbyTiles
