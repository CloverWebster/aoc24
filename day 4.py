with open('4.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

def search(row,chara,letter, dire):
    global total
    global array

    if letter == '.':
        total += 1
    else:
        if row > 0:
            if chara > 0:
                if data[row-1][chara-1] == letter and (dire == 'NW' or dire == 'any'):
                    array.append([row-1,chara-1,xmas[xmas.index(letter) + 1], 'NW'])
            if data[row-1][chara] == letter and (dire == 'N' or dire == 'any'):
                array.append([row-1,chara,xmas[xmas.index(letter) + 1],'N'])
            if chara < len(data[0]) - 1:
                if data[row-1][chara+1] == letter and (dire == 'NE' or dire == 'any'):
                    array.append([row-1,chara+1,xmas[xmas.index(letter) + 1],'NE'])
        
        if chara > 0:
            if data[row][chara-1] == letter and (dire == 'W' or dire == 'any'):
                array.append([row,chara-1,xmas[xmas.index(letter) + 1],'W'])
        if chara < len(data[0]) - 1:
            if data[row][chara+1] == letter and (dire == 'E' or dire == 'any'):
                array.append([row,chara+1,xmas[xmas.index(letter) + 1],'E'])
            
        if row < len(data)-1:
            if chara > 0:
                if data[row+1][chara-1] == letter and (dire == 'SW' or dire == 'any'):
                    array.append([row+1,chara-1,xmas[xmas.index(letter) + 1],'SW'])
            if data[row+1][chara] == letter and (dire == 'S' or dire == 'any'):
                array.append([row+1,chara,xmas[xmas.index(letter) + 1],'S'])
            if chara < len(data[0]) - 1:
                if data[row+1][chara+1] == letter and (dire == 'SE' or dire == 'any'):
                    array.append([row+1,chara+1,xmas[xmas.index(letter) + 1],'SE'])
    
                    

def part1():
    global total
    total = 0
    global xmas
    xmas = ['X','M','A','S','.']
    global array
    array = []

    for x in range(0,len(data)):
        data[x] = list(data[x])


    for line in range(0,len(data)):
        for character in range(0,len(data[line])):
            if data[line][character] == 'X':
                search(line, character,'M','any')

    x = 0
    while len(array) > 0:
        search(array[0][0], array[0][1], array[0][2], array[0][3])
        array.remove(array[0])
    print(total)



def part2():
    global total
    total = 0
    global xmas
    xmas = ['X','M','A','S','.']
    global array
    array = []

    for x in range(0,len(data)):
        data[x] = list(data[x])


    for line in range(0,len(data)):
        for character in range(0,len(data[line])):
            if data[line][character] == 'A':
                if line > 0 and line < len(data)-1 and character > 0 and character < len(data[0]) -1:
                    if SE(line,character) == True:
                        if SW(line,character) == True or NE(line,character) == True:
                            total += 1
                    elif NW(line,character) == True:
                        if SW(line,character) == True or NE(line,character) == True:
                            total += 1
    print(total)


def SE(row, chara):
    if data[row-1][chara-1] == 'M':
        if data[row+1][chara+1] == 'S':
            return True
    return False

def SW(row, chara):
    if data[row-1][chara+1] == 'M':
        if data[row+1][chara-1] == 'S':
            return True
    return False

def NW(row, chara):
    if data[row+1][chara+1] == 'M':
        if data[row-1][chara-1] == 'S':
            return True
    return False

def NE(row, chara):
    if data[row+1][chara-1] == 'M':
        if data[row-1][chara+1] == 'S':
            return True
    return False

part1()
part2()