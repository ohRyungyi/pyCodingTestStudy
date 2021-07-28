# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys

N = int(sys.stdin.readline())

int_list = list()
int_dict = dict()

comm_ind = 0
comm = list()

for i in range(N):
    data = int(sys.stdin.readline())
    int_list.append(data)

    if data not in int_dict:
        int_dict[data]=1
    else:
        int_dict[data]+=1

int_list.sort()

print(int(round(sum(int_list)/N, 0)))
print(int_list[int(N/2)])

ind = 0
one = -4001
two = -4001
count = 0
for data, val in int_dict.items():
    if val > ind:
        one = data
        two = -4001
        ind = val
        count = 1
    elif val == ind:
        count+=1
        if one > data:
            two = one
            one = data
        elif two > data:
            two = data

if count == 1:
    print(one)
else:
    print(two)


print(int_list[-1]-int_list[0])