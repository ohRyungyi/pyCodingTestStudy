import sys

N = int(sys.stdin.readline())

S = list()

for i in range(N):
    data = list(map(int, sys.stdin.readline().split('\n')[0].split(' ')))
    S.append(data)

dif = 400

start = '0'*(N//2)+'1'*(N//2)
end = '1'*(N//2)+'0'*(N//2)

num_list = [i for i in range(1, N+1)]

start_list = list()
end_list = list()

answer = []

for i in range(int(start, 2), int(end, 2)+1):
    # print(i)
    num = format(i, 'b').zfill(N)
    if num.count('1') == N//2 and num[0] == '0':
        
        # print(num, num[0])

        start_sum = 0 # 0 and 0
        link_sum = 0 # 1 and 1

        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                if num[i] == '1' and num[j] == '1' and i!=j:
                    link_sum+=S[i][j]
                    link_sum+=S[j][i]
                elif num[i] == '0' and num[j] == '0' and i!=j:
                    start_sum+=S[i][j]
                    start_sum+=S[j][i]
        
        answer.append(abs(start_sum-link_sum))
    elif num[0] == '1':
        break
print(sorted(answer)[0])

# result = 100*N//2

# for i , (start, link) in enumerate(zip(start_list, end_list)):
    
#     length = len(start)
#     # print(start, link)

#     start_sum = 0
#     link_sum = 0

#     for start_start, start_link in zip(start, link):
#         for end_start, end_link in zip(start, link):
#             if start_start != end_start and start_link != end_link:
#                 # print('start = ',start_start, end_start, ', sum = ', S[start_start][end_start])
#                 start_sum += S[start_start][end_start]
#                 # print('link = ',start_link, end_link, ', sum = ', S[start_link][end_link])
#                 link_sum += S[start_link][end_link]

#     # print(start_sum, link_sum)
#     if result > abs(start_sum - link_sum) :
#         result = abs(start_sum - link_sum)

# print(result)

'''
입력
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

출력
0

입력
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

출력
2

입력
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0

출력
1
'''