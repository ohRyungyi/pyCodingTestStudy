def solution(c):
    result = 1
    dic = {}
    for i in range(len(c)):
        dic[c[i][1]] = []
    kind = list(dic.keys()) #ex) kind = ['top', 'bottoms']
    for i in range(len(c)):
        dic[c[i][1]].append(c[i][0]) #ex) dic = {'top':['shirt','blouse'], 'bottoms'=['pants','skirt']}
    for i in kind:
        result *= (len(dic[i])+1) #'타입별옷개수+1' 곱한 것 - 1 (최소 1개는 착용해야 하므로 아무것도 착용하지 않은 경우 제외)
    return result - 1