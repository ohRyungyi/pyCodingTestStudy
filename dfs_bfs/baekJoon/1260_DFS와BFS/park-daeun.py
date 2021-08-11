import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
adj_matrix = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj_matrix[a-1][b-1] = 1
    adj_matrix[b-1][a-1] = 1

# dfs------------------------------------------
stack = []
nodes = [0] * N
dfs_ans = []
def dfs(g, v):
    #print(g, v)
    nodes[v] = 1
    stack.append(v)
    dfs_ans.append(v+1)
    for i in range(len(g[0])):
        #print(v, i)
        if nodes[i] == 0 and g[v][i] == 1:
            dfs(adj_matrix, i)

    stack.pop()

dfs(adj_matrix, V-1)
print(*dfs_ans, sep=' ')

# bfs------------------------------------------
q = deque([V-1])
nodes = [0] * N
bfs_ans = [V]
while(True):
    #print(q)
    node = q.popleft()
    nodes[node] = 1

    for i in range(len(adj_matrix[0])):
        #print(nodes)
        #print(node, i)
        if nodes[i] == 0 and adj_matrix[node][i] == 1:
            q.append(i)
            bfs_ans.append(i+1)
            nodes[i] = 1

    if len(q) == 0:
        break

print(*bfs_ans, sep=' ')
'''
입력 예시
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1

1000 1 1000
999 1000

출력 예시
1 2 4 3
1 2 3 4

3 1 2 5 4
3 1 4 2 5

1000 999
1000 999
'''