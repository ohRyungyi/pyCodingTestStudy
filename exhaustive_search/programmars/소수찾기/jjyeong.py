from itertools import permutations
import math
def is_prime_number(n):
    if n==0 or n==1:    
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):   # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
            if n % i == 0:                          # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
                return False

        return True


def solution(numbers):
    answer = []
    
    li = []
    for num in numbers:
        li.append(num)

    u = []
    for i in range(1, len(li)+1):

        if i == 1: 
            u.append(list(set(li)))

        else:
            for len_ in range(2, len(li)+1):
                permu_li = list(map(''.join, set(list(permutations(li, len_)))))  #map 함수 공부하기
                u.append(permu_li)

    for i in range(len(u)):
        for j in range(len(u[i])):
            if is_prime_number(int(u[i][j])):
                answer.append(int(u[i][j]))


    return len(set(answer))