import sys

n = int(sys.stdin.readline())
members = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    members.append([int(age), i, name])

members.sort(key = lambda x:(x[0], x[1]))

for mem in members:
    print(mem[0], mem[2])

'''
입력 예시
3
21 Junkyu
21 Dohyun
20 Sunyoung

출력 예시
20 Sunyoung
21 Junkyu
21 Dohyun
'''