
def solution(numbers):
    answer = ''
    num_list = list()

    num_list = sorted(list(map(str, numbers)), key = lambda x : str(x)*5, reverse= True)

    answer = str(int(''.join(num_list)))
            
    return answer

print(solution([6, 10, 2]))
print()
print(solution([3, 30, 34, 5, 9]))
print()
print(solution([121, 12]))