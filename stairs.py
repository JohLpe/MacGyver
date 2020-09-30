class Stairs():

    def __init__(self, image):

        maze = open('maze.txt', 'r')
        upstairsCoords = ()
        downstairsCoords = ()
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'U':
                    x = x * 40
                    coordXU = x
                    coordYU = y
                    upstairsCoords = (x, y)
                elif letter == 'D':
                    x = x * 40
                    coordXD = x
                    coordYD = y
                    downstairsCoords = (x, y)
                else:
                    pass

        self.image = image
        self.plcXU = coordXU
        self.pcYU = coordYU
        self.plcU = upstairsCoords
        self.plcXD = coordXD
        self.plcYD = coordYD
        self.plcD = downstairsCoords
