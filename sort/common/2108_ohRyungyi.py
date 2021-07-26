import sys

N = int(sys.stdin.readline())

int_list = list()
common_list = list()
ind = 0

for i in range(N):
    data = int(sys.stdin.readline())
    int_list.append(data)
    count = int_list.count(data)
    if count > ind :
        common_list = list()
        common_list.append(data)
        ind = count
    elif count == ind:
        common_list.append(data)

int_list.sort()
common_list.sort()

print(int(round( sum(int_list)/N, 0)))
print(int_list[int(N/2)])
result3 = common_list[0]
if len(common_list) > 1:
    result3 = common_list[1]
print(result3)
print(int_list[-1]-int_list[0])
