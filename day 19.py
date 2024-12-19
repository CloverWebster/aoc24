with open('19.txt') as j:
    data = [i for i in j.read().strip().split("\n\n")]

towels = data[0]
towels =towels.split(', ')
designs= data[1]
designs = designs.split('\n')
for x in range(0,len(designs)):
    designs[x] = designs[x]

def newCom(curr,num):
    for x in towels:
        new = curr+x
        if new not in newCombos:
            if design.startswith(new) is True and len(new) <= len(design):
                newCombos.append(new)
                newCombos.append(num)
        elif new in newCombos:
            newCombos[newCombos.index(new)+1] += num

total1, total2, combos = 0,0,[]
for x in towels:
    combos.append(x)
    combos.append(1)
for design in designs:
    pt1 = False
    combos = []
    for x in towels:
        combos.append(x)
        combos.append(1)
    while len(combos) > 0:
        newCombos = []
        for i in range(0,len(combos),2):
            instance = combos[i]
            newCom(instance, combos[i+1])
        for i in range(0,len(newCombos)-1,2):
            combo = newCombos[i]
            if design == combo:
                if pt1 is False:
                    total1 += 1
                    pt1 = True
                total2 += newCombos[i+1]
            
        combos = newCombos
print('part 1:',total1)
print('part 2:',total2)