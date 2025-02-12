class Reindeer:
    def __init__(self, xpos, ypos, dire, score, skip, actSkip, start, end):
        self.xpos = xpos
        self.ypos = ypos
        self.dire = dire
        self.score = score
        self.skip = skip
        self.actSkip = actSkip
        self.start =start
        self.end = end

cs =72
cs1 = cs + 1

with open('20.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

add = ['#','#']
oneAdd = 9999
add1 = [oneAdd, oneAdd]
for cell in data[0]:
    add.append('#')
    add1.append(oneAdd)
grid, minscores =[add],[add1]
for line in data:
    curr,curr1 = ['#'],[oneAdd]
    for cell in line:
        curr.append(cell)
        curr1.append(oneAdd)
    curr.append('#')
    curr1.append(oneAdd)
    grid.append(curr)
    minscores.append(curr1)
grid.append(add)
minscores.append(add1)

def printing():
    for line in grid:
        curr = ''
        for cell in line:
            curr+= cell
        print(curr)

printing()

def move(reind):
    global minscores
    #up
    if grid[reind.ypos-1][reind.xpos] != '#' and reind.dire != 'S':
        if reind.score+1 <= minscores[reind.ypos-1][reind.xpos]:
            newRein.append(Reindeer(reind.xpos, reind.ypos-1, 'N', reind.score +1,reind.skip, False,'0,0','0,0'))
    #down
    if grid[reind.ypos+1][reind.xpos] != '#' and reind.dire != 'N':
        if reind.score+1 <= minscores[reind.ypos+1][reind.xpos]:
            newRein.append(Reindeer(reind.xpos, reind.ypos+1, 'S', reind.score +1,reind.skip, False,'0,0','0,0'))
    #left
    if grid[reind.ypos][reind.xpos-1] != '#' and reind.dire != 'E':
        if reind.score+1 <= minscores[reind.ypos][reind.xpos-1]:
            newRein.append(Reindeer(reind.xpos-1, reind.ypos, 'W', reind.score +1,reind.skip, False,'0,0','0,0'))
    #right
    if grid[reind.ypos][reind.xpos+1] != '#' and reind.dire != 'W':
        if reind.score+1 <= minscores[reind.ypos][reind.xpos+1]:
            newRein.append(Reindeer(reind.xpos+1, reind.ypos, 'E', reind.score +1,reind.skip, False,'0,0','0,0'))
    '''
    if first is True and reind.score < 10:
        for line in minscores:
            curr = ''
            for cell in line:
                curr += str(cell[0]) +' '
            print(curr)
        print('\n')
    '''
    
    

    if reind.skip is False and first is False:
        #up
        if grid[reind.ypos-2][reind.xpos] != '#' and reind.dire != 'S':
            if reind.score+cs1 <= minscores[reind.ypos-2][reind.xpos]:
                newRein.append(Reindeer(reind.xpos, reind.ypos-2, 'N', reind.score +2,True, False,'0,0','0,0'))
        #down
        if grid[reind.ypos+2][reind.xpos] != '#' and reind.dire != 'N':
            if reind.score+cs1 <= minscores[reind.ypos+2][reind.xpos]:
                newRein.append(Reindeer(reind.xpos, reind.ypos+2, 'S', reind.score +2,True, False,'0,0','0,0'))
        #left
        if grid[reind.ypos][reind.xpos-2] != '#' and reind.dire != 'E':
            if reind.score+cs1 <= minscores[reind.ypos][reind.xpos-2]:
                newRein.append(Reindeer(reind.xpos-2, reind.ypos, 'W', reind.score +2,True, False,'0,0','0,0'))
        #right
        if grid[reind.ypos][reind.xpos+2] != '#' and reind.dire != 'W':
            if reind.score+cs1 <= minscores[reind.ypos][reind.xpos+2]:
                newRein.append(Reindeer(reind.xpos+2, reind.ypos, 'E', reind.score +2,True, False,'0,0','0,0'))


def firstR():
    global first, newRein, bascTotal, rein
    first = True
    while len(rein) > 0:
        newRein =[]
        for instance in rein:
            move(instance)
        for instance in newRein:
            minscores[instance.ypos][instance.xpos] = instance.score
        x =0
        while x < len(newRein):
            instance = newRein[x]
            if instance.xpos == endx and instance.ypos == endy:
                bascTotal = instance.score
                newRein.pop(x)
            else:
                x +=1
        rein=newRein
    print(bascTotal)

for y in range(0,len(grid)):
    if 'S' in grid[y]:
        xpos, ypos = grid[y].index('S'), y
        rein = [Reindeer(xpos,ypos, '',0,False, False,'0,0','0,0')]
for y in range(0,len(grid)):
    if 'E' in grid[y]:
        endx, endy = grid[y].index('E'), y
        grid[endy][endx]='.'


def allR():
    global first, newRein, bascTotal, rein
    first = False
    total = 0
    for y in range(0,len(grid)):
        if 'S' in grid[y]:
            xpos, ypos = grid[y].index('S'), y
            rein = [Reindeer(xpos,ypos, '',0,False, False,'0,0','0,0')]
    while len(rein) > 0:
        newRein =[]
        for instance in rein:
            move(instance)
        x =0
        while x < len(newRein):
            instance = newRein[x]
            if instance.xpos == endx and instance.ypos == endy:
                if instance.score <= bascTotal-cs:
                    total += 1
                newRein.pop(x)
            else:
                x +=1
        rein=newRein
    print('part 1:',total)


firstR()
allR()


add = ['#','#']
oneAdd = 9999
add1 = [oneAdd, oneAdd]
for cell in data[0]:
    add.append('#')
    add1.append(oneAdd)
grid, minscores =[add],[add1]
for line in data:
    curr,curr1 = ['#'],[oneAdd]
    for cell in line:
        curr.append(cell)
        curr1.append(oneAdd)
    curr.append('#')
    curr1.append(oneAdd)
    grid.append(curr)
    minscores.append(curr1)
grid.append(add)
minscores.append(add1)




def leftOver(ren,dir):
    if ren.ypos > 0 and ren.dire != 'S'and dir =='N':
        if minscores[ren.ypos-1][ren.xpos] != 9999:
            if ren.score+cs1 <= minscores[ren.ypos-1][ren.xpos]:
                newScore = ren.score +1+ (bascTotal - minscores[ren.ypos-1][ren.xpos])
                newRein.append(Reindeer(endx, endy, 'N', newScore,True, False,ren.start, str(ren.xpos)+','+str(ren.ypos-1)))
    #down
    if ren.ypos < len(grid)-1 and ren.dire != 'N'and dir =='S':
        if minscores[ren.ypos+1][ren.xpos] != 9999:
            if ren.score+cs1 <= minscores[ren.ypos+1][ren.xpos]:
                newScore = ren.score +1+ (bascTotal -minscores[ren.ypos+1][ren.xpos])
                newRein.append(Reindeer(endx, endy, 'S', newScore,True, False,ren.start, str(ren.xpos)+','+str(ren.ypos+1)))
    #left
    if ren.xpos > 0 and ren.dire != 'E'and dir =='W':
        if minscores[ren.ypos][ren.xpos-1] != 9999:
            if ren.score+cs1 <= minscores[ren.ypos][ren.xpos-1]:
                newScore = ren.score +1+ (bascTotal - minscores[ren.ypos][ren.xpos-1])
                newRein.append(Reindeer(endx, endy, 'W', newScore,True, False,ren.start, str(ren.xpos-1)+','+str(ren.ypos)))
    #right
    if ren.xpos < len(grid[0])-1 and ren.dire != 'W'and dir =='E':
        if minscores[ren.ypos][ren.xpos+1] != 9999:
            if ren.score+cs1 <= minscores[ren.ypos][ren.xpos+1]:
                newScore = ren.score +1+ (bascTotal -minscores[ren.ypos][ren.xpos+1])
                newRein.append(Reindeer(endx, endy, 'E', newScore,True, False,ren.start, str(ren.xpos+1)+','+str(ren.ypos)))




def move2(reind):
    if reind.actSkip is False:
        #up
        if grid[reind.ypos-1][reind.xpos] != '#' and reind.dire != 'S':
            if reind.score+1 <= minscores[reind.ypos-1][reind.xpos]:
                newRein.append(Reindeer(reind.xpos, reind.ypos-1, 'N', reind.score +1,reind.skip, False, '0,0','0,0'))
        #down
        if grid[reind.ypos+1][reind.xpos] != '#' and reind.dire != 'N':
            if reind.score+1 <= minscores[reind.ypos+1][reind.xpos]:
                newRein.append(Reindeer(reind.xpos, reind.ypos+1, 'S', reind.score +1,reind.skip, False, '0,0','0,0'))
        #left
        if grid[reind.ypos][reind.xpos-1] != '#' and reind.dire != 'E':
            if reind.score+1 <= minscores[reind.ypos][reind.xpos-1]:
                newRein.append(Reindeer(reind.xpos-1, reind.ypos, 'W', reind.score +1,reind.skip, False, '0,0','0,0'))
        #right
        if grid[reind.ypos][reind.xpos+1] != '#' and reind.dire != 'W':
            if reind.score+1 <= minscores[reind.ypos][reind.xpos+1]:
                newRein.append(Reindeer(reind.xpos+1, reind.ypos, 'E', reind.score +1,reind.skip, False, '0,0','0,0'))
    

    elif reind.actSkip > 1:
        #up
        if reind.ypos > 0 and reind.dire != 'S':
            if reind.actSkip == 20:
                reind.start = str(str(reind.xpos) +','+str(reind.ypos))
            if grid[reind.ypos-1][reind.xpos] == '#':
                newRein.append(Reindeer(reind.xpos, reind.ypos-1, 'N', reind.score +1,True, reind.actSkip-1, reind.start, reind.end))
            elif reind.actSkip != 20:
                leftOver(reind,'N')
        #down
        if reind.ypos < len(grid)-1 and reind.dire != 'N':
            if reind.actSkip == 20:
                reind.start = str(str(reind.xpos) +','+str(reind.ypos))
            if grid[reind.ypos+1][reind.xpos] == '#':
                newRein.append(Reindeer(reind.xpos, reind.ypos+1, 'S', reind.score +1,True, reind.actSkip-1, reind.start, reind.end))
            elif reind.actSkip != 20:
                leftOver(reind,'S')
        #left
        if reind.xpos > 0 and reind.dire != 'E':
            if reind.actSkip == 20:
                reind.start = str(str(reind.xpos) +','+str(reind.ypos))
            if grid[reind.ypos][reind.xpos-1] == '#':
                newRein.append(Reindeer(reind.xpos-1, reind.ypos, 'W', reind.score +1,True, reind.actSkip-1, reind.start, reind.end))
            elif reind.actSkip != 20:
                leftOver(reind,'W')
        #right
        if reind.xpos < len(grid[0])-1 and reind.dire != 'W':
            if reind.actSkip == 20:
                reind.start = str(str(reind.xpos) +','+str(reind.ypos))
            if grid[reind.ypos][reind.xpos+1] == '#':
                newRein.append(Reindeer(reind.xpos+1, reind.ypos, 'E', reind.score +1,True, reind.actSkip-1, reind.start, reind.end))
            elif reind.actSkip != 20:
                leftOver(reind,'E')
        
    else:
        leftOver(reind,'N')
        leftOver(reind,'E')
        leftOver(reind,'S')
        leftOver(reind,'W')



def allR2():
    global first, newRein, bascTotal, rein
    first = False
    total = 0
    finishCheats = []
    for y in range(0,len(grid)):
        if 'S' in grid[y]:
            xpos, ypos = grid[y].index('S'), y
            rein = [Reindeer(xpos,ypos, '',0,False, False,'0,0','0,0')]
    while len(rein) > 0:
        if rein[0].score > bascTotal - cs:
            break
        newRein =[]
        for instance in rein:
            move2(instance)
            if instance.actSkip is False and instance.skip is False:
                instance.actSkip = 20
                move2(instance)
        x =0
        while x < len(newRein):
            instance = newRein[x]
            if instance.xpos == endx and instance.ypos == endy:
                cheat = [instance.start, instance.end]
                if instance.score <= bascTotal-cs and cheat not in finishCheats:
                    print('score',instance.score)
                    print('add',bascTotal-instance.score, instance.start, instance.end, instance.skip)
                    total += 1
                    finishCheats.append(cheat)
                newRein.pop(x)
            else:
                x +=1
        rein=newRein
    print('part 2:',total)


for y in range(0,len(grid)):
    if 'S' in grid[y]:
        xpos, ypos = grid[y].index('S'), y
        rein = [Reindeer(xpos,ypos, '',0,False, False,'0,0','0,0')]
firstR()
allR2()