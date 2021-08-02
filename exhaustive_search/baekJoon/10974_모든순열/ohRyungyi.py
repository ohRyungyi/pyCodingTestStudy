import sys

N = int(sys.stdin.readline())

int_list = [i for i in range(1, N+1)]

result = list()

def permutation(int_list, start, end, result):
    if start == end:
        result.append(' '.join(map(str, int_list)))
    else:
        for i in range(start, end):
            int_list[start], int_list[i] = int_list[i], int_list[start]
            permutation(int_list, start+1, end, result)
            int_list[start], int_list[i] = int_list[i], int_list[start]

permutation(int_list, 0, N, result)
result.sort()
for i in result:
    print(i)

# print(sorted([2, 1]))


'''
입력
3

출력
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''