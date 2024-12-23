with open('1.txt') as j:
    data = [i for i in j.read().strip().split("\n")]

total1 = 0
total2 = 0
first = []
second = []
for x in data:
    x = x.split('   ')
    first.append(int(x[0]))
    second.append(int(x[1]))

first = sorted(first)
second = sorted(second)


for x in range(0,len(first)):
    difference = second[x] - first[x]
    total1 += abs(difference)

for x in range(0,len(first)):
    instances = second.count(first[x])
    total2 += first[x] * instances


print('part 1 answer:', total1)
print('part 2 answer:', total2)