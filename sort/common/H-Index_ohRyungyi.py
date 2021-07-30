def solution(citations):
    answer = 0
    
    # citations.sort()

    # for i in range(len(citations)):
    #     # print(len(citations)-i, citations[i])
    #     if len(citations)-i >= citations[i]:
    #         answer = max(answer, citations[i])

    # # print(citations)

    citations.sort()

    print(citations)

    for ind, num in enumerate(citations):
        # print(str(num)+'번 이상 인용된 논문이 '+str(len(citations)-ind)+'편 이상')
        if len(citations)-ind <=  num:
            print(str(num)+'번 이상 인용된 논문이 '+str(len(citations)-ind)+'편 이상')
            return min(len(citations)-ind, num)

    return answer

print(solution([3, 0, 6, 1, 5])) # 0, 1, 3, 5, 6
print(solution([1, 2, 3, 4, 6, 0])) # 0, 1, 2, 3, 4, 6
print(solution([0, 1, 4, 5, 6]))
print(solution([0, 0, 0, 0, 0]))