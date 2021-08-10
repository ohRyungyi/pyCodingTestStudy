import sys
from itertools import permutations, combinations

L, C = list(map(int, sys.stdin.readline().split('\n')[0].split(' ')))

eng_list = list(map(str, sys.stdin.readline().split('\n')[0].split(' ')))

eng_list = sorted(eng_list)

ans = []

vowels = ['a', 'e', 'i', 'o', 'u']

alpha_list = [[], []]


def brute(engs, start):
    if len(engs) == L:
        cnt = 0
        for vowel in vowels:
            if vowel in engs:
                cnt +=1

        if cnt >= 1 and L-cnt >= 2:
            ans.append(''.join(engs))
    else:
        for ind in range(start, C):
            engs.append(eng_list[ind])
            brute(engs, ind+1)
            del engs[-1]

# brute([], 0)

for i in combinations(eng_list, L):
    cnt = 0
    for vowel in vowels:
        if vowel in i:
            cnt+=1
    if cnt >=1 and L-cnt >=2:
        print(''.join(i))
# for answer in ans:
#     print(answer)

'''
입력
4 6
a t c i s w

출력
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
'''