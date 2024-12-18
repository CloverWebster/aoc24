class Elves:
    def __init__(self, xpos, ypos, dire, score):
        self.xpos = xpos
        self.ypos = ypos
        self.dire = dire
        self.score = score


with open('18.txt') as j:
    data = [i for i in j.read().strip().split("\n")]
grid, minscores =[],[]
for line in range(0,71):
    curr,curr1 = [],[]
    for cell in range(0,71):
        curr.append('.')
        curr1.append([999999999999999,999999999999999,999999999999999,999999999999999])
    grid.append(curr)
    minscores.append(curr1)

#NSWE

def contains(reg,array):
    add = False
    for x in range(0,len(array)):
        curr = array[x]
        if curr.xpos == reg.xpos and curr.ypos == reg.ypos:
            add = True
            if curr.score > reg.score:
                array[x] = reg
                break
    if add is False:
        array.append(reg)
        
    return array
    
    

def move(Elf):
    global newElf
    #up
    if Elf.ypos >0:
        if grid[Elf.ypos-1][Elf.xpos] != '#' and Elf.dire != 'S':
            if Elf.score+1 <= minscores[Elf.ypos-1][Elf.xpos][0]:
                newElf = contains(Elves(Elf.xpos, Elf.ypos-1, 'N', Elf.score +1), newElf)
                minscores[Elf.ypos-1][Elf.xpos][0] = Elf.score +1
    #down
    if Elf.ypos <len(grid)-1:
        if grid[Elf.ypos+1][Elf.xpos] != '#' and Elf.dire != 'N':
            if Elf.score+1 <= minscores[Elf.ypos+1][Elf.xpos][1]:
                newElf = contains(Elves(Elf.xpos, Elf.ypos+1, 'S', Elf.score +1), newElf)
                minscores[Elf.ypos+1][Elf.xpos][1] = Elf.score +1
    #left
    if Elf.xpos >0:
        if grid[Elf.ypos][Elf.xpos-1] != '#' and Elf.dire != 'E':
            if Elf.score+1 <= minscores[Elf.ypos][Elf.xpos-1][2]:
                newElf = contains(Elves(Elf.xpos-1, Elf.ypos, 'W', Elf.score +1), newElf)
                minscores[Elf.ypos][Elf.xpos-1][2] = Elf.score +1
    #right
    if Elf.xpos <len(grid[0])-1:
        if grid[Elf.ypos][Elf.xpos+1] != '#' and Elf.dire != 'W' :
            if Elf.score+1 <= minscores[Elf.ypos][Elf.xpos+1][3]:
                newElf = contains(Elves(Elf.xpos+1, Elf.ypos, 'E', Elf.score +1), newElf)
                minscores[Elf.ypos][Elf.xpos+1][3] = Elf.score +1
newElf=[]

for i in range(0,1024):
    line = data[i]
    coords = line
    coords = coords.split(',')
    x,y = int(coords[0]), int(coords[1])
    grid[y][x] = '#'

endx,endy = 70,70
'''
for line in grid:
    curr = ''
    for cell in line:
        curr += cell
    print(curr)
'''
def complete():
    global newElf
    elf = [Elves(0,0,'E',0)]
    total = 99999999999999999
    while len(elf) > 0:
        newElf =[]
        for instance in elf:
            move(instance)
        x =0
        while x < len(newElf):
            instance = newElf[x]
            if instance.xpos == endx and instance.ypos == endy:
                if instance.score < total:
                    total = instance.score
                    return total
                newElf.pop(x)
            else:
                x +=1
        elf=newElf
    return total

print('part 1:',complete())
for i in range(1024,len(data)):
    line = data[i]
    coords = line
    coords = coords.split(',')
    x,y = int(coords[0]), int(coords[1])
    grid[y][x] = '#'
    minscores = []
    for row in range(0,71):
        curr1 = []
        for cell in range(0,71):
            curr1.append([999999999999999,999999999999999,999999999999999,999999999999999])
        minscores.append(curr1)
    if complete() == 99999999999999999:
        print('part 2:',line)
        break
