

def findNextDot(x,y):
    if data[y][x-1] == '.':
        return x-1,y
    elif data[y][x+1] == '.':
        return x+1,y
    elif data[y-1][x] == '.':
        return x,y-1
    elif data[y+1][x] == '.':
        return x,y+1
    return 0,0


def findLimit(i):
    if i >= len(data[0])-1 or i<1:
        return False
    return True


def main(cheat):
    global data
    with open('20.txt') as j:
        data = [i for i in j.read().strip().split("\n")]
    for i in range (0,len(data)):
        data[i] = list(data[i])
    out = 0

    ''' find the start '''
    cont = True
    for i in range (0,len(data)):
        if 'E' in data[i]:
            ypos,yE = i,i
            xpos,xE = data[i].index('E'),data[i].index('E')
            if cont is False:
                break
            cont = False
        if 'S' in data[i]:
            yS = i
            xS = data[i].index('S')
            if cont is False:
                break
            cont = False
        
    ''' replace dots with distance to end '''
    data[yE][xE],count = 0,1
    xpos, ypos = findNextDot(xpos,ypos)
    while xpos != 0:
        data[ypos][xpos] = count
        count += 1
        xpos, ypos = findNextDot(xpos,ypos)
    data[yS][xS] = count

    ''' check route savings from each point '''
    for y in range(1,len(data)-1):
        for x in range(1,len(data)-1):
            wins = []
            if data[y][x]!= '#':
                for ychange in range(-cheat,cheat+1):
                    ypos = y+ychange
                    if findLimit(ypos)is True:
                        xran = cheat+1-abs(ychange)
                        for xchange in range(0,xran):
                            xpos = x+xchange
                            if findLimit(xpos) is True and data[ypos][xpos] != '#':
                                save = data[y][x] - data[ypos][xpos]-abs(xchange)-abs(ychange)
                                if save >= 100:
                                    wins.append(save)
                            if xchange!=0:
                                xpos = x-xchange
                                if findLimit(xpos) is True and data[ypos][xpos] != '#':
                                    save = data[y][x] - data[ypos][xpos]-abs(xchange)-abs(ychange)
                                    if save >= 100:
                                        wins.append(save)
            out += len(wins)
                        
    print(out)

main(2)
main(20)

