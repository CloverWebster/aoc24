with open('17.txt') as j:
    data = [i for i in j.read().strip().split("\n")]


def combo(num):
    if num < 4:
        return num
    elif num == 4:
        return a
    elif num ==5:
        return b
    elif num ==6:
        return c

def adv(oper): # 0
    global a, ins
    a = a//pow(2,combo(oper))
    ins += 2

def bxl(oper): # 1
    global b, ins
    b = b^oper
    ins += 2
    
def bst(oper): # 2
    global b, ins
    b = combo(oper) % 8
    ins += 2

def jnz(oper): # 3
    global ins
    if a != 0:
        ins = oper
    else:
        ins += 2

def bxc(oper): # 4
    global b, ins
    b = b ^ c
    ins += 2

def out(oper): # 5
    global output, ins
    output += str(combo(oper)%8) +','
    ins += 2

def bdv(oper): # 6
    global b, ins
    b = a//pow(2,combo(oper))
    ins += 2

def cdv(oper): # 7
    global c, ins
    c = a//pow(2,combo(oper))
    ins += 2

a = int(data[0][data[0].index(':')+2:])
b = int(data[1][data[1].index(':')+2:])
c = int(data[2][data[2].index(':')+2:])
ins = 0
output = ''
nums = data[4][9:]
nums = nums.split(',')
for x in range(0,len(nums)):
    nums[x] = int(nums[x])

while ins < len(nums):
    opcode, operand = nums[ins], nums[ins +1]
    if opcode == 0:
        adv(operand)
    elif opcode == 1:
        bxl(operand)
    elif opcode == 2:
        bst(operand)
    elif opcode == 3:
        jnz(operand)
    elif opcode == 4:
        bxc(operand)
    elif opcode == 5:
        out(operand)
    elif opcode == 6:
        bdv(operand)
    elif opcode == 7:
        cdv(operand)

print('part 1:',output[:len(output)-1])

i = 1
while True:
    a = i
    b = 0
    c = 0
    ins = 0
    output = ''
    while ins < len(nums):
        opcode, operand = nums[ins], nums[ins +1]
        if opcode == 0:
            adv(operand)
        elif opcode == 1:
            bxl(operand)
        elif opcode == 2:
            bst(operand)
        elif opcode == 3:
            jnz(operand)
        elif opcode == 4:
            bxc(operand)
        elif opcode == 5:
            out(operand)
        elif opcode == 6:
            bdv(operand)
        elif opcode == 7:
            cdv(operand)

    newNums = output[:len(output)-1]
    newNums = newNums.split(',')
    for x in range(0,len(newNums)):
        newNums[x] = int(newNums[x])

    if len(nums) != len(newNums):
        i = i*8
    elif nums == newNums:
        print('part 2:', i)
        break
    else:
        for x in range(len(newNums)-1,-1,-1):
            if newNums[x] != nums[x]:
                i += pow(8,x)
                break


