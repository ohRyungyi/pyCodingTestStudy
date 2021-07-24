import sys
dic = {}
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1  # 입력받은 책의 제목과 판매량을 딕셔너리에 저장 => dic = {'top':2, 'ai':2, 'no':1}

l_dic = list(zip(dic.keys(),dic.values()))  # list로 변환(이중정렬하려고) => l_dic = [['top', 2], ['ai', 2], ['no', 1]]
s_dic = sorted(l_dic, key = lambda x : (-x[1], x[0]))  # 판매량을 기준으로 내림차순, 이름을 기준으로 오름차순 정렬 => s_dic = [['ai', 2], ['top', 2], ['no', 1]]
print(s_dic[0][0])