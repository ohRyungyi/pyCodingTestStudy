import sys
data = []
for i in range(9):
    n = int(sys.stdin.readline())
    data.append(n) #입력된 난쟁이 키 data리스트에 저장
from itertools import combinations
com_data = list(combinations(data, 7)) #9명의 난쟁이 중 7명의 난쟁이를 뽑아 com_data에 저장
sum_com_data = list(map(sum, com_data)) #7명 뽑은 난쟁이들 키의 합을 sum_com_data에 저장

for i in range(36):
    if sum_com_data[i] == 100:
        result = list(com_data[i])
        result.sort()
        print(*result, sep='\n')
        break;