from itertools import combinations


def solution(clothes):
    clothes_dict = {}

    for cloth in clothes:
        # print(cloth)
        if cloth[1] in clothes_dict:
            cloth[1] = clothes_dict.get(cloth[1]).extend([cloth[0]])
            print(clothes_dict)
        else:
            clothes_dict[cloth[1]] = [cloth[0]]
        # print(clothes_dict)

    values = list(clothes_dict.values())
    answer = 1
    for i in values:
        answer = answer * (len(i) + 1)

    answer = answer - 1

    return answer


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
#clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["a", "foot"], ["c", "foot"], ["d", "foot"], ["i", "up"], ["j", "up"], ["k", "up"]]
print(solution(clothes))

'''
입력 예시
clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

clothes = [["crowmask", "face"], [
    "bluesunglasses", "face"], ["smoky_makeup", "face"]]

출력 예시
5

3
'''
