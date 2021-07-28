import sys

N = int(sys.stdin.readline())
judges = dict()
for i in range(N):
    age, name = sys.stdin.readline().split('\n')[0].split(' ')
    age = int(age)

    if age not in judges.keys():
        judges[age] = list()
        judges[age].append(name)
    else:
        judges[age].append(name)

judge_list = sorted(judges.items(), key = lambda x : x[0])

for i in judge_list:
    age = i[0]
    names = i[1]

    for name in names:
        print(age, name)