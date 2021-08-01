# def solution(citations):
#     answer = 0 # answer = 0
#     for i in range(len(citations)+1): # i = 0, 1, 2, 3, 4, 5 
#         #print(f'i : {i}')
#         count = 0
#         for j in range(len(citations)): #0, 1, 2, 3,
            
#             if citations[j] >= i: #
#                 count += 1 #
#                 #print(f'count : {count}')
#             if count == i :
#                 answer = i
#                 break 

#     return answer

# print(solution([10,32,19,48,32]))

# 우수 코드
cit = [10,32,19,48,32]
cit.sort(reverse=True)
print(max(map(min, enumerate(cit, start=1))))

