import sys

n = int(sys.stdin.readline())
int_list = list()

for i in range(n):
    int_list.append(int(sys.stdin.readline()))

int_list.sort()

for i in int_list:
    print(i)