def letter_to_sprite(letterList, letterPick):

    sprSize = 40
    maze = open('maze.txt', 'r')
    if type(letterPick) == str:
        for y, line in enumerate(maze):
            y = y * sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == letterPick:
                    x = x * sprSize
                    letterList.append((x, y))
                else:
                    pass
    return letterList


def list_to_sprite(letterList, letterPick):
    maze = open('maze.txt', 'r')
    for i in range(0, len(letterPick)):
        print(i)
        for y, line in enumerate(maze):
            print(line)
            y = y * 40
            for x, letter in enumerate(line):
                print(letter)
                if x == 15:
                    continue
                else:
                    if letter == letterPick[i]:
                        x = x * 40
                        letterList.append((x, y))
    return letterList


class Maze():

    def __init__(self, letter):

        self.plcList = []
        self.plc = letter_to_sprite(self.plcList, letter)
