with open('7.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

'''
0 = *
1 = +
2 = II
'''
def part1():
    total = 0
    for x in range(0,len(data)):
        line = data[x].split(': ')
        nums = line[1].split(' ')
        testValue = int(line[0])
        for count in range(0,2**(len(nums)-1) ):
            ops = bin(count)
            ops = str(ops[2:])
            while len(ops) < len(nums) - 1:
                ops = '0' + ops
            curTotal = int(nums[0])
            for y in range(1,len(nums)):
                if ops[y-1] == '0':
                    curTotal = curTotal * int(nums[y])
                else:
                    curTotal += int(nums[y])
            if curTotal == testValue:
                total += testValue
                break
    print('part 1:', total)

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def part2():
    total = 0
    for x in range(0,len(data)):
        line = data[x].split(': ')
        nums = line[1].split(' ')
        testValue = int(line[0])
        for count in range(0,3**(len(nums)-1) ):
            ops = ternary(count)
            ops = str(ops)
            while len(ops) < len(nums) - 1:
                ops = '0' + ops
            curTotal = int(nums[0])
            for y in range(1,len(nums)):
                if ops[y-1] == '0':
                    curTotal = curTotal * int(nums[y])
                elif ops[y-1] == '1':
                    curTotal += int(nums[y])
                else:
                    curTotal = int(str(curTotal) + nums[y])
            if curTotal == testValue:
                total += testValue
                break
    print('part 2:', total)

part1()
part2()