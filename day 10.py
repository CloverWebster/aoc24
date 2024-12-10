class Hikes:
    def __init__(Hike, xpos, ypos):
        Hike.xpos = xpos
        Hike.ypos = ypos

def move(hike):
    #up
    if hike.ypos > 0:   
        if grid[hike.ypos-1][hike.xpos] == grid[hike.ypos][hike.xpos] + 1:
            newhike = Hikes(hike.xpos, hike.ypos-1)
            newHikes.append(newhike)

    #down
    if hike.ypos < len(grid)-1:   
        if grid[hike.ypos+1][hike.xpos] == grid[hike.ypos][hike.xpos] + 1:
            newhike = Hikes(hike.xpos, hike.ypos+1)
            newHikes.append(newhike)

    #left
    if hike.xpos > 0:   
        if grid[hike.ypos][hike.xpos-1] == grid[hike.ypos][hike.xpos] + 1:
            newhike = Hikes(hike.xpos-1, hike.ypos)
            newHikes.append(newhike)

    #right
    if hike.xpos < len(grid[0])-1:   
        if grid[hike.ypos][hike.xpos+1] == grid[hike.ypos][hike.xpos] + 1:
            newhike = Hikes(hike.xpos+1, hike.ypos)
            newHikes.append(newhike)


def prune(hikeList):
    newHikeList = []
    for x in range(0,len(hikeList)):
        currHike = hikeList[x]
        add=True
        for y in range(0,len(newHikeList)):
            check = newHikeList[y]
            if currHike.xpos == check.xpos and currHike.ypos == check.ypos:
                add=False
                break
        if add is True:
            newHikeList.append(currHike)
    return newHikeList


with open('10.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

grid = []
for x in range(0,len(data)):
    curr = []
    for y in range(0,len(data[x])):
        curr.append(int(data[x][y]))
    grid.append(curr)

def part1():
    total =0
    global newHikes
    trailheads = []
    for line in range(0,len(grid)):
        for cell in range(0,len(grid[0])):
            if grid[line][cell] == 0:
                trailheads.append(Hikes(cell,line))

    for i in range(0,len(trailheads)):
        hikes = [trailheads[i]]
        count=0
        while len(hikes) > 0:
            newHikes=[]
            for instance in hikes:
                move(instance)
            count += 1
            newHikes = prune(newHikes)
            if count == 9:
                total += len(newHikes)
                break
            hikes = newHikes
    print('part 1:',total)


def part2():
    total =0
    global newHikes
    trailheads = []
    for line in range(0,len(grid)):
        for cell in range(0,len(grid[0])):
            if grid[line][cell] == 0:
                trailheads.append(Hikes(cell,line))

    for i in range(0,len(trailheads)):
        hikes = [trailheads[i]]
        count=0
        while len(hikes) > 0:
            newHikes=[]
            for instance in hikes:
                move(instance)
            count += 1
            if count == 9:
                total += len(newHikes)
                break
            hikes = newHikes
    print('part 2:',total)

part1()
part2()
