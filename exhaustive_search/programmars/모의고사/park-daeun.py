def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    i, j, k = 0, 0, 0
    
    score = {1: 0, 2: 0, 3: 0}
    
    for a in answers:
        #print(a, one[i], two[j], thr[k])
        if a == one[i]:
            score[1] += 1
        if a == two[j]:
            score[2] += 1
        if a == thr[k]:
            score[3] += 1
        
        i += 1
        j += 1
        k += 1
        
        if i >= 5:
            i = 0
        if j >= 8:
            j = 0
        if k >= 10:
            k = 0
            
    score = list(score.items())
    score.sort(key = lambda x : -x[1])
    #print(score)
    
    if score[0][1] == score[1][1] and score[1][1] == score[2][1]:
        answer = [1, 2, 3]
    elif score[0][1] == score[1][1]:
        answer = [score[0][0], score[1][0]]
    else:
        answer = [score[0][0]]
    
    return answer

answers = [1,2,3,4,5]
print(solution(answers))

'''
입력 예시
answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

출력 예시
return = [1]
return = [1,2,3]
'''