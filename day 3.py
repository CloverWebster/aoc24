with open('3.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

nums = ['0','1','2','3','4','5','6','7','8','9']
def part1():
    total = 0
    for y in data:
        line = y + '..........'
        while 'mul(' in line:
            pos = line.index('mul(')
            if ',' in line[pos+4:pos+8]:
                comma = line[pos+4:pos+8].index(',') +pos +4
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

                            total += num1*num2

            line = line.replace('mul(','',1)

    print(total)

def part2():
    total = 0
    mul = True
    for y in data:
        line = y + '..........do()don\'t()'
        line = line.replace('\'','-')
        while 'mul(' in line:
            pos = line.index('mul(')
            while line.index('do()') < pos or line.index('don-t()') < pos:
                if line.index('do()') < pos and line.index('do()') < line.index('don-t()'):
                    mul = True
                    line = line.replace('do()','',1)
                    pos = line.index('mul(')
                if line.index('don-t()') < pos and line.index('do()') > line.index('don-t()'):
                    mul = False
                    line = line.replace('don-t()','',1)
                pos = line.index('mul(')
            pos = line.index('mul(')
            

            if ',' in line[pos+4:pos+8]:
                comma = line[pos+4:pos+8].index(',') +pos +4
                if comma != pos + 4:
                    num = True
                    for x in range(pos+4,comma):
                        if line[x] not in nums:
                            num1 = 0
                            num = False
                            break
                    if num == True:
                        num1 = int(line[pos+4:comma])

                    if ')' in line[comma+1:comma+5]:
                        bracket = line[comma+1:comma+5].index(')') +comma +1
                        if bracket != comma +1:
                            num = True
                            for x in range(comma+1,bracket):
                                if line[x] not in nums:
                                    num2 = 0
                                    num = False
                                    break
                            if num == True:
                                num2 = int(line[comma+1:bracket])

                            if mul == True:
                                total += num1*num2

            line = line.replace('mul(','',1)

    print(total)


part1()
part2()