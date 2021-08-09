from itertools import permutations

def solution(numbers):
    answer = []

    result = list()
    numbers = list(map(str, numbers))
    # print(numbers)

    int_list = []

    for i in range(1, len(numbers)+1) :
        for num in permutations(numbers, i):
            # print(int(''.join(num)))
            data = int(''.join(num))
            if data not in int_list:
                int_list.append(data)
                isPrime = True
                if data<=1:
                    continue
                else:
                    # print(data)
                    for i in range(2, data) :
                        if data%i == 0:
                            isPrime = False
                            break
                    if isPrime == True:
                        answer.append(data)

    # print(int_list, answer)
    return len(answer)

print(solution("17"))
print(solution("011"))