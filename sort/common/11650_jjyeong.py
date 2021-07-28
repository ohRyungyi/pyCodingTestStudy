import sys

N = int(sys.stdin.readline())

li = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)] # tuple 씌우는거 되더라.. 

sorted_li = sorted(li, key=lambda x : (x[0], x[1]))
for i in range(N):
  print(*sorted_li[i])


#5
#li = [(3, 4), (1, 1), (1, -1), (2, 2), (3, 3)] <- tuple(map())