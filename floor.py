class Floor():

    def __init__(self, image):

        self.image = image

    @staticmethod
    def floor_tiles():

        maze = open('maze.txt', 'r')
        floorCoordinatesList = []
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == 'F':
                    x = x * 40
                    floorCoordinatesList.append((x, y))
                elif letter == 'A':
                    x = x * 40
                    floorCoordinatesList.append((x, y))
                elif letter == 'G':
                    x = x * 40
                    floorCoordinatesList.append((x, y))
                elif letter == 'U':
                    x = x * 40
                    floorCoordinatesList.append((x, y))
                elif letter == 'D':
                    x = x * 40
                    floorCoordinatesList.append((x, y))
                else:
                    pass
        return floorCoordinatesList
