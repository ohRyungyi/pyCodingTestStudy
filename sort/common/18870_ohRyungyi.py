import sys

N = int(sys.stdin.readline())

order = list()
ind = list()

data = list(sys.stdin.readline().split('\n')[0].split(' '))

for i in data:
    i = int(i)
    if i not in ind:
        ind.append(i)
    order.append(i)

ind.sort()
for i in order:
    print(ind.index(i), end=' ')