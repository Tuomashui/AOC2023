def OpenFile(filename):
    openedFile = open(filename, 'r', encoding="utf-8")
    numbernames = ['kakka','one','two','three', 'four','five','six','seven','eight','nine']
    FULL_LIST = []
    numberlist = []

    while True:
        lineChar = openedFile.readline()
        if (len(lineChar) == 0):
            break
        lines = lineChar [:-1]
        lines = lines.split()
        onewholeLine = lines[0]
        x = 0
        i = 0
        print(onewholeLine)
        for i in range(0, len(onewholeLine)+5):
            if (i < 5):
                x = 0
            else:
                x = i-5
            if (i < len(onewholeLine)):
                oneLine = onewholeLine[x:i+1]
            else:
                oneLine = onewholeLine[x:len(onewholeLine)]
                x = x + 1
                print(oneLine)
            for a in range(1,10):
                if (str(a) in oneLine):
                    numberlist.append(str(a))
                if (str(numbernames[a]) in oneLine):
                    numberlist.append(str(a))
        if (len(numberlist) == 0):
            print("ei mitään")
        else:
            FULL_LIST.append(int(str(numberlist[0])+str(numberlist[-1])))
        numberlist.clear()
    openedFile.close()
    numberlistsum = sum(FULL_LIST)
    return numberlistsum
def main():
    filename = input("Open file: ")
    sum = OpenFile(filename)
    print("vastaus on: " +  str(sum) )


main()