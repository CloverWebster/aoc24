with open('3.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

nums = ['0','1','2','3','4','5','6','7','8','9']
total = 0
for y in data:
    line = y + '..........'
    while 'mul(' in line:
        pos = line.index('mul(')
        if ',' in line[pos+4:pos+8]:
            comma = line[pos+4:pos+8].index(',') +pos +4
            print(comma)
            if comma != pos + 4:
                for x in range(pos+4,comma):
                    if line[x] not in nums:
                        num1 = 0
                        break
                num1 = int(line[pos+4:comma])

                if ')' in line[comma+1:comma+5]:
                    bracket = line[comma+1:comma+5].index(')') +comma +1
                    if bracket != comma +1:
                        for x in range(comma+1,bracket):
                            if line[x] not in nums:
                                num2 = 0
                                break
                        num2 = int(line[comma+1:bracket])

                        print('multiply', num1, num2)
                        total += num1*num2

        line = line.replace('mul(','',1)
        print(line)

print(total)



