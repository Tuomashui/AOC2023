def OpenFile(filename):
    openedFile = open(filename, 'r', encoding="utf-8")
    return openedFile


def Calculations(opened_file):
    GameIndex = []
    while True:
        oneLine = opened_file.readline()
        if (len(oneLine) == 0):
            break
        oneLine = oneLine[:-1]
        oneLine = oneLine.split(':')
        gameRound = oneLine[1].split(';')

        gameColours = []

        for item in gameRound:
            parts = item.split(', ')
            cubes = [element.strip().split() for element in parts]
            gameColours.append(cubes)
            
        ## 12 red cubes, 13 green cubes, and 14 blue cubes
        max_colours = {'blue': 14, 'red': 12, 'green': 13}

        Game_index = oneLine[0].split()

        print(GameIndex)

        valid_game = True

        for sublist in gameColours:
            for item in sublist:
                quantity, color = item
                max_quantity = max_colours.get(color.lower(), None) 
                if max_quantity is None:
                    valid_game = False
                if int(quantity) > max_quantity:
                    valid_game = False
        if valid_game:
            GameIndex.append(int(Game_index[1]))
    indexSum = sum(GameIndex)
    return indexSum
    

def main():
    filename = input("Open file: ")
    opened_file = OpenFile(filename)
    sum = Calculations(opened_file)
    print("IndexSum: " + str(sum))
main()