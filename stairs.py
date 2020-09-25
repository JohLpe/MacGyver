class Stairs():

    def __init__(self, image):

        maze = open('maze.txt', 'r')
        upstairsCoordinates = ()
        downstairsCoordinates = ()
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'U':
                    x = x * 40
                    coordinatesXU = x
                    coordinatesYU = y
                    upstairsCoordinates = (x, y)
                elif letter == 'D':
                    x = x * 40
                    coordinatesXD = x
                    coordinatesYD = y
                    downstairsCoordinates = (x, y)
                else:
                    pass

        self.image = image
        self.placementXU = coordinatesXU
        self.placementYU = coordinatesYU
        self.placementU = upstairsCoordinates
        self.placementXD = coordinatesXD
        self.placementYD = coordinatesYD
        self.placementD = downstairsCoordinates
