import sys
n = int(sys.stdin.readline())
data = list(range(1,n+1))
from itertools import permutations
p = list(permutations(data, n))
for i in range(len(p)):
    print(*p[i], sep=' ')