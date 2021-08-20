def solution(numbers, target):
    answer = 0

    for i in range(2 ** len(numbers)):
        case = format(i, "020b")
        case = case[20-len(numbers):]
        #print(case)

        num = 0
        for k in range(len(case)):
            #print(case[k])
            if case[k] == '0':
                num += numbers[k]
            else:
                num += -numbers[k]
        
        if num == target:
            answer += 1

    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

'''
입력 예시
numbers = [1, 1, 1, 1, 1]
target = 3

numbers = [1, 2, 1, 2]
target = 2

출력 예시
5

3
'''