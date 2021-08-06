def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start_p = commands[i][0]
        end_p = commands[i][1]
        index_p = commands[i][2]
        
        sorted_li = sorted(array[start_p-1:end_p])
        answer.append(sorted_li[index_p -1])
    return answer


