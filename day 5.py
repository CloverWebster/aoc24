with open('5.txt') as j:
    data = [i for i in j.read().strip().split("\n\n")]

rules = data[0].split('\n')
for x in range(0,len(rules)):
    rules[x] = rules[x].split('|')
updates = data[1].split('\n')
for x in range(0,len(updates)):
    updates[x] = updates[x].split(',')

total1, total2 = 0,0
for update in updates:
    toAdd = 1
    alreadySort = False
    while alreadySort == False:
        alreadySort = True
        for x in range(0,len(update)):
            for rule in rules:
                num = update[x]
                if rule[0]== num:
                    if rule[1] in update:
                        for y in range(0,x):
                            if rule[1] == update[y]:
                                update[x] = rule[1]
                                update[y] = num
                                alreadySort = False
                                toAdd = 0
                                break

    if toAdd == 0:
        toAdd = int(update[len(update)//2])
        total2 += toAdd
    if toAdd == 1:
        toAdd = int(update[len(update)//2])
        total1 += toAdd
print('part 1: ', total1,'\npart 2: ', total2)