import sys

size_list = list()

N = int(sys.stdin.readline())

for i in range(N):
    height, weight = sys.stdin.readline().split('\n')[0].split(' ')
    
    size_list.append([int(height), int(weight)])

rankings = [ 1 for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        # print(size_list[i]," vs ",size_list[j])

        if size_list[i][0] > size_list[j][0] and size_list[i][1] > size_list[j][1]:
            rankings[j]+=1
        elif size_list[i][0] < size_list[j][0] and size_list[i][1] < size_list[j][1]:
            rankings[i]+=1
        # print(rankings)

# print(rankings)

for rank in rankings:
    print(rank, end=' ')

'''
입력
5
55 185
58 183
88 186
60 175
46 155

출력
2 2 1 2 5
'''