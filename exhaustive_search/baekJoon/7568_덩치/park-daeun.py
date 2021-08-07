import sys

n = int(sys.stdin.readline())

people = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    people.append((x, y))

rank = []
for i in range(n):
    cnt = 1

    for j in range(n):
        if i == j:
            continue
        
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    
    rank.append(cnt)

print(*rank, sep=' ')

'''
입력 예시
5
55 185
58 183
88 186
60 175
46 155

출력 예시
2 2 1 2 5
'''