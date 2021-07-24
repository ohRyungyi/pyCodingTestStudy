import hashlib
def hash_func(s):
    r = str(s*2)
    return r # 직접 해시함수 대충 만듦 -> 이럴필요없이 hash()쓰면 됨
N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
hash_tbl = {}
for i in n:
    key_i = hash_func(i)
    hash_tbl[key_i] = i # 처음 입력받은 수 hash dic에 저장
for i in m:
    key_i = hash_func(i) # 두번째로 입력받은 수를 hash key로 변환
    try:
        if hash_tbl[key_i]: # hash dic에 있으면 1
            print(1)
    except:
        print(0) # 없으면 0 출력