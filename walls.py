class Walls():

    def __init__(self, image):

        self.image = image

    @staticmethod
    def wall_tiles():
        maze = open('maze.txt', 'r')
        floorCoordinatesList = []
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'W':
                    x = x * 40
                    floorCoordinatesList.append((x, y))
                else:
                    pass
        return floorCoordinatesList
