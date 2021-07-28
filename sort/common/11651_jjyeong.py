import sys

N = int(sys.stdin.readline())

li = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)] 

sorted_li = sorted(li, key=lambda x : (x[1], x[0]))
for i in range(N):
  print(*sorted_li[i])