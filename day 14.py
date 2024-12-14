class Robots:
    def __init__(self, xpos, ypos, vx, vy):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy


def moveUp(robot):
    if robot.ypos > 0:
        robot = Robots(robot.xpos, robot.ypos-1, robot.vx, robot.vy)
    else:
        robot = Robots(robot.xpos, len(grid)-1, robot.vx, robot.vy)
    return robot

def moveDown(robot):
    if robot.ypos < len(grid)-1:
        robot = Robots(robot.xpos, robot.ypos+1, robot.vx, robot.vy)
    else:
        robot = Robots(robot.xpos, 0, robot.vx, robot.vy)
    return robot


def moveLeft(robot):
    if robot.xpos > 0:
        robot = Robots(robot.xpos-1, robot.ypos, robot.vx, robot.vy)
    else:
        robot = Robots(len(grid[0])-1, robot.ypos, robot.vx, robot.vy)
    return robot

def moveRight(robot):
    if robot.xpos < len(grid[0])-1:
        robot = Robots(robot.xpos+1, robot.ypos, robot.vx, robot.vy)
    else:
        robot = Robots(0, robot.ypos, robot.vx, robot.vy)
    return robot


with open('14.txt') as j:
    data = [i for i in j.read().strip().split("\n")]


grid = []
for line in range(0,103):
    curr = []
    for row in range(0,101):
        curr.append('.')
    grid.append(curr)

robots = []
for i in range(0,len(data)):
    curr = data[i].split(' ')
    xy = curr[0]
    vel = curr[1]
    x = int(xy[2:xy.index(',')])
    y = int(xy[xy.index(',')+1:])
    v1 = int(vel[2:vel.index(',')])
    v2 = int(vel[vel.index(',')+1:])
    robots.append(Robots(x,y,v1,v2))


def part1():
    left = len(grid[0])//2 -1
    right = len(grid[0])//2 +1
    up = len(grid)//2 -1
    down = len(grid)//2 +1
    q1,q2,q3,q4 = 0,0,0,0
    for instance in robots:
        if instance.xpos <= left and instance.ypos <= up:
            q1 +=1
        elif instance.xpos >= right and instance.ypos <= up:
            q2 +=1
        elif instance.xpos <= left and instance.ypos >= down:
            q3 +=1
        elif instance.xpos >= right and instance.ypos >= down:
            q4 +=1
    print('part 1:',q1*q2*q3*q4)

#[y,[x],y,[x]]
def lineCheck(array):
    inst = []
    for instance in array:
        if instance.ypos in inst:
            inst[inst.index(instance.ypos)+1].append(instance.xpos)
        else:
            inst.append(instance.ypos)
            inst.append([instance.xpos])
    for i in range(1,len(inst),2):
        allX = inst[i]
        allX.sort()
        streak,top = 0,0
        for c in range(1,len(allX)):
            if allX[c-1] +1 == allX[c]:
                streak += 1
            elif allX[c-1] +1 < allX[c]:
                if streak > top:
                    top = streak
                    streak =0
        if top >= 30 or streak >= 30:
            return True
    return False


def printing(table, robos):
    for instance in robos:
        table[instance.ypos][instance.xpos] = 'X'
    for line in table:
        curr = ''
        for cell in line:
            curr += cell
        print(curr)


sec = 0
while lineCheck(robots) is False:
    if sec == 100:
        part1()
    newRobots = []
    for instance in robots:
        for x in range(0,abs(instance.vx)):
            if instance.vx > 0:
                instance = moveRight(instance)
            else:
                instance = moveLeft(instance)
        for y in range(0,abs(instance.vy)):
            if instance.vy > 0:
                instance = moveDown(instance)
            else:
                instance = moveUp(instance)
        newRobots.append(instance)
    robots = newRobots
    sec +=1

printing(grid,robots)
print('part 2:',sec)






