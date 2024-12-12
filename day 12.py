class Regions:
    def __init__(Region, xpos, ypos):
        Region.xpos = xpos
        Region.ypos = ypos

'''
for u in grid:
    print(u)
'''

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

    #down
    if region.ypos < len(grid)-1:   
        if grid[region.ypos+1][region.xpos] == grid[region.ypos][region.xpos]:
            newregion = Regions(region.xpos, region.ypos+1)
            if contains(newregion,regions) is False and contains(newregion,newRegions) is False:
                newRegions.append(newregion)

    #left
    if region.xpos > 0:   
        if grid[region.ypos][region.xpos-1] == grid[region.ypos][region.xpos]:
            newregion = Regions(region.xpos-1, region.ypos)
            if contains(newregion,regions) is False and contains(newregion,newRegions) is False:
                newRegions.append(newregion)

    #right
    if region.xpos < len(grid[0])-1:   
        if grid[region.ypos][region.xpos+1] == grid[region.ypos][region.xpos]:
            newregion = Regions(region.xpos+1, region.ypos)
            if contains(newregion,regions) is False and contains(newregion,newRegions) is False:
                newRegions.append(newregion)

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
        if contains(Regions(pos.xpos+1,pos.ypos),regions) is True:
            count +=1
            '''
        #NW
        if contains(Regions(pos.xpos-1,pos.ypos-1),regions) is True:
            return True
        #NE
        if contains(Regions(pos.xpos+1,pos.ypos-1),regions) is True:
            return True
        #SE
        if contains(Regions(pos.xpos+1,pos.ypos+1),regions) is True:
            return True
        #SW
        if contains(Regions(pos.xpos-1,pos.ypos+1),regions) is True:
            return True
        '''
    return count



visited = []
price = 0
for line in range(0,len(grid)):
    print(line,'/', len(grid))
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
print(price)