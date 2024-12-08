with open('8.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

for x in range(0,len(data)):
    data[x] = list(data[x])

def createGrid():
    global grid
    grid = []
    for x in range(0,len(data)):
        curr=[]
        for y in data[x]:
            curr.append('.')
        grid.append(curr)
createGrid()

def findPair(lett):
    array = []
    for row in range(0,len(data)):
        for column in range(0,len(data[0])):
            if data[row][column]==lett:
                array.append([column,row])
    return(array)
def part1():
    for line in range(0,len(data)):
        for cell in range(0,len(data[0])):
            if data[line][cell] != '.':
                pairs = findPair(data[line][cell])
                for x in range(0,len(pairs)):
                    pairX,pairY = pairs[x][0],pairs[x][1]
                    if pairX != cell and pairY != line:
                        antiX = cell + (2*(pairX - cell))
                        antiY = line + (2*(pairY - line))
                        if 0 <= antiX < len(data[0]) and 0<= antiY < len(data):
                            grid[antiY][antiX] = '#'
    count = 0
    for line in range(0,len(grid)):
        for cell in range(0,len(grid[0])):
            if grid[line][cell] == '#':
                count+=1
    print('part 1:',count)


def part2():
    for line in range(0,len(data)):
        for cell in range(0,len(data[0])):
            if data[line][cell] != '.':
                grid[line][cell] = '#'
                pairs = findPair(data[line][cell])
                for x in range(0,len(pairs)):
                    pairX,pairY = pairs[x][0],pairs[x][1]
                    if pairX != cell and pairY != line:
                        antiX = cell + (2*(pairX - cell))
                        antiY = line + (2*(pairY - line))
                        while 0 <= antiX < len(data[0]) and 0<= antiY < len(data):
                            grid[antiY][antiX] = '#'
                            firstX,firstY = pairX, pairY
                            pairX,pairY = antiX,antiY
                            antiX = firstX + (2*(pairX - firstX))
                            antiY = firstY + (2*(pairY - firstY))

    count = 0
    for line in range(0,len(grid)):
        for cell in range(0,len(grid[0])):
            if grid[line][cell] == '#':
                count+=1
    print('part 2:',count)
part1()
part2()