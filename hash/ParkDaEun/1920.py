import sys
n = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
B = map(int, sys.stdin.readline().split())

A_dict = dict.fromkeys(A, 0)

for i in B:
    if i in A_dict.keys():
        print(1)
    else:
        print(0)

'''
입력 예시
5
4 1 5 2 3
5
1 3 7 9 5

출력 예시
1
1
0
0
1
'''
