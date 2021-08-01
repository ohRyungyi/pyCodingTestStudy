def solution(numbers):
    answer = ''
    num_dict = dict()
    for num in numbers:
        ind = int(str(num)[0])
        if ind not in num_dict.keys():
            num_dict[ind] = list()
            num_dict[ind].append(num)
        else :
            num_dict[ind].append(num)

    num_list = sorted(num_dict.items(), key = lambda x: x[0], reverse = True)
    for num in num_list:
        nums = num[1]
        # nums_list = sorted(nums , key = lambda x : x[1:], reverse = True)
        print(nums)
        # for n in nums:
        #     answer+=str(n)
        for n in  nums:
            
    return answer

# print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
