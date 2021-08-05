import sys

li = [int(sys.stdin.readline()) for _ in range(9)]
#print(li)

#print(sum(li))
from itertools import combinations

#print(list(combinations(li,2)))
for com in combinations(li,2):
    if sum(li) - sum(com) == 100:
        li.remove(com[0])
        li.remove(com[1])
        break

print(*sorted(li), sep='\n')