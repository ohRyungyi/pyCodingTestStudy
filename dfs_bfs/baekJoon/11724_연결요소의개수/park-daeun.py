import sys
from collections import deque

def bfs(graph, visited, v):
    visited[v] = True
    queue = deque([v])

    while queue:
        node = queue.popleft()
        #print(node, end=' ')

        for n in graph[node]:
            if visited[n] == False:
                visited[n] = True
                queue.append(n)

n, m = map(int, sys.stdin.readline().split())
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        bfs(graph, visited, i)
        cnt += 1

print(cnt)

'''
입력 예시
6 5
1 2
2 5
5 1
3 4
4 6

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

출력 예시
2

1
'''