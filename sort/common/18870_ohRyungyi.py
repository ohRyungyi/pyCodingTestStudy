# 만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면, 모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다.

import sys

N = int(sys.stdin.readline())

data_list = [int(x) for x in sys.stdin.readline().split('\n')[0].split(' ')]

print(data_list)