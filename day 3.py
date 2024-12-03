with open('3.txt') as j:
    data = [i for i in j.read().strip().split("\n")]


for line in data:
    while line.index('mul(') != None:
        pos = line.index('mul(')
        print(pos)

