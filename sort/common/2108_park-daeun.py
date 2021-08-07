import sys

n = int(sys.stdin.readline())
num_list = []
num_count = {}

for _ in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)
    
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

num_list.sort()
print(num_list)
num_count = sorted(num_count.items(), key = lambda x : (-x[1], x[0]))
print(num_count)

print(round(sum(num_list)/n))
print(num_list[int(len(num_list)/2)])
if len(num_count) > 1 and num_count[0][1] == num_count[1][1]:
    print(num_count[1][0])
else:
    print(num_count[0][0])
print(max(num_list)-min(num_list))

'''
입력 예시
5
1
3
8
-2
2

1
4000

5
-1
-2
-3
-1
-2

15
1
1
1
2
2
2
3
3
3
4
4
4
5
6
7

출력 예시
2
2
1
10

4000
4000
4000
0

-2
-2
-1
2
'''