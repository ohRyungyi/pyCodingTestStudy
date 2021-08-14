import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[False]*n for _ in range(n)]

map_info = []
for _ in range(n):
    col = list(sys.stdin.readline().rstrip())
    map_info.append(col)

#print(map_info)

x, y = 0, 0
complex = []
while x < n and y < n:
    #print(x, y)
    ori_x = x
    ori_y = y

    if graph[x][y] == True:
        y = ori_y + 1
        if y >= n:
            y = 0
            x = ori_x + 1
        continue

    graph[x][y] = True
    cnt = 0

    if map_info[x][y] == '1':
        queue = deque([(x, y)])
        cnt += 1

        while queue:
            v = queue.popleft()
            x = v[0]
            y = v[1]

            if x > 0:
                if graph[x-1][y] == False:
                    graph[x-1][y] = True
                    if map_info[x-1][y] == '1':
                        queue.append((x-1, y))
                        cnt += 1
            
            if y > 0:
                if graph[x][y-1] == False:
                    graph[x][y-1] = True
                    if map_info[x][y-1] == '1':
                        queue.append((x, y-1))
                        cnt += 1
            
            if x < n-1:
                if graph[x+1][y] == False:
                    graph[x+1][y] = True
                    if map_info[x+1][y] == '1':
                        queue.append((x+1, y))
                        cnt += 1
            
            if y < n-1:
                if graph[x][y+1] == False:
                    graph[x][y+1] = True
                    if map_info[x][y+1] == '1':
                        queue.append((x, y+1))
                        cnt += 1
    
    if cnt > 0:
        complex.append(cnt)

    y = ori_y + 1
    x = ori_x
    if y >= n:
        y = 0
        x = ori_x + 1

complex.sort()
print(len(complex))
if len(complex) != 0:
    print(*complex, sep='\n')

'''
입력 예시
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

7
0110100
0110101
1110101
0000111
0100000
0111110
0111001

5
11111
10001
10101
10001
11111

출력 예시
3
7
8
9

4
1
7
8
9

2
1
16
'''