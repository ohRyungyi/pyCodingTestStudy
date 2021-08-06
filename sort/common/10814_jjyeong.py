import sys

N = int(sys.stdin.readline())

li = []
for i in range(N):
  a, b = sys.stdin.readline().split() # ★주의 ! 나이를 문자로 받아서는 안됨. . . map(str, ...) -> X
  tmp = [i, int(a), b]
  li.append(tuple(tmp))


sorted_li = sorted(li, key=lambda x : (x[1], x[0]))
for i in range(N):
  print(sorted_li[i][1], sorted_li[i][2])