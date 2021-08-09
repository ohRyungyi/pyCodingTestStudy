from itertools import permutations

def solution(numbers):
    num_set = [] # 카드의 조합 만드는 리스트

    for i in range(1, len(numbers)+1):
        num_set.extend(list(permutations(numbers, i)))

    num_set = set(num_set) # 중복 제거
    #print(num_set) # >> {('1', '0'), ('1', '1'), ('1', '1', '0'), ('1', '0', '1'), ('0', '1'), ('0',), ('0', '1', '1'), ('1',)}
    
    num_list = []
    for num in num_set: # tuple 형식으로 되어있는 숫자를 int로 변환해 새로운 리스트인 num_list에 저장
        num_list.append(int("".join(num))) # "".join(list) : list를 str로 변환
    
    num_list = set(num_list) # 중복 제거 (예. ('0', '1') , ('1'))

    # 소수의 개수 구하기
    answer = 0
    for num in num_list:
        if num < 2: # 0, 1 일 때는 pass
            continue

        # 소수인지 판별
        isPrime = 1
        for i in range(2, num):
            if num % i == 0:
                isPrime = 0
                break

        if isPrime == 1:
            answer += 1

    return answer

numbers = "011"
print(solution(numbers))

'''
입력 예시
numbers = "17"

numbers = "011"

출력 예시
3

2
'''