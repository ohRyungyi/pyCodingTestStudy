import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    cnt = 0
    while queue:
        v = queue.popleft()
        #print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    
    return cnt

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

visited = [False] * (n+1)
print(bfs(graph, 1, visited))

'''
입력 예시
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력 예시
4
'''