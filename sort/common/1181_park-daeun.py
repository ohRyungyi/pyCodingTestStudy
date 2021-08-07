import sys

n = int(sys.stdin.readline())
words = []

for i in range(n):
    word = sys.stdin.readline().rstrip()
    words.append((len(word), word))

words = set(words)
words = list(words)
words.sort(key = lambda x:(x[0], x[1]))

for w in words:
    print(w[1])

'''
입력 예시
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

출력 예시
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''