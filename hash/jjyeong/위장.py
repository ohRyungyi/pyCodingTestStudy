from functools import reduce

def multiply(some_list):
    return reduce(lambda x, y: x * y,some_list)

def solution(clothes):

    hash_table = dict()

    for cloth in clothes: #2차원배열 
        if hash_table.get(cloth[1]) == None : # 없다면 추가하자 
            hash_table[cloth[1]] = 2
        else: # 있으면 
            hash_table[cloth[1]] += 1

    values = list(hash_table.values())

    if len(values) == 1: 
        return values[0] - 1
    else:
        return multiply(values) -1
