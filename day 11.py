with open('11.txt') as j:
    nums = [i for i in j.read().strip().split(" ")]

for x in range(0,len(nums)):
    nums[x] == int(nums[x])


def zero(num):
    return 1

def even(num):
    num = str(num)
    half = len(num) //2
    first = int(num[:half])
    second = int(num[half:])
    return first,second

def other(num):
    return int(num) * 2024

def clean(Stones):
    p=0
    while p < len(Stones):
        if Stones[p] in Stones[p+1:]:
            pair = Stones[p+1:].index(Stones[p])
            if pair %2 ==1:
                Stones[p+pair+2] += Stones[p+1]
                Stones.pop(p+1)
                Stones.pop(p)
                p -= 2
        p += 2


def twentyFiveLoop(data,loop):
    data = sorting(data)
    for count in range(0,loop):
        newStones = []
        for x in range(0,len(data),2):
            counter = data[x+1]
            new = ruleCheck(data[x])
            if len(new) == 2:
                l = [new[0],counter,new[1],counter]
            else:
                l = [new[0],counter]
            newStones+=l
        clean(newStones)
        data = newStones
    return data

def sorting(numList):
    numList.sort()
    newNumList = []
    x = 0
    current = ''
    while x <= len(numList)-1:
        if numList[x] != current:
            newNumList.append(numList[x])
            newNumList.append(numList.count(numList[x]))
            current = numList[x]
        x+=1
    return newNumList


def rules(num):
    if num ==0 or num == '0':
        return [zero(0)]
    elif len(str(num)) % 2 == 0:
        firs, sec = even(num)
        return [firs,sec]
    else:
        return [other(num)]

rules_memo = {}
def ruleCheck(k):
    if k not in rules_memo:
        rules_memo[k] = rules(k)
    return rules_memo[k]

def parts(it):
    data = twentyFiveLoop(nums,it)
    total = 0
    for q in range(1,len(data),2):
        total += data[q]
    print(total)

parts(25)
parts(75)