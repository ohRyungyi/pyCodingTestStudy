import sys

N = int(sys.stdin.readline())

binary = list(map(int, sys.stdin.readline().split('\n')[0]))
print(binary.count(1))


# cnt = 0

# while binary != 0:
#     temp = ~binary+1
#     temp = binary&temp
#     binary = binary - temp
#     cnt += 1
#     # break    
# print(cnt)
'''
입력
5
10110

출력
3
'''