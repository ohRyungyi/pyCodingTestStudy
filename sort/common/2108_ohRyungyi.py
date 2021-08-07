import sys
from collections import Counter

N = int(sys.stdin.readline())

int_dict = dict()
int_list = list()
# int_list = [int(sys.stdin.readline()) for _ in range(N)]

for i in range(N):
    data = int(sys.stdin.readline())
    int_list.append(data)
    if data not in int_dict.keys():
        int_dict[data] = 1
    else:
        int_dict[data] += 1

int_list.sort()

# print(sorted(set(int_list)))

# int_dict = { i:int_list.count(i) for i in sorted(set(int_list))}
int_dict = sorted(int_dict.items(), key = lambda x: (x[1], -x[0]), reverse=True)

# print(int_dict)

print(round(sum(int_list)/N))
print(int_list[N//2])


if len(int_dict) > 1 and int_dict[0][1] == int_dict[1][1]:
    print(int_dict[1][0])
else:
    print(int_dict[0][0])

print(int_list[-1]-int_list[0])

# print(round(sum(int_list)/N))

# int_list.sort()

# print(int_list[N//2])

# int_dict = {  i:int_list.count(i) for i in set(int_list)}
# int_dict = sorted(int_dict.items(), key = lambda x : (-x[1], x[0]))


# if len(int_dict)>1 and int_dict[0][1] == int_dict[1][1]:
#     print(int_dict[1][0])
# else:
#     print(int_dict[0][0])
# # if len(int_dict) > 1 and int_dict[0][1] == int_dict[1][1]:

# print(int_list[-1]-int_list[0])


'''
입력
5
1
3
8
-2
2

출력
2
2
1
10

입력
1
4000

출력
4000
4000
4000
0

입력
5
-1
-2
-3
-1
-2

출력
-2
-2
-1
2

'''