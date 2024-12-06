with open('6.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

for x in range(0,len(data)):
    data[x] = list(data[x])

def start():
    for line in range(0,len(data)):
        for cell in range(0,line):
            if data[line][cell] == '^':
                data[line][cell] = 'X'
                return cell, line, 'N'

def moveUp(xpo,ypo):
    global total, data
    if ypo > 0:
        if data[ypo-1][xpo] != '#':
            ypo = ypo - 1
            if data[ypo][xpo] != 'X':
                total += 1
                data[ypo][xpo] = 'X'
            return xpo, ypo, 'N'
        else:
            return xpo,ypo, 'E'
    return xpo, ypo, 'end'

def moveRight(xpo,ypo):
    global total
    if xpo < len(data[0])-1 :
        if data[ypo][xpo+1] != '#':
            xpo += 1
            if data[ypo][xpo] != 'X':
                total += 1
                data[ypo][xpo] = 'X'
            return xpo, ypo, 'E'
        else:
            return xpo,ypo, 'S'
    return xpo, ypo, 'end'

def moveDown(xpo,ypo):
    global total
    if ypo < len(data)-1:
        if data[ypo + 1][xpo] != '#':
            ypo = ypo + 1
            if data[ypo][xpo] != 'X':
                total += 1
                data[ypo][xpo] = 'X'
            return xpo, ypo, 'S'
        else:
            return xpo,ypo, 'W'
    return xpo, ypo, 'end'

def moveLeft(xpo,ypo):
    global total
    if xpo > 0:
        if data[ypo][xpo-1] != '#':
            xpo = xpo - 1
            if data[ypo][xpo] != 'X':
                total += 1
                data[ypo][xpo] = 'X'
            return xpo, ypo, 'W'
        else:
            return xpo,ypo, 'N'
    return xpo, ypo, 'end'
            
total = 1
xposition, yposition, direction = start()
def move(xpos, ypos, dire):
    global total
    count = 0
    while dire != 'end':
        if dire == 'N':
            xpos, ypos, dire = moveUp(xpos,ypos)
        elif dire == 'E':
            xpos, ypos, dire = moveRight(xpos,ypos)
        elif dire == 'S':
            xpos, ypos, dire = moveDown(xpos,ypos)
        elif dire == 'W':
            xpos, ypos, dire = moveLeft(xpos,ypos)
        count +=1
        if count > 7500:
            return False
    return True
hi = move(xposition, yposition, direction)
print('part 1:',total)

total2 = 0
for line in range(0,len(data)):
    for cell in range(0,len(data[0])):
        if line != yposition or cell != xposition:
            if data[line][cell] == 'X':
                data[line][cell] = '#'
                if move(xposition, yposition, direction) == False:
                    total2 += 1
                data[line][cell] = 'X'
print('part 2:',total2)

                
