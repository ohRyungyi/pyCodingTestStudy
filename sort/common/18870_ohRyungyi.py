import sys

N = int(sys.stdin.readline())

int_list = [int(n) for n in sys.stdin.readline().split('\n')[0].split(' ')]

# print(int_list)

sorted_list = sorted(set(int_list))

sorted_dict = {sorted_list[i]:i for i in range(len(sorted_list))}

# print(sorted_dict)

for i in int_list:
    print(sorted_dict[i], end=' ')

'''
입력
5
2 4 -10 4 -9

출력
2 3 0 3 1

입력
6
1000 999 1000 999 1000 999

출력
1 0 1 0 1 0
'''