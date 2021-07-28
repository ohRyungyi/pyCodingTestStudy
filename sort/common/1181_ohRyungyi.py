import sys

N = int(sys.stdin.readline())
str_dict= dict()

for _ in range(N):
    data = sys.stdin.readline().split('\n')[0]
    
    if len(data) not in str_dict.keys():
        str_dict[len(data)] = list()
        str_dict[len(data)].append(data)
    else:
        if data not in str_dict[len(data)]:
            str_dict[len(data)].append(data)

str_list = sorted(str_dict.items() , key = lambda x : x[0])

for i in str_list:
    strs = i[1]
    strs.sort()

    for string in strs:
        print(string)