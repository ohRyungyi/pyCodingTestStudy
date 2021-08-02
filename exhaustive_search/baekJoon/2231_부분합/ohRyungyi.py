import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    int_list = list(map(int, str(i)))
    sub_sum = sum(int_list)+i
    # print(sub_sum )

    if sub_sum == N:
        print(i)
        break

    if i == N:
        print(0)

# for i in range(N):
#     print(str(i).split(''))
    # int_list = [int(n) for n in str(i).split('')]
    # print(int_list)
    # subSum = i+

'''
입력
216

출력
198
'''