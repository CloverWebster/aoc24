class Regions:
    def __init__(Region, xpos, ypos):
        Region.xpos = xpos
        Region.ypos = ypos

with open('12.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

grid = []
for x in range(0,len(data)):
    curr = ['.','.']
    for y in range(0,len(data[x])):
        curr.append(data[x][y])
    curr.append('.')
    curr.append('.')
    grid.append(curr)
curr = []
for x in range(0,len(grid[0])):
    curr.append('.')
grid = [curr] + [curr] + grid + [curr] + [curr]

upEdge,downEdge = [],[]
leftEdge, rightEdge =[],[]

def contains(reg,array):
    for x in range(0,len(array)):
        curr = array[x]
        if curr.xpos == reg.xpos and curr.ypos == reg.ypos:
            return True
    return False



def move(region):
    #up
    if region.ypos > 0:   
        if grid[region.ypos-1][region.xpos] == grid[region.ypos][region.xpos]:
            newregion = Regions(region.xpos, region.ypos-1)
            if contains(newregion,regions) is False and contains(newregion,newRegions) is False:
                newRegions.append(newregion)
        else:
            if region.ypos-1 in upEdge:
                allX = upEdge.index(region.ypos-1)+1
                if region.xpos not in upEdge[allX]:
                    upEdge[allX].append(region.xpos)
            else:
                upEdge.append(region.ypos-1)
                upEdge.append([region.xpos])

    #down
    if region.ypos < len(grid)-1:   
        if grid[region.ypos+1][region.xpos] == grid[region.ypos][region.xpos]:
            newregion = Regions(region.xpos, region.ypos+1)
            if contains(newregion,regions) is False and contains(newregion,newRegions) is False:
                newRegions.append(newregion)
        else:
            if region.ypos+1 in downEdge:
                allX = downEdge.index(region.ypos+1)+1
                if region.xpos not in downEdge[allX]:
                    downEdge[allX].append(region.xpos)
            else:
                downEdge.append(region.ypos +1)
                downEdge.append([region.xpos])

    #left
    if region.xpos > 0:   
        if grid[region.ypos][region.xpos-1] == grid[region.ypos][region.xpos]:
            newregion = Regions(region.xpos-1, region.ypos)
            if contains(newregion,regions) is False and contains(newregion,newRegions) is False:
                newRegions.append(newregion)
        else:
            if region.xpos-1 in leftEdge:
                allY = leftEdge.index(region.xpos-1)+1
                if region.ypos not in leftEdge[allY]:
                    leftEdge[allY].append(region.ypos)
            else:
                leftEdge.append(region.xpos-1)
                leftEdge.append([region.ypos])

    #right
    if region.xpos < len(grid[0])-1:   
        if grid[region.ypos][region.xpos+1] == grid[region.ypos][region.xpos]:
            newregion = Regions(region.xpos+1, region.ypos)
            if contains(newregion,regions) is False and contains(newregion,newRegions) is False:
                newRegions.append(newregion)
        else:
            if region.xpos+1 in rightEdge:
                allY = rightEdge.index(region.xpos+1)+1
                if region.ypos not in rightEdge[allY]:
                    rightEdge[allY].append(region.ypos)
            else:
                rightEdge.append(region.xpos+1)
                rightEdge.append([region.ypos])

def surrounding(pos):
    count = 0
    if contains(pos,regions) is False:
        #N
        if contains(Regions(pos.xpos,pos.ypos-1),regions) is True:
            count +=1
        #E
        if contains(Regions(pos.xpos+1,pos.ypos),regions) is True:
            count +=1
        #S
        if contains(Regions(pos.xpos,pos.ypos+1),regions) is True:
            count +=1
        #W
        if contains(Regions(pos.xpos-1,pos.ypos),regions) is True:
            count +=1
    return count


def part1():
    global regions, newRegions
    visited = []
    price = 0
    for line in range(0,len(grid)):
        for column in range(0,len(grid[0])):
            cell = grid[line][column]
            if cell != '.' and contains(Regions(column,line),visited) is False:
                regions,newRegions = [Regions(column,line)], [1]
                while len(newRegions) > 0:
                    newRegions = []
                    for instance in regions:
                        move(instance)
                    if len(newRegions)>0:
                        visited += newRegions
                        regions += newRegions
                area = len(regions)
                perim = 0
                for y in range(1,len(grid)-1):
                    for x in range(1,len(grid[0])-1):
                        perim += surrounding(Regions(x,y))
                price += area *perim
    print('part 1:',price)
part1()


def peri(array):
    count = 0
    for x in range(1,len(array),2):
        coords = sorted(array[x])
        prev = -2
        for y in range(0,len(coords)):
            if coords[y] != prev + 1:
                count += 1
            prev = coords[y]
    return count


def part2():
    global regions, newRegions
    global upEdge, downEdge, leftEdge, rightEdge
    upEdge,downEdge = [],[]
    leftEdge, rightEdge =[],[]
    visited = []
    price = 0
    for line in range(0,len(grid)):
        for column in range(0,len(grid[0])):
            upEdge,downEdge = [],[]
            leftEdge, rightEdge =[],[]
            cell = grid[line][column]
            if cell != '.' and contains(Regions(column,line),visited) is False:
                regions,newRegions = [Regions(column,line)], [1]
                while len(newRegions) > 0:
                    newRegions = []
                    for instance in regions:
                        move(instance)
                    if len(newRegions)>0:
                        visited += newRegions
                        regions += newRegions
                area = len(regions)
                perim = peri(upEdge) + peri(downEdge)+ peri(leftEdge)+peri(rightEdge)
                price += area *perim
    print('part 2:',price)
part2()


