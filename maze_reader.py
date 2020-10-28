import random


def letter_to_sprite(letter_pick):
    """Returns list of coordinates for 1 or a list of character(s)."""

    spr_size = 40
    maze = open('maze.txt', 'r')
    letter_list = []
    if type(letter_pick) == str:
        for y, line in enumerate(maze):
            y = y * spr_size
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == letter_pick:
                    x = x * spr_size
                    letter_list.append((x, y))
    elif type(letter_pick) == list:
        for y, line in enumerate(maze):
            y = y * spr_size
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                else:
                    for i in range(0, len(letter_pick)):
                        if letter == letter_pick[i]:
                            x = x * spr_size
                            letter_list.append((x, y))
    return letter_list


def item_placement():
    """Returns a random tuple of coordinates for items."""

    spr_size = 40
    maze = open('maze.txt', 'r')
    removal_list = []
    accessible_tiles = []
    for y, line in enumerate(maze):
        y = y * spr_size
        for x, letter in enumerate(line):
            if x == 15:
                continue
            elif letter == 'F':
                x = x * spr_size
                accessible_tiles.append((x, y))
            elif letter == 'G':
                x = x * spr_size
                min_x = x - spr_size
                max_x = x + (spr_size * 2)
                min_y = y - spr_size
                max_y = y + (spr_size * 2)
                for y2 in range(min_y, max_y, spr_size):
                    for x2 in range(min_x, max_x, spr_size):
                        removal_list.append((x2, y2))
    for coordinates in removal_list:
        if coordinates in accessible_tiles:
            accessible_tiles.remove(coordinates)
    i = random.randrange(0, len(accessible_tiles))
    plc = accessible_tiles[i]
    return plc


def hero_placement():
    """returns player's axis X and axis Y coordinates."""

    spr_size = 40
    maze = open('maze.txt', 'r')
    for y, line in enumerate(maze):
        y = y * spr_size
        for x, letter in enumerate(line):
            if x == 15:
                continue
            if letter == 'A':
                coord_x = x * spr_size
                coord_y = y
                break
    return coord_x, coord_y


def guardian_nearby_tiles():
    """returns list of coordinates around the ennemy."""

    nearby_tiles = []
    spr_size = 40
    maze = open('maze.txt', 'r')
    for y, line in enumerate(maze):
        y = y * spr_size
        for x, letter in enumerate(line):
            if x == 15:
                continue
            if letter != 'G':
                continue
            if letter == 'G':
                x = x * spr_size
                min_x = x - spr_size
                max_x = x + (spr_size * 2)
                min_y = y - spr_size
                max_y = y + (spr_size * 2)
                for y2 in range(min_y, max_y, spr_size):
                    for x2 in range(min_x, max_x, spr_size):
                        nearby_tiles.append((x2, y2))
    return nearby_tiles
