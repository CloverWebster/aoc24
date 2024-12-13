with open('13.txt') as j:
    data = [i for i in j.read().strip().split("\n\n")]

def part1():
    total = 0
    for i in range(0,len(data)):
        item = data[i].split('\n')
        line = item[0]
        a = int(line[12:line.index(',')])
        c = int(line[line.index(',')+4:])
        line = item[1]
        b = int(line[12:line.index(',')])
        d = int(line[line.index(',')+4:])
        line = item[2]
        e = int(line[9:line.index(',')])
        f = int(line[line.index(',')+4:])


        buttA = (f*b-e*d)/(c*b-a*d)
        buttB = (e-a*buttA)/b

        if buttA%1 ==0 and buttA >=0 and buttA < 101:
            if buttB%1 ==0 and buttB >=0 and buttB < 101:
                total += int(buttA*3) + int(buttB)
    print('total 1:',total)

def part2():
    total = 0
    for i in range(0,len(data)):
        item = data[i].split('\n')
        line = item[0]
        a = int(line[12:line.index(',')])
        c = int(line[line.index(',')+4:])
        line = item[1]
        b = int(line[12:line.index(',')])
        d = int(line[line.index(',')+4:])
        line = item[2]
        e = int(line[9:line.index(',')]) + 10000000000000
        f = int(line[line.index(',')+4:]) + 10000000000000


        buttA = (f*b-e*d)/(c*b-a*d)
        buttB = (e-a*buttA)/b

        if buttA%1 ==0 and buttA >=0:
            if buttB%1 ==0 and buttB >=0:
                total += int(buttA*3) + int(buttB)
    print('total 2:',total)

part1()
part2()