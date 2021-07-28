import sys
n = int(sys.stdin.readline())

for i in range(n):
    a, b = sys.stdin.readline().split()
    if sorted(a) == sorted(b):
        print(a, '&', b, 'are anagrams.')
    else:
        print(a, '&', b, 'are NOT anagrams.')

'''
입력 예시
3
blather reblath
maryland landam
bizarre brazier

출력 예시
blather & reblath are anagrams.
maryland & landam are NOT anagrams.
bizarre & brazier are anagrams.
'''