with open('2.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

def upSafetyCheck(line):
    for x in range(1,len(line)):
        if line[x] <= line[x-1]:
            return False
        if line[x] - line[x-1] > 3:
            return False
    return True 


def downSafetyCheck(line):
    for x in range(1,len(line)):
        if line[x] >= line[x-1]:
            return False
        if line[x-1] - line[x] > 3:
            return False
    return True 


def doubleCheck(line):
    for x in range(0,len(line)):
        report = []
        for y in range(0,x):
            report.append(line[y])
        for y in range(x + 1, len(line)):
            report.append(line[y])
        if upSafetyCheck(report) == True or downSafetyCheck(report) == True:
            return True
            


def part1():
    total = 0
    for y in data:

        report = y.split(' ')
        for x in range(0,len(report)):
            report[x] = int(report[x])

        if report[0] > report[1]:
            check = downSafetyCheck(report)
        else:
            check = upSafetyCheck(report)

        if check == True:
            total += 1

    print(total)


def part2():
    total = 0
    for y in data:

        report = y.split(' ')
        for x in range(0,len(report)):
            report[x] = int(report[x])

        if report[0] > report[1]:
            check = downSafetyCheck(report)
        else:
            check = upSafetyCheck(report)

        if check == True:
            total += 1
        elif doubleCheck(report) == True:
            total += 1

    print(total)


part1()
part2()