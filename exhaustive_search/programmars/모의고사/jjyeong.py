answers =[1,3,2,4,2]
answer = [] 
stu_1 = [1,2,3,4,5] * len(answers)
stu_2 = [2,1,2,3,2,4,2,5] * len(answers)
stu_3 = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    
score = {1:0, 2:0, 3:0}
for i in range(len(answers)): 
    if answers[i] == stu_1[i]:
        score[1] += 1 
    if answers[i] == stu_2[i]:
        score[2] += 1 
    if answers[i] == stu_3[i]:
        score[3] += 1 

a = sorted(list(score.items()), key=lambda x : (x[1]), reverse=True)
if a[0][1] != a[1][1]:
    answer.append(a[0][0])
elif a[1][1] != a[2][1]:
    answer.append(a[0][0])
    answer.append(a[1][0])
else:
    answer.append(a[0][0])
    answer.append(a[1][0])
    answer.append(a[2][0])

print(answer)