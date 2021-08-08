import sys 
from itertools import permutations, combinations

N = int(sys.stdin.readline()) #4
team_num = list(range(N)) #[0,1,2,3]
score_set = []
for _ in range(N):
    score_set.append(list(map(int, sys.stdin.readline().split())))
print(score_set)

# 먼저 팀 조합을 구해야함. 
min_deduct_val = 999999999
print(list(combinations(team_num, int(N/2))))
for one_combi in combinations(team_num, int(N/2)):
    
    team_copy = team_num.copy()
    for c in one_combi:
        team_copy.remove(c)
    the_other_combi = team_copy

    one_team_val = 0
    the_other_team_val = 0
    #print(f"combi : {one_combi}")
    for one_permu, the_other_permu in zip(permutations(one_combi,2),permutations(the_other_combi,2)): #(0,1) (1,0)
        #print(f"one_permu : {one_permu}")
        #print(f"the_other_permu : {the_other_permu}")
        one_team_val += score_set[one_permu[0]][one_permu[1]]
        the_other_team_val += score_set[the_other_permu[0]][the_other_permu[1]]
        #print(f"one_team_val : {one_team_val}")
        #print(f"one_team_val : {the_other_team_val}")


    #print(f"one_team_val : {one_team_val}")

    deduct_val = abs(the_other_team_val - one_team_val)
    #print(f"deduct_val : {deduct_val}")
    
    if deduct_val == 0:
        min_deduct_val = deduct_val
        #print("0이다")
        break 

    min_deduct_val = min(deduct_val, min_deduct_val)
    #print(f"min_deduct_val : {min_deduct_val}")

print(min_deduct_val)

'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''

'''
0
'''

'''
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
'''

'''
2
'''
