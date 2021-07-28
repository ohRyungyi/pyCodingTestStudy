import sys

N = sys.stdin.readline().strip() # int로 값 받고 
li = []
for i in range(len(N)):
  li.append(N[i])
li.sort(reverse=True)
li= list(map(int, li))
print(*li,sep='')