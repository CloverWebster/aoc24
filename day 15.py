class Boxes:
    def __init__(self, xpos, ypos, symbol):
        self.xpos = xpos
        self.ypos = ypos
        self.symbol = symbol

with open('15.txt') as j:
    data = [i for i in j.read().strip().split("\n\n")]

data[0] = data[0].split('\n')
grid1, grid2=[],[]
for line in data[0]:
    curr,curr2 = [],[]
    for cell in line:
        curr.append(cell)
        if cell == 'O':
            curr2.append('[')
            curr2.append(']')
        elif cell =='.':
            curr2.append('.')
            curr2.append('.')
        elif cell =='#':
            curr2.append('#')
            curr2.append('#')
        else:
            curr2.append('@')
            curr2.append('.')
    grid1.append(curr)
    grid2.append(curr2)



data[1] = data[1].split('\n')
directions=[]
for line in data[1]:
    curr = []
    for cell in line:
        curr.append(cell)
    directions += curr

def moveUp1(x,y):
    first = y
    while grid1[first][x] == '@' or grid1[first][x] == 'O':
        first -= 1
    if grid1[first][x] != '#':
        grid1[first][x] = 'O'
        grid1[y][x] = '.'
        grid1[y-1][x] = '@'
        return x,y-1
    return x,y

def moveDown1(x,y):
    first = y
    while grid1[first][x] == '@' or grid1[first][x] == 'O':
        first += 1
    if grid1[first][x] != '#':
        grid1[first][x] = 'O'
        grid1[y][x] = '.'
        grid1[y+1][x] = '@'
        return x,y+1
    return x,y

def moveLeft1(x,y):
    first = x
    while grid1[y][first] == '@' or grid1[y][first] == 'O':
        first -= 1
    if grid1[y][first] != '#':
        grid1[y][first] = 'O'
        grid1[y][x] = '.'
        grid1[y][x-1] = '@'
        return x-1,y
    return x,y

def moveRight1(x,y):
    first = x
    while grid1[y][first] == '@' or grid1[y][first] == 'O':
        first += 1
    if grid1[y][first] != '#':
        grid1[y][first] = 'O'
        grid1[y][x] = '.'
        grid1[y][x+1] = '@'
        return x+1,y
    return x,y


def moveLeft2(x,y):
    first = x
    while grid2[y][first] == '@' or grid2[y][first] == '[' or grid2[y][first] == ']':
        first -= 1
    if grid2[y][first] != '#' and grid2[y][x-1] != '.':
        for place in range(first, x,2):
            grid2[y][place] = '['
            grid2[y][place +1] = ']'
        grid2[y][x-1] = '@'
        grid2[y][x] = '.'
        return x-1,y
    elif grid2[y][x-1] == '.':
        grid2[y][x-1] = '@'
        grid2[y][x] = '.'
        return x-1,y
    return x,y

def moveRight2(x,y):
    first = x
    while grid2[y][first] == '@' or grid2[y][first] == '[' or grid2[y][first] == ']':
        first += 1 
    if grid2[y][first] != '#' and grid2[y][x+1] != '.':
        for place in range(first, x,-2):
            grid2[y][place] = ']'
            grid2[y][place -1] = '['
        grid2[y][x+1] = '@'
        grid2[y][x] = '.'
        return x+1,y
    elif grid2[y][x+1] == '.':
        grid2[y][x+1] = '@'
        grid2[y][x] = '.'
        return x+1,y
    return x,y


def findPair(item):
    if item.symbol == '[':
        return Boxes(item.xpos+1, item.ypos, ']')
    else:
        return Boxes(item.xpos-1, item.ypos, '[')


def moveUp2(x,y):
    moveCheck = True
    check,toMove = [],[]
    d = Boxes(x, y-1, grid2[y-1][x])
    toMove+= [d] + [findPair(d)]
    check += [d] + [findPair(d)]
    while len(check) != 0 and moveCheck is True:
        for i in range(0,len(check)):
            above = Boxes(check[0].xpos,check[0].ypos -1, grid2[check[0].ypos -1][check[0].xpos])
            if above.symbol != '.' and above.symbol != '#':
                pair = findPair(above)
                toMove += [above,pair]
                check += [above,pair]
            elif above.symbol == '#':
                moveCheck = False
                break
            check.pop(0)
    if moveCheck is True:
        for i in range(len(toMove)-1,-1,-1):
            curr = toMove[i]
            grid2[curr.ypos-1][curr.xpos] = curr.symbol
            grid2[curr.ypos][curr.xpos] = '.'
        grid2[y-1][x] = '@'
        grid2[y][x] ='.'
        return x, y-1
    return x,y


def moveDown2(x,y):
    moveCheck = True
    check,toMove = [],[]
    d = Boxes(x, y+1, grid2[y+1][x])
    toMove+= [d] + [findPair(d)]
    check += [d] + [findPair(d)]
    while len(check) != 0 and moveCheck is True:
        for i in range(0,len(check)):
            above = Boxes(check[0].xpos,check[0].ypos +1, grid2[check[0].ypos +1][check[0].xpos])
            if above.symbol != '.' and above.symbol != '#':
                pair = findPair(above)
                toMove += [above,pair]
                check += [above,pair]
            elif above.symbol == '#':
                moveCheck = False
                break
            check.pop(0)
    if moveCheck is True:
        for i in range(len(toMove)-1,-1,-1):
            curr = toMove[i]
            grid2[curr.ypos+1][curr.xpos] = curr.symbol
            grid2[curr.ypos][curr.xpos] = '.'
        grid2[y+1][x] = '@'
        grid2[y][x] ='.'
        return x, y+1
    return x,y



for y in range(0,len(grid1)):
    if '@' in grid1[y]:
        xpos, ypos = grid1[y].index('@'), y

for inst in directions:
    if inst == '^':
        xpos,ypos = moveUp1(xpos,ypos)
    elif inst == 'v':
        xpos,ypos = moveDown1(xpos,ypos)
    elif inst == '<':
        xpos,ypos = moveLeft1(xpos,ypos)
    elif inst == '>':
        xpos,ypos = moveRight1(xpos,ypos)

total = 0
for line in range(0,len(grid1)):
    for cell in range(0,len(grid1[0])):
        if grid1[line][cell] == 'O':
            total += (line *100) + cell
print('part 1:',total)

for y in range(0,len(grid2)):
    if '@' in grid2[y]:
        xpos, ypos = grid2[y].index('@'), y

for inst in directions:
    if inst == '^':
        if grid2[ypos-1][xpos] =='[' or grid2[ypos-1][xpos] ==']':
            xpos,ypos = moveUp2(xpos,ypos)
        elif grid2[ypos-1][xpos] =='.':
            grid2[ypos-1][xpos] ='@'
            grid2[ypos][xpos] ='.'
            ypos -= 1
    elif inst == 'v':
        if grid2[ypos+1][xpos] =='[' or grid2[ypos+1][xpos] ==']':
            xpos,ypos = moveDown2(xpos,ypos)
        elif grid2[ypos+1][xpos] =='.':
            grid2[ypos+1][xpos] ='@'
            grid2[ypos][xpos] ='.'
            ypos += 1
    elif inst == '<':
        xpos,ypos = moveLeft2(xpos,ypos)
    elif inst == '>':
        xpos,ypos = moveRight2(xpos,ypos)

total = 0
for line in range(0,len(grid2)):
    for cell in range(0,len(grid2[0])):
        if grid2[line][cell] == '[':
            total += (line *100) + cell
print('part 2:',total)