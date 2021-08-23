from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            queue = deque([i])
            answer += 1

        while queue:
            v = queue.popleft()

            for j in range(len(computers[v])):
                if visited[j] == False and computers[v][j] == 1:
                    queue.append(j)
                    visited[j] = True
    
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))

'''
입력 예시
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

출력 예시
2

1
'''