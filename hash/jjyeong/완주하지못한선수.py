def solution(participant,completion):
    hash = dict()
    for e in participant:
        if e in hash:
            hash[e] +=1
        else:
            hash[e] =1
    o_hash = hash.copy()
    for p in completion:
        hash[p] += 1
    for k in list(hash.keys()):
        if hash[k] != o_hash[k]*2:
            break
    return k


'''
테스트 1 〉	통과 (24.29ms, 23MB)
테스트 2 〉	통과 (40.32ms, 27.9MB)
테스트 3 〉	통과 (43.18ms, 30.2MB)
테스트 4 〉	통과 (45.79ms, 36.3MB)
테스트 5 〉	통과 (50.70ms, 36.4MB)
'''