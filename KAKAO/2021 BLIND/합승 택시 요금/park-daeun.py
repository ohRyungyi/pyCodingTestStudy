import heapq

INF = int(1e9)

def dijkstra(start, distance, graph): # 다익스트라 알고리즘 (최단 경로)
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        now, dist = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
    
    return distance

def solution(n, s, a, b, fares):
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]

    for fare in fares: # 양방향이므로 두번 append
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    
    total = [[]] # 전체 노드 -> 노드 거리 구함
    for i in range(1, n+1):
        dist = dijkstra(i, distance, graph)
        total.append(dist)
        distance = [INF] * (n+1)
    print(total)

    ans = INF
    for i in range(1, n+1):
        if i == s:
            continue

        ans = min(ans, total[s][i] + total[i][a] + total[i][b])
    ans = min(ans, total[s][a] + total[s][b])

    return ans

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, a, b, fares))

n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n, s, a, b, fares))

'''
입력 예시
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

출력 예시
82

14

18
'''