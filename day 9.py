with open('9.txt') as j:
    input = [i for i in j.read().strip()]

data = list(input)

def part1():
    count = 0
    diskMap = []
    total = 0

    for x in range(0,len(data),2):
        fileSize = int(data[x])
        if x+1 < len(data):
            spaceSize = int(data[x+1])
        else:
            spaceSize = 0
        for y in range(0,fileSize):
            diskMap.append(count)
        count+=1
        for y in range(0,spaceSize):
            diskMap.append('.')
    print('diskmap done')


    for x in range(len(diskMap)-1,-1,-1):
        if diskMap.index('.') < x:
            diskMap[diskMap.index('.')] = diskMap[x]
            diskMap[x] = '.'
        else:
            break
    print('ordered')

    for x in range(0,len(diskMap)):
        if diskMap[x] == '.':
            break
        total += x * diskMap[x]
    print('part 1:', total)

def part2():
    count = 0
    diskMap = []
    total = 0

    for x in range(0,len(data),2):
        fileSize = int(data[x])
        if x+1 < len(data):
            spaceSize = int(data[x+1])
        else:
            spaceSize = 0
        curr = []
        for y in range(0,fileSize):
            curr.append(count)
        diskMap.append(curr)
        count+=1
        if spaceSize!=0:
            curr = []
            for y in range(0,spaceSize):
                curr.append('.')
            diskMap.append(curr)
    print('diskmap done')

    x = len(diskMap)-1
    while x >= 0:
        y=-1
        while y < len(diskMap)-1:
            y+=1
            swap = False
            if diskMap[y][0]=='.' and y < x and len(diskMap[y]) >= len(diskMap[x]) and diskMap[x][0]!= '.':
                swap = True
                for i in range(0,len(diskMap[x])):
                    diskMap[y][i] = diskMap[x][i]
                for i in range(0,len(diskMap[x])):
                    diskMap[x][i] = '.'
                if len(diskMap[y]) > len(diskMap[x]):
                    space = len(diskMap[y]) - len(diskMap[x])
                    diskMap[y] = diskMap[y][:diskMap[y].index('.')]
                    curr=[]
                    for i in range(0,space):
                        curr.append('.')
                    diskMap.insert(y+1, curr)
                    x = x+1
                if x-1 >= 0:
                    if diskMap[x-1][0] == '.':
                        diskMap[x-1]+=(diskMap[x])
                        diskMap.pop(x)
                        x=x-1
                if x+1 <len(diskMap):
                    if diskMap[x+1][0] == '.':
                        diskMap[x+1]+=(diskMap[x])
                        diskMap.pop(x)
                        x +=1
                if y-1 >= 0:
                    if diskMap[y-1][0] == diskMap[y][0]:
                        diskMap[y-1]+=(diskMap[y])
                        diskMap.pop(y)
                        y,x =y-1, x-1
                if y+1 <len(diskMap):
                    if diskMap[y+1][0] == diskMap[y][0]:
                        diskMap[y+1] += (diskMap[y])
                        diskMap.pop(y)
                        x=x-1
            if swap is True:
                break
        x = x -1

    count = 0
    for x in range(0,len(diskMap)):
        for y in range(0,len(diskMap[x])):
            if diskMap[x][y] != '.':
                total += count*int(diskMap[x][y])
            count +=1
    print('part 2:',total)



part1()
part2()