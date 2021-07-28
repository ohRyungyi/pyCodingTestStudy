import sys

N = int(sys.stdin.readline())

li=[]
for _ in range(N):
  word = sys.stdin.readline().strip() 
  li.append((len(word), word))

sorted_li = sorted(list(set(li)), key=lambda x : (x[0], x[1]))

for i in range(len(sorted_li)):
  print(sorted_li[i][1])