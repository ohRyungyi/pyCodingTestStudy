import sys

data = list(sys.stdin.readline().split('\n')[0])
data_list = list()

for i in data:
    data_list.append(int(i))

datas_list = sorted(data_list, reverse = True)

for i in datas_list:
    print(i, end='')


