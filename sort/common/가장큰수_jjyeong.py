def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    #real_numbers = numbers.copy()
    #print(numbers)
    hash = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    for i in range(len(numbers)):
        if int(numbers[i]) % 10 == 0 or len(numbers[i]) == 1:
            #print(numbers[i])
            hash[int(numbers[i][0])].append([i,numbers[i]])
        #print(hash)

    for key in hash:
        if len(hash[key]) > 1 : #len이 2이상이면 
            if len(hash[key]) % 2 == 0: #짝수개라면 ex) 4라면 
                for j in range(len(hash[key])//2): # 0, 1, 2, 3 
                    numbers[hash[key][j][0]] , numbers[hash[key][len(hash[key]) - 1 - j][0]] = numbers[hash[key][len(hash[key]) - 1 - j][0]], numbers[hash[key][j][0]] 
            else: #홀수개라면 
                for j in range(len(hash[key])//2): #0, 1, 2, 3, 4 
                    numbers[hash[key][j][0]] , numbers[hash[key][len(hash[key]) - 1 - j][0]] = numbers[hash[key][len(hash[key]) - 1 - j][0]], numbers[hash[key][j][0]] 
    answer = print(*numbers, sep='')
    answer = ''
    for i in range(len(numbers)):
        answer += numbers[i]
    return answer

# solution([3, 30, 34, 5, 9])