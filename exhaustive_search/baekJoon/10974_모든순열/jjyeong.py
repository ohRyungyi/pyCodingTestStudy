import sys
from itertools import permutations

N = int(sys.stdin.readline())
li = list(range(1, N+1))
for permu in permutations(li,3):
    print(*permu)