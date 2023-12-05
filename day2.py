def OpenFile(filename):
    openedFile = open(filename, 'r', encoding="utf-8")
    return openedFile


def Calculations(opened_file):
    GameIndex = []
    Game_min_colors = []
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

        # Multiply all minimum amounts of colors then sum games together
        Game_index = oneLine[0].split()

        valid_game = True
        max_colours = {'blue': 14, 'red': 12, 'green': 13} 
        min_colours = {'blue': 0, 'red': 0, 'green': 0}

        # check if game is valid and change the minimum color amounts
        for sublist in gameColours:
            for item in sublist:
                quantity, color = item
                quantity = int(quantity)
                max_quantity = max_colours.get(color.lower(), None)
                if quantity > min_colours[color]:# 2 STAR CODE
                    min_colours[color] = quantity# 2 STAR CODE
                if max_quantity is None: 
                     valid_game = False 
                if quantity > max_quantity:
                    valid_game = False
        # multiply all game colors together and add to the list
        # 2 STAR CODE
        multiply_colors = 1
        for color_amount in min_colours.values():
                multiply_colors *= int(color_amount)

        Game_min_colors.append(multiply_colors) # 2 STAR CODE
        if valid_game: # FIRST STAR CODE
            GameIndex.append(int(Game_index[1]))

    print(Game_min_colors)
    indexSum = sum(GameIndex)
    gameMinSum = sum(Game_min_colors)
    return indexSum, gameMinSum
    

def main():
    filename = input("Open file: ")
    opened_file = OpenFile(filename)
    sum, minsum = Calculations(opened_file)
    print("IndexSum: " + str(sum))
    print("MinSum: " + str(minsum))
main()