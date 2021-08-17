import sys
from collections import deque

def bfs(graph, visited, x, y, max_x, max_y):
    ans = []

    while x <= max_x and y <= max_y:
        queue = deque()

        if graph[x][y] == 0:
            visited = [[False] * (max_y+1) for _ in range(max_x+1)]
            visited[x][y] = True
            queue.append((x,y,0))

            #print(x,y)

        while queue:
            v = queue.popleft()
            a, b, cnt = v[0], v[1], v[2]

            if graph[a][b] == 1 and (a != x or b != y):
                #print(">>", a, b, cnt)
                ans.append(cnt)
                break

            if a > 0:
                if visited[a-1][b] == False:
                    visited[a-1][b] = True
                    queue.append((a-1, b, cnt+1))

            if a > 0 and b > 0:
                if visited[a-1][b-1] == False:
                    visited[a-1][b-1] = True
                    queue.append((a-1, b-1, cnt+1))
            
            if a > 0 and b < max_y:
                if visited[a-1][b+1] == False:
                    visited[a-1][b+1] = True
                    queue.append((a-1, b+1, cnt+1))
            
            if b > 0:
                if visited[a][b-1] == False:
                    visited[a][b-1] = True
                    queue.append((a, b-1, cnt+1))

            if b < max_y:
                if visited[a][b+1] == False:
                    visited[a][b+1] = True
                    queue.append((a, b+1, cnt+1))
            
            if a < max_x and b > 0:
                if visited[a+1][b-1] == False:
                    visited[a+1][b-1] = True
                    queue.append((a+1, b-1, cnt+1))
            
            if a < max_x:
                if visited[a+1][b] == False:
                    visited[a+1][b] = True
                    queue.append((a+1, b, cnt+1))
            
            if a < max_x and b < max_y:
                if visited[a+1][b+1] == False:
                    visited[a+1][b+1] = True
                    queue.append((a+1, b+1, cnt+1))

            #print(queue)

        x += 1

        if x > max_x:
            x = 0
            y += 1
        
        if y > max_y:
            if len(ans) == 0:
                return 0

            return max(ans)

    return max(ans)


n, m = map(int, sys.stdin.readline().split())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
print(bfs(space, visited, 0, 0, n-1, m-1))

'''
입력 예시
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1

7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1

출력 예시
2

2
'''