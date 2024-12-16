class Reindeer:
    def __init__(self, xpos, ypos, dire, score, prev):
        self.xpos = xpos
        self.ypos = ypos
        self.dire = dire
        self.score = score
        self.prev = prev


with open('16.txt') as j:
    data = [i for i in j.read().strip().split("\n")]
grid, minscores =[],[]
for line in data:
    curr,curr1 = [],[]
    for cell in line:
        curr.append(cell)
        curr1.append([999999999999999,999999999999999,999999999999999,999999999999999])
    grid.append(curr)
    minscores.append(curr1)

#NSWE

def move(reind,place):
    #up
    if grid[reind.ypos-1][reind.xpos] != '#' and reind.dire != 'S':
        if reind.dire == 'N':
            if reind.score+1 <= minscores[reind.ypos-1][reind.xpos][0]:
                newRein.append(Reindeer(reind.xpos, reind.ypos-1, 'N', reind.score +1,place))
                minscores[reind.ypos-1][reind.xpos][0] = reind.score +1
        else:
            if reind.score+1001 <= minscores[reind.ypos-1][reind.xpos][0]:
                newRein.append(Reindeer(reind.xpos, reind.ypos-1, 'N', reind.score +1001,place))
                minscores[reind.ypos-1][reind.xpos][0] = reind.score +1001
    #down
    if grid[reind.ypos+1][reind.xpos] != '#' and reind.dire != 'N':
        if reind.dire == 'S':
            if reind.score+1 <= minscores[reind.ypos+1][reind.xpos][1]:
                newRein.append(Reindeer(reind.xpos, reind.ypos+1, 'S', reind.score +1,place))
                minscores[reind.ypos+1][reind.xpos][1] = reind.score +1
        else:
            if reind.score+1001 <= minscores[reind.ypos+1][reind.xpos][1]:
                newRein.append(Reindeer(reind.xpos, reind.ypos+1, 'S', reind.score +1001,place))
                minscores[reind.ypos+1][reind.xpos][1] = reind.score +1001
    #left
    if grid[reind.ypos][reind.xpos-1] != '#' and reind.dire != 'E':
        if reind.dire == 'W':
            if reind.score+1 <= minscores[reind.ypos][reind.xpos-1][2]:
                newRein.append(Reindeer(reind.xpos-1, reind.ypos, 'W', reind.score +1,place))
                minscores[reind.ypos][reind.xpos-1][2] = reind.score +1
        else:
            if reind.score+1001 <= minscores[reind.ypos][reind.xpos-1][2]:
                newRein.append(Reindeer(reind.xpos-1, reind.ypos, 'W', reind.score +1001,place))
                minscores[reind.ypos][reind.xpos-1][2] = reind.score +1001
    #right
    if grid[reind.ypos][reind.xpos+1] != '#' and reind.dire != 'W':
        if reind.dire == 'E':
            if reind.score+1 <= minscores[reind.ypos][reind.xpos+1][3]:
                newRein.append(Reindeer(reind.xpos+1, reind.ypos, 'E', reind.score +1,place))
                minscores[reind.ypos][reind.xpos+1][3] = reind.score +1
        else:
            if reind.score+1001 <= minscores[reind.ypos][reind.xpos+1][3]:
                newRein.append(Reindeer(reind.xpos+1, reind.ypos, 'E', reind.score +1001,place))
                minscores[reind.ypos][reind.xpos+1][3] = reind.score +1001


for y in range(0,len(grid)):
    if 'S' in grid[y]:
        xpos, ypos = grid[y].index('S'), y
        rein = [Reindeer(xpos,ypos, 'E',0,[])]
for y in range(0,len(grid)):
    if 'E' in grid[y]:
        endx, endy = grid[y].index('E'), y
        grid[endy][endx]='.'

total = 9999999999999999
while len(rein) > 0:
    newRein =[]
    for instance in rein:
        move(instance,[])
    x =0
    while x < len(newRein):
        instance = newRein[x]
        if instance.xpos == endx and instance.ypos == endy:
            if instance.score < total:
                total = instance.score
            newRein.pop(x)
        else:
            x +=1
    rein=newRein
print('part 1:',total)
least = total


def counting(path):
    for item in path:
        if item not in bestSeats:
            bestSeats.append(item)

for y in range(0,len(grid)):
    if 'S' in grid[y]:
        xpos, ypos = grid[y].index('S'), y
        rein = [Reindeer(xpos,ypos, 'E',0,[])]

grid, minscores =[],[]
for line in data:
    curr,curr1 = [],[]
    for cell in line:
        curr.append(cell)
        curr1.append([999999999999999,999999999999999,999999999999999,999999999999999])
    grid.append(curr)
    minscores.append(curr1)

bestSeats =[]
while len(rein) > 0:
    newRein =[]
    for instance in rein:
        pre = instance.prev + [[instance.xpos,instance.ypos]]
        move(instance,pre)
    x =0
    while x < len(newRein):
        instance = newRein[x]
        if instance.xpos == endx and instance.ypos == endy:
            if instance.score == least:
                counting(instance.prev)
            newRein.pop(x)
        else:
            x +=1
    rein=newRein
print('part 2:',len(bestSeats)+1)

