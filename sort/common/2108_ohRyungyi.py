import sys
from collections import Counter

N = int(sys.stdin.readline())

int_list = [int(sys.stdin.readline()) for _ in range(N) ]
int_dict = dict()

for _ in range(N):
    data = int(sys.stdin.readline().strip())
    int_list.append(data)
    if data not in int_dict:
        int_dict[data] = 1
    else:
        int_dict[data]+=1

int_list.sort()
int_dict_list = sorted(int_dict.items(), key = lambda x : x[1])

print(int_dict_list)

print(int(round(sum(int_list)/N, 0)))
print(int_list[N//2])



# common = Counter(int_list).most_common(2);

# if len(common) == 1:
#     print(common[0][0])
# elif len(common) == 2:
#     if common[1][0] > common[0][0]:
#         print(commmon[0][0])
#     else:
#         print(common[1][0])



print(max(int_list)-min(int_list))



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